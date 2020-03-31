#!/usr/bin/python3
'''
State object with the name
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
    session = Session()
    Mex1 = session.query(State).filter(State.id == '2').first()
    Mex1.name = 'New Mexico'
    session.commit()
    session.close()
