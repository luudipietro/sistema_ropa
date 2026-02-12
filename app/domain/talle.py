from extensions import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Size(Base):
    __tablename__ = "sizes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)

    stocks: Mapped[list["Stock"]] = relationship("Stock", back_populates="talle")

    def __repr__(self):
        return f"Talle {self.id!r} Nombre: {self.nombre!r}"