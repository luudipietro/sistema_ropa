from sistema_ropa.app.extensions import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(255))
    imagen = Column(String(255))
    costo = Column(Float, default=0.0)
    precio = Column(Float, default=0.0)

    id_categoria: Mapped[int] = mapped_column(Integer, ForeignKey("categorias.id"))
    categoria: Mapped["Categoria"] = relationship("Categoria", back_populates="productos")

    id_marca: Mapped[int] = mapped_column(Integer, ForeignKey("marcas.id"))
    marca: Mapped["Marca"] = relationship("Marca", back_populates="productos")

    stocks: Mapped[list["Stock"]] = relationship("Stock", back_populates="producto")
    detalles_promocion: Mapped[list["DetallePromocion"]] = relationship("DetallePromocion", back_populates="producto")

    def __repr__(self):
        return f"Producto {self.id!r} {self.nombre!r}"