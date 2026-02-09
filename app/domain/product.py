from extensions import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(255))
    imagen = Column(String(255))
    id_categoria = Column(Integer, ForeignKey("categorias.id"))
    costo = Column(Float, default=0.0)
    precio = Column(Float, default=0.0)
    marca = Column(String(50)) #quiza marca podria ser otra tabla

    def __repr__(self):
        return f"Producto {self.id!r} {self.nombre!r}"