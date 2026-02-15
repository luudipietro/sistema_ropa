from sistema_ropa.app.extensions import Base
from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column


class Cambio(Base):
    __tablename__ = "cambios"

    id = Column(Integer, primary_key=True, index=True)
    monto = Column(Float, nullable=False)

    id_venta: Mapped[int] = mapped_column(Integer, ForeignKey("ventas.id"), nullable=False)
    venta: Mapped["Venta"] = relationship("Venta", back_populates="cambios")

    id_sucursal: Mapped[int] = mapped_column(Integer, ForeignKey("sucursales.id"), nullable=False)
    sucursal: Mapped["Sucursal"] = relationship("Sucursal", back_populates="cambios")

    detalles: Mapped[list["DetalleDevolucion"]] = relationship("DetalleDevolucion", back_populates="cambio")

    def __repr__(self):
        return f"Cambio {self.id!r} Monto: {self.monto!r}"
