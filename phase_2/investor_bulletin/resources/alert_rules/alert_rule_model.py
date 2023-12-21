""" Alert Rule Model """
from datetime import datetime
from db.models.model_base import Base
from sqlalchemy import Column, Double, Integer ,String ,DateTime
from sqlalchemy.orm import relationship

class AlertRule(Base):
    __tablename__ = "alert_rules"

    # Fields
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price_threshold = Column(Double)
    symbol= Column(String)

    # Timestamps
    created_at= Column(DateTime , default=datetime.utcnow, nullable=False)
    updated_at= Column(DateTime , default=datetime.utcnow, nullable=False)
    deleted_at= Column(DateTime , default=None, nullable=True)

    # Relationships
    alerts = relationship("Alert", back_populates="rule")
