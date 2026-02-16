from app.db.extensions import Base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship, Mapped

class MetodoPago(Base):
    __tablename__ = "metodos_pago"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    recargo = Column(Float, nullable=False)

    pagos: Mapped[list["Pago"]] = relationship("Pago", back_populates="metodo_pago")
    compras: Mapped[list["Compra"]] = relationship("Compra", back_populates="metodo_pago")

    def __repr__(self):
        return f"MetodoPago {self.id!r} {self.nombre!r}"