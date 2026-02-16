from app.db.extensions import Base, engine
import sys

def migration():
    Base.metadata.create_all(engine)

migration()