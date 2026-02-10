from extensions import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column


class Brand(Base):
    __tablename__ = "brands"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)

    products: Mapped[list['Product']] = relationship('Product', back_populates='brand')

    def __repr__(self):
        return f"Marca {self.id!r} {self.nombre!r}"
