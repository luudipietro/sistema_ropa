from app.db.extensions import Base
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy import Column, Integer, String

class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)

    productos: Mapped[list["Producto"]] = relationship("Producto", back_populates="categoria")

    def __repr__(self):
        return f"Categoria {self.id!r} {self.nombre!r}"