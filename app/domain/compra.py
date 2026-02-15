from sistema_ropa.app.extensions import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import Column, Integer, Float, ForeignKey

class Compra(Base):
    __tablename__ = "compras"

    id = Column(Integer, primary_key=True, index=True)
    total = Column(Float, nullable=False)

    id_metodo_pago: Mapped[int] = mapped_column(Integer, ForeignKey("metodos_pago.id"))
    metodo_pago: Mapped["MetodoPago"] = relationship("MetodoPago", back_populates="compras")

    detalles: Mapped[list["DetalleCompra"]] = relationship("DetalleCompra", back_populates="compra")

    def __repr__(self):
        return f"Compra {self.id!r} Total: {self.total!r}"
