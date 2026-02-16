from app.db.extensions import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, relationship

class Talle(Base):
    __tablename__ = "talles"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)

    stocks: Mapped[list["Stock"]] = relationship("Stock", back_populates="talle")

    def __repr__(self):
        return f"Talle {self.id!r} Nombre: {self.nombre!r}"