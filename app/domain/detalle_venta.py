from app.db.extensions import Base
from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

class DetalleVenta(Base):
    __tablename__ = "detalles_venta"

    id = Column(Integer, primary_key=True, index=True)
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(Float, nullable=False)

    id_venta: Mapped[int] = mapped_column(Integer, ForeignKey("ventas.id"), nullable=False)
    venta: Mapped["Venta"] = relationship("Venta", back_populates="detalles")

    id_stock: Mapped[int] = mapped_column(Integer, ForeignKey("stocks.id"), nullable=False)
    stock: Mapped["Stock"] = relationship("Stock", back_populates="detalles_venta")

    id_promocion: Mapped[int] = mapped_column(Integer, ForeignKey("promociones.id"))
    promocion: Mapped["Promocion"] = relationship("Promocion", back_populates="detalles")

    def __repr__(self):
        return f"DetalleVenta {self.id!r} Venta: {self.id_venta!r} Stock: {self.id_stock!r} Cant: {self.cantidad!r} PU: {self.precio_unitario!r}"
