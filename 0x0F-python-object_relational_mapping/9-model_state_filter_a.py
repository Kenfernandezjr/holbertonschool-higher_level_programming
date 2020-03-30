#!/usr/bin/python3
""" """

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
    for u in session.query(State).filter(State.name.like('%a')).order_by(asc(State.id)):
        print("{}: {}".format(u.id, u.name))

    session.close()
