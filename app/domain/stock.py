from app.db.extensions import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column


class Stock(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, index=True)
    cantidad = Column(Integer, default=0)

    id_producto: Mapped[int] = mapped_column(Integer, ForeignKey("productos.id"))
    producto: Mapped["Producto"] = relationship("Producto", back_populates="stocks")

    id_color: Mapped[int] = mapped_column(Integer, ForeignKey("colores.id"))
    color: Mapped["Color"] = relationship("Color", back_populates="stocks")

    id_talle: Mapped[int] = mapped_column(Integer, ForeignKey("talles.id"))
    talle: Mapped["Talle"] = relationship("Talle", back_populates="stocks")

    id_sucursal: Mapped[int] = mapped_column(Integer, ForeignKey("sucursales.id"))
    sucursal: Mapped["Sucursal"] = relationship("Sucursal", back_populates="stocks")

    detalles_venta: Mapped[list["DetalleVenta"]] = relationship("DetalleVenta", back_populates="stock")
    detalles_compra: Mapped[list["DetalleCompra"]] = relationship("DetalleCompra", back_populates="stock")
    detalles_devolucion: Mapped[list["DetalleDevolucion"]] = relationship("DetalleDevolucion", back_populates="stock")

    def __repr__(self):
        producto_nombre = getattr(self.producto, 'nombre', None)
        color_nombre = getattr(self.color, 'nombre', None)
        talle_nombre = getattr(self.talle, 'nombre', None)
        sucursal_nombre = getattr(self.sucursal, 'nombre', None)
        return f"Stock {self.id!r} Cantidad: {self.cantidad!r} Producto: {producto_nombre!r} Color: {color_nombre!r} Talle: {talle_nombre!r} Sucursal: {sucursal_nombre!r}"
