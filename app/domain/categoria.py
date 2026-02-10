from extensions import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import Column, Integer, String, ForeignKey

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)

    products: Mapped[list["Product"]] = relationship("Product", back_populates="categoria")

    def __repr__(self):
        return f"Categoria {self.id!r} {self.nombre!r}"