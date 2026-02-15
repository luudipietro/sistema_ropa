from sistema_ropa.app.extensions import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Mapped

class Color(Base):
    __tablename__ = "colores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)

    stocks: Mapped[list["Stock"]] = relationship("Stock", back_populates="color")

    def __repr__(self):
        return f"Color {self.id!r} Nombre: {self.nombre!r}"