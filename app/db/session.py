import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = os.getenv('DB_URL', 'postgresql://localhost/stoke_archives') 
engine = create_engine(db_url)

Session = sessionmaker(bind=engine)