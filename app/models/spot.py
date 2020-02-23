from app.models.base import Base

from sqlalchemy import Column, Integer, Sequence, String, ARRAY

class Spot(Base):
    __tablename__ = 'spots'

    id = Column(Integer, primary_key=True)
    surfline_id = Column(String, nullable=False, unique=True)
    surfline_spot_id = Column(String, nullable=False, unique=True, index=True)
    name = Column(String, nullable=False, unique=True)
    favorable_swells = Column(ARRAY(String))

    def _asdict(self):
        return {
            'id': self.id,
            'surfline_id': self.surfline_id,
            'surfline_spot_id': self.surfline_spot_id,
            'name': self.name
        }