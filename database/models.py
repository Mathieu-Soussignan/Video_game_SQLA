from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# Table `Genre`
class Genre(Base):
    __tablename__ = "genre"
    id_genre = Column(Integer, primary_key=True)
    nom_genre = Column(String(255))

# Table `Editeur`
class Editeur(Base):
    __tablename__ = "editeur"
    id_editeur = Column(Integer, primary_key=True)
    nom_editeur = Column(String(255))

# Table `Plateforme`
class Plateforme(Base):
    __tablename__ = "plateforme"
    id_plateforme = Column(Integer, primary_key=True)
    nom_plateforme = Column(String(255))

# Table `Annee_de_sortie`
class AnneeDeSortie(Base):
    __tablename__ = "annee_de_sortie"
    id_sortie = Column(Integer, primary_key=True)
    date = Column(Integer)

# Table `Jeu_video`
class JeuVideo(Base):
    __tablename__ = "jeu_video"
    id_jeu = Column(Integer, primary_key=True)
    titre = Column(String(255))
    
    # Clés étrangères vers d'autres tables
    id_genre = Column(Integer, ForeignKey('genre.id_genre'))
    id_editeur = Column(Integer, ForeignKey('editeur.id_editeur'))
    id_plateforme = Column(Integer, ForeignKey('plateforme.id_plateforme'))
    id_sortie = Column(Integer, ForeignKey('annee_de_sortie.id_sortie'))

    # Relations
    genre = relationship("Genre", backref="jeux")
    editeur = relationship("Editeur", backref="jeux")
    annee_sortie = relationship("AnneeDeSortie", backref="jeux")
    plateforme = relationship("Plateforme", backref="jeux")

# Table `Ventes`
class Ventes(Base):
    __tablename__ = "ventes"
    id_ventes = Column(Integer, primary_key=True)
    id_jeu = Column(Integer, ForeignKey('jeu_video.id_jeu'))
    
    # Champs de ventes par région
    na_sales = Column(Float)
    eu_sales = Column(Float)
    jp_sales = Column(Float)
    other_sales = Column(Float)
    global_sales = Column(Float)

    # Relation avec `JeuVideo`
    jeu = relationship("JeuVideo", backref="ventes")