from typing import List
from resources.alerts.alert_schema import Alert
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.models.model_base import get_session
from resources.alerts.alert_dal import get_alerts


router = APIRouter()


@router.get('', response_model=List[Alert])
def get_alerts_route(db : Session = Depends(get_session)):
    return get_alerts(session=db)
