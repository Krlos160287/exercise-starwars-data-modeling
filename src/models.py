import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er


Base = declarative_base()

class Users(Base):
    __tablename__ = 'Users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastName = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    Favorites = relationship("Favorites")
class Favorites(Base):
    __tablename__ = 'Favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    Users_id = Column(Integer, ForeignKey("Users.id"))
    Characters_id = Column(Integer, ForeignKey("Characters.id"))
    Planets_id = Column(Integer, ForeignKey("Planets.id"))
    Starships_id = Column(Integer, ForeignKey("Starships.id"))
class Characters (Base):
    __tablename__ = "Characters"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    mass = Column(String(250), nullable=False)
    hairColor = Column(String(250), nullable=False)
    eyesColor = Column(String(250), nullable=False)
    birthdate = Column(String(250), nullable=False)
    Favorites = relationship("Favorites")
class Planets (Base):
    __tablename__ = "Planets"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    diameter = Column(String(250), nullable=False)
    Favorites = relationship("Favorites")
class Starships (Base):
    __tablename__ = "Starships"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable= False)
    type = Column(String(250), nullable = False)
    model = Column(String(250), nullable=False)
    passengers= Column(String(250), nullable=False)
    crew = Column(String(250), nullable=False)
    length = Column(String(250), nullable=False)
    Favorites = relationship("Favorites")

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')