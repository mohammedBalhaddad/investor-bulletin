from api.controllers.market_controllers import router as MarketRouter
from api.controllers.alert_rules_controller import router as RulesRouter
from api.controllers.alert_controller import router as AlertRouter

def init_routes(app):
    app.include_router(MarketRouter, prefix="/market-prices", tags=["Market"])
    app.include_router(AlertRouter, prefix="/alerts", tags=["Alerts"])
    app.include_router(RulesRouter, prefix="/alert-rules", tags=["Alert Rules"])
    return app
