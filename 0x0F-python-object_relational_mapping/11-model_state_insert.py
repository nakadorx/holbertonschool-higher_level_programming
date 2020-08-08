#!/usr/bin/python3
""" this script adds a new object to states table in the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker


def mainx():
    """ main function """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    newS = State(name='Louisiana')
    session.add(newS)
    session.commit()
    print(newS.id)
    session.close()


if __name__ == '__main__':
    mainx()
