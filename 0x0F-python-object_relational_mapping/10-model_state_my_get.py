#!/usr/bin/python3
""" con
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker


def maix():
    """con"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    state = session.query(State).filter_by(name=sys.argv[4]).first()
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
    session.close()

if __name__ == "__main__":
    maix()
