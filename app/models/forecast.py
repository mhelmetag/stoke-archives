from app.models.base import Base

import datetime

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

    def _asdict(self):
        return {
            'id': self.id,
            'spot_id': self.spot_id,
            'timestamp': self.timestamp.isoformat(),
            'am_min_height': self.am_min_height,
            'am_max_height': self.am_max_height,
            'am_rating': self.am_rating,
            'pm_min_height': self.pm_min_height,
            'pm_max_height': self.pm_max_height,
            'pm_rating': self.pm_rating,
            'swell1_height': self.swell1_height,
            'swell1_period': self.swell1_period,
            'swell1_direction': self.swell1_direction,
            'swell2_height': self.swell2_height,
            'swell2_period': self.swell2_period,
            'swell2_direction': self.swell1_direction,
            'swell3_height': self.swell3_height,
            'swell3_period': self.swell3_period,
            'swell3_direction': self.swell1_direction
        }