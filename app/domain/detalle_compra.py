from sistema_ropa.app.extensions import Base
        return f"DetalleCompra {self.id!r} Compra: {self.id_compra!r} Stock: {self.id_stock!r} Cant: {self.cantidad!r} CostoU: {self.costo_unitario!r}"
    def __repr__(self):

    stock: Mapped["Stock"] = relationship("Stock", back_populates="detalles_compra")
    id_stock: Mapped[int] = mapped_column(Integer, ForeignKey("stocks.id"), nullable=False)

    compra: Mapped["Compra"] = relationship("Compra", back_populates="detalles")
    id_compra: Mapped[int] = mapped_column(Integer, ForeignKey("compras.id"), nullable=False)

    costo_unitario = Column(Float, nullable=False)
    cantidad = Column(Integer, nullable=False)
    id = Column(Integer, primary_key=True, index=True)

    __tablename__ = "detalles_compra"
class DetalleCompra(Base):

from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import Column, Integer, Float, ForeignKey
