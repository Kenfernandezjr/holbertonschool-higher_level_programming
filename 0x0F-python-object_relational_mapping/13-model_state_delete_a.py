#!/usr/bin/python3
'''
objects that contain the letter a
'''

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import asc
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]))

    Session = sessionmaker(engine)
    Session.configure(bind=engine)
    session = Session()
    query1 = session.query(State).filter(State.name.ilike('%a%'))
    for u in query1:
        session.delete(u)
    session.commit()
    session.close()
