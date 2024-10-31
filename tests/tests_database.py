import pytest 
import sqlalchemy
import os
import sys
sys.path.insert(0,
                os.path.abspath(
                    os.path.join(
                        os.path.dirname(__file__),
                        ".."
                    ) ))
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, declarative_base
from database.models import Base, Genre, Editeur, Plateforme, AnneeDeSortie, Name
from database.database import  Session

@pytest.fixture()
def db_session():
    # Crée base de donées en memoire
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    session = Session()
    yield session 
    session.close()  

# Test de Table `genre`
def test_genre(db_session):
    new_genre= Genre(nom_genre="Sport")
    db_session.add(new_genre)
    db_session.commit()
    assert db_session.query(Genre).filter_by(nom_genre="Sport").first() is not None


# Test de Table `editeur`
def test_editeur(db_session):
    new_editeur= Editeur(nom_editeur="Nintendo")
    db_session.add(new_editeur)
    db_session.commit()
    assert db_session.query(Editeur).filter_by(nom_editeur="Nintendo").first() is not None


# Test de Table `Plateforme`
def test_plateforme(db_session):
    new_plateforme = Plateforme(nom_plateforme='Wii')
    db_session.add(new_plateforme)
    db_session.commit()
    assert db_session.query(Plateforme).filter_by(nom_plateforme='Wii').first() is not None


# Test de Table `Annee_de_sortie`
def test_AnneeDeSortie(db_session):
    new_sortie = AnneeDeSortie(date='2020')
    db_session.add(new_sortie)
    db_session.commit()
    assert db_session.query(AnneeDeSortie).filter_by(date='2020').first() is not None


def test_jeu_video(db_session):
    new_titre = Name(title="Super Mario")
    db_session.add(new_titre)
    db_session.commit()
    assert db_session.query(Name).filter_by(title="Super Mario").first() is not None