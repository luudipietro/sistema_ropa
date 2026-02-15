from sistema_ropa.app.extensions import Base
from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

class DetallePromocion(Base):
    __tablename__ = "detalles_promocion"

    id = Column(Integer, primary_key=True, index=True)
    cantidad = Column(Integer, nullable=False)
    precio_unitario_con_descuento = Column(Float, nullable=False)

    id_promocion: Mapped[int] = mapped_column(Integer, ForeignKey("promociones.id"), nullable=False)
    promocion: Mapped["Promocion"] = relationship("Promocion", back_populates="detalles")

    id_producto: Mapped[int] = mapped_column(Integer, ForeignKey("productos.id"), nullable=False)
    producto: Mapped["Producto"] = relationship("Producto", back_populates="detalles_promocion")

    def __repr__(self):
        return f"DetallePromocion {self.id!r} Promo: {self.id_promocion!r} Producto: {self.id_producto!r} Cant: {self.cantidad!r} PUdesc: {self.precio_unitario_con_descuento!r}"
