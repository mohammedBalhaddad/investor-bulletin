""" Alert Rule  DAL"""
"""_summary_
this file is to right any ORM logic for the Alert Rule model
"""
from sqlalchemy.orm import Session
from resources.alert_rules.alert_rule_schema import AlertRuleCreate
from db.models import AlertRule


# encapsulate the logic of creating an alert rule
def create_alert_rule(session : Session, alert_rule: AlertRuleCreate):
    new_rule = AlertRule(
        name = alert_rule.name,
        price_threshold = alert_rule.price_threshold,
        symbol = alert_rule.symbol)
    session.add(new_rule)
    session.commit()
    session.refresh(new_rule)
    return new_rule


# encapsulate the logic of retreving all alert rules
def get_alert_rules( session: Session, skip: int = 0, limit: int = 100):
    return session.query(AlertRule).offset(skip).limit(limit).all()


# encapsulate the logic of retreving alert rule by id
def get_alert_rule_by_id( session: Session, alert_rule_id: int):
    return session.query(AlertRule).filter(AlertRule.id == alert_rule_id).first()


# encapsulate the logic of deleting alert rule by id
def delete_alert_rule_by_id( session: Session, alert_rule_id: int):
    session.query(AlertRule).filter(AlertRule.id == alert_rule_id).delete()
    session.commit()
    return True;


# encapsulate the logic of updating alert rule by id
def update_alert_rule_by_id( session: Session, alert_rule_id: int, alert_rule: AlertRuleCreate):
    session.query(AlertRule).filter(AlertRule.id == alert_rule_id).update(alert_rule.model_dump())
    session.commit()
    return True;
