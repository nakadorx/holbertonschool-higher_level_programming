#!/usr/bin/python3
""" tcon
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker


def mainx():
    """ con """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    new_state = State(name='Louisiana')
    state = session.add(new_state)
    state = session.query(State).filter_by(name='Louisiana').first()
    print("{}".format(state.id))
    session.commit()
    session.close()


if __name__ == '__main__':
    mainx()
