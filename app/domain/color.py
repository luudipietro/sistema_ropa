from extensions import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

class Color(Base):
    __tablename__ = "colors"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)

    stocks: Mapped[list["Stock"]] = relationship("Stock", back_populates="color")

    def __repr__(self):
        return f"Color {self.id!r} Nombre: {self.nombre!r}"