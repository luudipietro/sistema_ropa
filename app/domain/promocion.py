from app.db.extensions import Base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship, Mapped

class Promocion(Base):
    __tablename__ = "promociones"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    precio_total = Column(Float, nullable=False)

    detalles: Mapped[list["DetallePromocion"]] = relationship("DetallePromocion", back_populates="promocion")

    def __repr__(self):
        return f"Promocion {self.id!r} {self.nombre!r} PrecioTotal: {self.precio_total!r}"
