from sistema_ropa.app.extensions import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Mapped


class Marca(Base):
    __tablename__ = "marcas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)

    productos: Mapped[list['Producto']] = relationship('Producto', back_populates='marca')

    def __repr__(self):
        return f"Marca {self.id!r} {self.nombre!r}"
