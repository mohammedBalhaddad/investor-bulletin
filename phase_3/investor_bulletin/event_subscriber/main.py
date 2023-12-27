import json
from pika import BlockingConnection,ConnectionParameters
from resources.alert_rules.alert_rule_dal import mark_alert_rule_notified
from resources.alerts.alert_dal import create_alert
from resources.alerts.alert_schema import AlertCreate
from db.models.model_base import get_session

def init_subscriber():
  return BlockingConnection(ConnectionParameters(host='localhost',port=5672))

def on_event(ch, method, properties, body):
  db_session = next(get_session())
  print(f"Received new message {body}")
  # TODO : Need to be in a tansactions
  rule_id = json.loads(body)['alert_rule_id']
  new_alert =  AlertCreate(alert_rule_id = rule_id )
  create_alert(session=db_session,alert=new_alert)# create alert
  mark_alert_rule_notified(session=db_session,alert_rule_id=rule_id) # update rule isNotified to true


if __name__ == "__main__":
  subscriber = init_subscriber()
  channel = subscriber.channel()
  channel.queue_declare(queue='THRESHOLD_ALERT')
  channel.basic_consume(queue='THRESHOLD_ALERT', auto_ack=True ,on_message_callback=on_event)
  print("Start Consuming")
  channel.start_consuming()
