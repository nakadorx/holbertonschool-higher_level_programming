#!/usr/bin/python3
"""
con
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """ con"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all,delete", backref='state')
