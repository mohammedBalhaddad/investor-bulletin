""" Model base """

from .model_base import Base,engine
from .models import *

AlertRule.metadata.create_all(bind=engine, checkfirst=True)
Alert.metadata.create_all(engine)
