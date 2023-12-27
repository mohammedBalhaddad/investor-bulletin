""" Alert Model """
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer ,String ,DateTime, null
from sqlalchemy.orm import relationship
from db.models.model_base import Base

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True)
    alert_rule_id = Column(Integer, ForeignKey("alert_rules.id"))

    # Timestamps
    created_at= Column(DateTime , default=datetime.utcnow, nullable=False)
    updated_at= Column(DateTime , default=datetime.utcnow, nullable=False)
    deleted_at= Column(DateTime , default=None, nullable=True)

    # Relationships
    rule = relationship("AlertRule", back_populates="alerts")
