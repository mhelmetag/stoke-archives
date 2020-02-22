from app.models.base import Base

from sqlalchemy import Column, Integer, Sequence, ForeignKey, DateTime, String, Float

class Forecast(Base):
    __tablename__ = 'forecasts'

    id = Column(Integer, primary_key=True)
    spot_id = Column(Integer, ForeignKey('spots.id', ondelete='CASCADE'), index=True)
    timestamp = Column(DateTime, nullable=False, index=True)
    am_min_height = Column(Integer, nullable=False)
    am_max_height = Column(Integer, nullable=False)
    am_rating = Column(String, nullable=False)
    pm_min_height = Column(Integer, nullable=False)
    pm_max_height = Column(Integer, nullable=False)
    pm_rating = Column(String, nullable=False)
    swell1_height = Column(Float, nullable=False)
    swell1_period = Column(Integer, nullable=False)
    swell1_direction = Column(Float, nullable=False)
    swell2_height = Column(Float, nullable=False)
    swell2_period = Column(Integer, nullable=False)
    swell2_direction = Column(Float, nullable=False)
    swell3_height = Column(Float, nullable=False)
    swell3_period = Column(Integer, nullable=False)
    swell3_direction = Column(Float, nullable=False)