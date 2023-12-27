import json
from amqpstorm import Message
from amqpstorm import Connection
from celery import Celery
from datetime import timedelta

from sqlalchemy import null
from resources.market.market_service import get_market_data
from resources.alert_rules.alert_rule_dal import get_alert_rules
from dotenv import load_dotenv
from db.models.model_base import get_session

# Load the .env file
load_dotenv()

# RabiitMQ Connection
broker = Connection("localhost", "guest", "guest")
channel = broker.channel()
channel.queue.declare('THRESHOLD_ALERT')
properties = { 'content_type': 'text/plain' }

# Create a celery app object to start your workers
app = Celery('app', broker='pyamqp://guest@localhost//',backend='rpc://')
app.conf.beat_schedule = {
    'fetch-every-5-seconds': {
        'task': 'worker.app.get_market_data_task',
        'schedule': timedelta(minutes=5),
    },
}
app.conf.timezone = 'UTC'

# this should be in a caching (e.g. redis ) or at least in db
# for the sake of simplicity we will use a dictionary
last_prices = {};


@app.task
def get_market_data_task():
  db_session = next(get_session())

  try:
    # get needed data
    rules = get_alert_rules(session=db_session)
    market_data = get_market_data()
    if(market_data == null):
      print('PapidAPI Rate Limit Exceeded')
      return

    # use to imitate a market data crossing the threshold
    # market_data = {
    #   'AAPL': {'price': '193.53000'},
    #   'MSFT': {'price': '374.60501'},
    #   'GOOG': {'price': '142.75999'},
    #   'AMZN': {'price': '153.44501'},
    #   'META': {'price': '353.42001'}
    # }

    # loop on each symbol from the market data
    for symbol,price_dict in market_data.items():
      price = float(price_dict['price'])
      if symbol in last_prices:
        filtered_rules = list(filter(lambda rule: rule.symbol == symbol and rule.isNotified == False, rules))
        for rule in filtered_rules:
          if price <= rule.price_threshold <= last_prices[symbol]: # price crossed the threshold going down
            print('Rule of Symbol ' + symbol + ' was crossed ( decreasing )')
            send_message({'alert_rule_id' : rule.id})
          elif last_prices[symbol] <= rule.price_threshold <= price : # price crossed the threshold going up
            print('Rule of Symbol ' + symbol + ' was crossed ( increasing )')
            send_message({'alert_rule_id' : rule.id})
          else:
            print('Rule of Symbol ' + symbol + ' was not crossed')
      last_prices[symbol] = price
  finally:
      db_session.close()

def send_message(body):
  message = Message.create(channel=channel, body=json.dumps(body), properties=properties)
  message.publish("THRESHOLD_ALERT")
