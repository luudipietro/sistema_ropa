from app.db.extensions import Base
from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

class Venta(Base):
    __tablename__ = "ventas"

    id = Column(Integer, primary_key=True, index=True)
    subtotal = Column(Float, nullable=False)
    descuento = Column(Float, nullable=False)
    total = Column(Float, nullable=False)

    id_sucursal: Mapped[int] = mapped_column(Integer, ForeignKey("sucursales.id"))
    sucursal: Mapped["Sucursal"] = relationship("Sucursal", back_populates="ventas")

    detalles: Mapped[list["DetalleVenta"]] = relationship("DetalleVenta", back_populates="venta")
    pagos: Mapped[list["Pago"]] = relationship("Pago", back_populates="venta")
    cambios: Mapped[list["Cambio"]] = relationship("Cambio", back_populates="venta")

    def __repr__(self):
        return f"Venta {self.id!r} Total: {self.total!r}"
