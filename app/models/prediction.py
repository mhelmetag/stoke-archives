from app.models.base import Base

from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float


class Prediction(Base):
    __tablename__ = 'predictions'

    id = Column(Integer, primary_key=True)
    spot_id = Column(Integer, ForeignKey(
        'spots.id', ondelete='CASCADE'), nullable=False, index=True)
    created_on = Column(DateTime, nullable=False, index=True)
    forecasted_for = Column(DateTime, nullable=False, index=True)
    surfline_height = Column(Float, nullable=False)
    stoke_height = Column(Float, nullable=False)
    swell1_height = Column(Float, nullable=False)
    swell1_period = Column(Integer, nullable=False)
    swell1_direction = Column(Float, nullable=False)
    swell2_height = Column(Float, nullable=False)
    swell2_period = Column(Integer, nullable=False)
    swell2_direction = Column(Float, nullable=False)
    swell3_height = Column(Float, nullable=False)
    swell3_period = Column(Integer, nullable=False)
    swell3_direction = Column(Float, nullable=False)
    swell4_height = Column(Float, nullable=False)
    swell4_period = Column(Integer, nullable=False)
    swell4_direction = Column(Float, nullable=False)
    swell5_height = Column(Float, nullable=False)
    swell5_period = Column(Integer, nullable=False)
    swell5_direction = Column(Float, nullable=False)
    swell6_height = Column(Float, nullable=False)
    swell6_period = Column(Integer, nullable=False)
    swell6_direction = Column(Float, nullable=False)

    def _asdict(self):
        return {
            'id': self.id,
            'spot_id': self.spot_id,
            'created_on': self.created_on.isoformat(),
            'forecasted_for': self.forecasted_for.isoformat(),
            'surfline_height': self.surfline_height,
            'stoke_height': self.stoke_height,
            'swell1_height': self.swell1_height,
            'swell1_period': self.swell1_period,
            'swell1_direction': self.swell1_direction,
            'swell2_height': self.swell2_height,
            'swell2_period': self.swell2_period,
            'swell2_direction': self.swell1_direction,
            'swell3_height': self.swell3_height,
            'swell3_period': self.swell3_period,
            'swell3_direction': self.swell1_direction,
            'swell4_height': self.swell4_height,
            'swell4_period': self.swell4_period,
            'swell4_direction': self.swell4_direction,
            'swell5_height': self.swell5_height,
            'swell5_period': self.swell5_period,
            'swell5_direction': self.swell5_direction,
            'swell6_height': self.swell6_height,
            'swell6_period': self.swell6_period,
            'swell6_direction': self.swell6_direction
        }
