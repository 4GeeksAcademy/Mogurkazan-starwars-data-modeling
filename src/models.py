import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Starships(Base):
    __tablename__ = 'starships'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Fav_planet(Base):
    __tablename__ = 'fav_planet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    planet_id = Column(Integer, ForeignKey('planets.id'), primary_key=True)
    users = relationship(Users)
    planets = relationship(Planets)

class Fav_character(Base):
    __tablename__ = 'fav_character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.id'), primary_key=True)
    users = relationship(Users)
    characters = relationship(Characters)

class Fav_starship(Base):
    __tablename__ = 'fav_starship'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    starship_id = Column(Integer, ForeignKey('starships.id'), primary_key=True)
    users = relationship(Users)
    starships = relationship(Starships)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
