from app.models.base import Base

from sqlalchemy import Column, Integer, Sequence, String

class Spot(Base):
    __tablename__ = 'spots'

    id = Column(Integer, primary_key=True)
    surfline_id = Column(String, nullable=False, unique=True)
    surfline_spot_id = Column(String, nullable=False, unique=True, index=True)
    name = Column(String, nullable=False, unique=True)