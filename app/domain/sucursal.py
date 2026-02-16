from app.db.extensions import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Mapped


class Sucursal(Base):
    __tablename__ = "sucursales"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)

    stocks: Mapped[list['Stock']] = relationship('Stock', back_populates='sucursal')
    ventas: Mapped[list['Venta']] = relationship('Venta', back_populates='sucursal')
    cambios: Mapped[list['Cambio']] = relationship('Cambio', back_populates='sucursal')

    def __repr__(self):
        return f"Sucursal {self.id!r} {self.nombre!r}"