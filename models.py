from sqlalchemy import create_engine
from sqlalchemy.orm import Session

def conntect_db():
    engine = create_engine('', conn_args = {} )
    session = Session(bind= engine.connect())
    return session