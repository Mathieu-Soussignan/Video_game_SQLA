from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String

# Création de la base de données
Base = declarative_base()

# Déclaration de la table `Genre`
class Genre(Base):
    __tablename__ = "Genre"
    id_genre = Column(Integer,primary_key=True)
    Nom_genre = Column(String(255))
    
# Déclaration de la table `Editeur`
class Editeur(Base):
    __tablename__ = "Editeur"
    id_editeur = Column(Integer,primary_key=True)
    Nom_editeur = Column(String(255))

# Déclaration de la table `Plateforme`
class Plateforme(Base):
    __tablename__ = "Plateforme"
    id_plateforme = Column(Integer,primary_key=True)
    Nom_plateforme = Column(String(255))
    
# Déclaration de la table `Annee de sortie`
class Annee(Base):
    __tablename__ = "Annee de sortie"
    id_sortie = Column(Integer,primary_key=True)
    date = Column(Integer)

# Déclaration de la table `jeu video`
class jeu_video(Base):
    __tablename__ = "Jeu video"
    id_jeu = Column(Integer,primary_key=True)
    titre = Column(String(255))
    
    id_genre = Column(Integer)
    id_editeur = Column(Integer)
    id_plateforme = Column(Integer)
    id_sortie = Column(Integer)


    Genre = relationship(
        'Genre',
        primaryjoin='Genre.id_genre == jeu_video.id_genre',
        foreign_keys=id_genre
    )

    Editeur = relationship(
        'Editeur',
        primaryjoin='Editeur.id_editeur == jeu_video.id_editeur',
        foreign_keys=id_editeur
    )

    Annee = relationship(
        'Annee de sotrie',
        primaryjoin = 'Annee.id_sortie == jeu_video.id_sortie',
        foreign_keys = id_sortie
    )

    Plateforme = relationship(
        'Plateforme',
        primaryjoin = 'Plateforme.id_plateforme == Jeu_video.id_plateforme',
        foreign_keys = id_plateforme
    )

# Déclaration de la table `ventes`
class Ventes(Base):
    __tablename__ = "Ventes"
    id_Ventes = Column(Integer,primary_key=True)
    NA_Sales = Column(float)
    EU_Sales = Column(float)
    JP_Sales = Column(float)
    Other_Sales = Column(float)
    Global_Sales = Column(float)
    
    id_jeu = Column(Integer)

    jeu_video = relationship(
        'Jeu video',
        primaryjoin = 'ventes.id_jeu == jeu_video.id_jeu',
        foreign_keys = id_jeu
    )
