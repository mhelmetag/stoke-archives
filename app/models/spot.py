from sqlalchemy import Column, Integer, Sequence, String

from app.models.base import Base

class Spot(Base):
    __tablename__ = 'spots'

    id = Column(Integer, Sequence('id'), primary_key=True)
    surfline_id = Column(String, nullable=False, unique=True)
    surfline_spot_id = Column(String, nullable=False, unique=True, index=True)
    name = Column(String, nullable=False, unique=True)