""" Alert Rule Schema """
"""_summary_
This file to abstract any validation logic for the Alert Rules
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel

# Father Schema contains shared attributes
class AlertRuleBase(BaseModel):
    name: str
    price_threshold: float
    symbol: str

# Schema for creating an Alert Rule Model
class AlertRuleCreate(AlertRuleBase):
    ...

# Schema for retreving an Alert Rule Model
class AlertRule(AlertRuleBase):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]

    class Config:
        orm_mode = True
