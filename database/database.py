from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base

engine = create_engine('sqlite:///database//vgsale.db', echo=True)

Session = sessionmaker(bind=engine)
def create_session():
    return Session()
