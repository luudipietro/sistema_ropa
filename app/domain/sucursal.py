from extensions import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column


class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)

    stocks: Mapped[list['Stock']] = relationship('Stock', back_populates='branch')

    def __repr__(self):
        return f"Sucursal {self.id!r} {self.nombre!r}"