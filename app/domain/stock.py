from extensions import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column


class Stock(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, index=True)
    cantidad = Column(Integer, default=0)

    id_producto: Mapped[int] = mapped_column(Integer, ForeignKey("products.id"))
    producto: Mapped["Product"] = relationship("Product", back_populates="stock")
    id_color: Mapped[int] = mapped_column(Integer, ForeignKey("colors.id"))
    color: Mapped["Color"] = relationship("Color", back_populates="stocks")
    id_talle: Mapped[int] = mapped_column(Integer, ForeignKey("sizes.id"))
    talle: Mapped["Size"] = relationship("Size", back_populates="stocks")
    id_sucursal: Mapped[int] = mapped_column(Integer, ForeignKey("branches.id"))
    sucursal: Mapped["Store"] = relationship("Branch", back_populates="stocks")

    def __repr__(self):
        return f"Stock {self.id!r} Cantidad: {self.cantidad!r} Producto: {self.producto.nombre!r} Color: {self.color.nombre!r} Talle: {self.talle.nombre!r} Sucursal: {self.sucursal.nombre!r}"