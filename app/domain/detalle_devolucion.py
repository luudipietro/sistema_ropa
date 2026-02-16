from app.db.extensions import Base
from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

class DetalleDevolucion(Base):
    __tablename__ = "detalles_devolucion"

    id = Column(Integer, primary_key=True, index=True)
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(Float, nullable=False)

    id_cambio: Mapped[int] = mapped_column(Integer, ForeignKey("cambios.id"), nullable=False)
    cambio: Mapped["Cambio"] = relationship("Cambio", back_populates="detalles")

    id_stock: Mapped[int] = mapped_column(Integer, ForeignKey("stocks.id"), nullable=False)
    stock: Mapped["Stock"] = relationship("Stock", back_populates="detalles_devolucion")

    def __repr__(self):
        return f"DetalleDevolucion {self.id!r} Cambio: {self.id_cambio!r} Stock: {self.id_stock!r} Cant: {self.cantidad!r} PU: {self.precio_unitario!r}"
