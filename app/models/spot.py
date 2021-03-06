from app.models.base import Base

from sqlalchemy import Column, Integer, String, ARRAY, Boolean


class Spot(Base):
    __tablename__ = 'spots'

    id = Column(Integer, primary_key=True)
    surfline_id = Column(String, nullable=False, unique=True)
    surfline_spot_id = Column(String, nullable=False, unique=True, index=True)
    name = Column(String, nullable=False)
    favorable_swells = Column(ARRAY(String))
    gathering_data = Column(Boolean, nullable=False, index=True)

    def _asdict(self):
        return {
            'id': self.id,
            'surfline_id': self.surfline_id,
            'surfline_spot_id': self.surfline_spot_id,
            'name': self.name,
            'favorable_swells': self.favorable_swells,
            'gathering_data': self.gathering_data
        }
