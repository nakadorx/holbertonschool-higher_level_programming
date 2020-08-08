#!/usr/bin/python3
""" a script that lists only first State object from the database hbtn_0e_6_usa
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
    instance = session.query(State).first()
    if instance is None:
        print("Nothing")
    else:
        print(str(instance.id) + ': ' + instance.name)
    session.close()


if __name__ == '__main__':
    mainx()
