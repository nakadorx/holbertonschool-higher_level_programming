#!/usr/bin/python3
"""
con
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """ con """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, nullable=False)

    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
