from fastapi import APIRouter
# from resources.alert_rules.alert_rule_service import get_market_data
router = APIRouter()

@router.get('')
def get_alerts_route():
    return "Get all alerts"
