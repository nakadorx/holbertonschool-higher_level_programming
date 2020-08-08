#!/usr/bin/python3
""" con """
import sys
from relationship_state import Base, State, City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def mainx():
""" con """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    px = State(name='California')
    city = City(name='San Francisco')
    px.cities.append(city)
    session.add(px)
    session.commit()
    session.close()


if __name__ == '__main__':
    mainx()

