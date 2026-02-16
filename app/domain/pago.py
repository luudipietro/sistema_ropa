from app.db.extensions import Base
from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

class Pago(Base):
    __tablename__ = "pagos"

    id = Column(Integer, primary_key=True, index=True)
    monto_sin_recargo = Column(Float, nullable=False)
    monto_con_recargo = Column(Float, nullable=False)

    id_venta: Mapped[int] = mapped_column(Integer, ForeignKey("ventas.id"), nullable=False)
    venta: Mapped["Venta"] = relationship("Venta", back_populates="pagos")

    id_metodo_pago: Mapped[int] = mapped_column(Integer, ForeignKey("metodos_pago.id"), nullable=False)
    metodo_pago: Mapped["MetodoPago"] = relationship("MetodoPago", back_populates="pagos")

    def __repr__(self):
        return f"Pago {self.id!r} Monto: {self.monto_con_recargo!r} Metodo: {self.id_metodo_pago!r}"
