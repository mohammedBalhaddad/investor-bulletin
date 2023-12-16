from fastapi import APIRouter
# from resources.alert_rules.alert_rule_service import get_market_data
router = APIRouter()

@router.get('')
def get_alert_rules_route():
    return "Get all alerts rules"

@router.post('')
def create_alert_rules_route():
    return "Creates an alert rule with the following properties: name, threshold price, and symbol."

@router.patch('/{id}')
def update_alert_rules_route(id):
    return "Update an alert rule by ID"

@router.delete('/{id}')
def delete_alert_rules_route(id):
    return "Deletes an alert rule by ID"
