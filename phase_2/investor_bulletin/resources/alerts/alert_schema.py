""" Alert Schema """
"""_summary_
This file to abstract any validation logic for the Alerts
"""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel


# Father Schema contains shared attributes
class AlertBase(BaseModel):
    alert_rule_id: int


# Schema for creating an Alert Rule Model
class AlertCreate(AlertBase):
    ...


# Schema for retreving an Alert Rule Model
class Alert(AlertBase):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]

    class Config :
        orm_mode = True
