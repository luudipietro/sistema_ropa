from extensions import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(255))
    imagen = Column(String(255))
    costo = Column(Float, default=0.0)
    precio = Column(Float, default=0.0)
    marca = Column(String(50)) #quiza marca podria ser otra tabla

    id_categoria: Mapped[int] = mapped_column(Integer, ForeignKey("categorias.id"))
    categoria: Mapped["Category"] = relationship("Categoria", back_populates="products")
    id_marca: Mapped[int] = mapped_column(Integer, ForeignKey("brand.id"))
    marca_rel: Mapped["Brand"] = relationship("Brand", back_populates="products")

    def __repr__(self):
        return f"Producto {self.id!r} {self.nombre!r}"