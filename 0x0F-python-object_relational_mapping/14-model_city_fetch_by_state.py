#!/usr/bin/python3
""" con """
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker


def mainx():
    """ con """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for inst, st in session.query(City, State)\
            .filter(City.state_id == State.id).order_by(asc(City.id)):
        print("{}: ({}) {}".format(st.name, inst.id, inst.name))
    session.close()


if __name__ == '__main__':
    mainx()
