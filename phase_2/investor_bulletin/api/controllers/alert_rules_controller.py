from typing import List
from fastapi import APIRouter, Depends
from resources.alert_rules.alert_rule_schema import AlertRule,AlertRuleCreate
from resources.alert_rules.alert_rule_dal import create_alert_rule, delete_alert_rule_by_id, get_alert_rules, update_alert_rule_by_id
from db.models.model_base import get_session
from sqlalchemy.orm import Session

router = APIRouter()


@router.get('',response_model=List[AlertRule])
def get_alert_rules_route(db: Session = Depends(get_session)):
    return get_alert_rules(session=db)


@router.post('',response_model=AlertRule)
def create_alert_rules_route(input_alert_rule : AlertRuleCreate , db: Session = Depends(get_session)):
    return create_alert_rule(alert_rule=input_alert_rule , session=db)


@router.patch('/{id}')
def update_alert_rules_route(id:int,new_alert_rule : AlertRuleCreate , db: Session = Depends(get_session)):
    return update_alert_rule_by_id(session=db,alert_rule_id=id,alert_rule=new_alert_rule)


@router.delete('/{id}')
def delete_alert_rules_route(id:int,db: Session = Depends(get_session)):
    return delete_alert_rule_by_id(session=db,alert_rule_id=id)
