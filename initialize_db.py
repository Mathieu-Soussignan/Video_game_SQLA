from database.database import engine
from database.models import Base

# Créer toutes les tables définies dans models.py
Base.metadata.create_all(engine)
print("Tables créées avec succès.")