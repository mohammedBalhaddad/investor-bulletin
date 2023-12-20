""" Alert DAL"""
"""_summary_
this file is to right any ORM logic for the Alert model
"""
from resources.alerts.alert_schema import AlertCreate
from sqlalchemy.orm import Session
from db.models import Alert

# encapsulate the logic of creating an alert
def create_alert( alert: AlertCreate, session : Session):
    new_alert = Alert()
    new_alert.alert_rule_id = alert.alert_rule_id
    session.add(new_alert)
    session.commit()
    session.refresh(new_alert)
    return new_alert

# encapsulate the logic of retriving all alerts
def get_alerts( session: Session, skip: int = 0, limit: int = 100):
    return session.query(Alert).offset(skip).limit(limit).all()
