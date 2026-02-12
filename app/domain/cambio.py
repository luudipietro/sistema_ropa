from sistema_ropa.app.extensions import Base
from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship, Mapped


class Return(Base):
    __tablename__ = "returns"

    id = Column(Integer, primary_key=True, index=True)
    monto = Column(Float, nullable=False)

    id_venta : Mapped[int] = Column(Integer, ForeignKey("sales.id"), nullable=False)
    sale : Mapped["Sale"] = relationship("Sale", back_populates="returns")
    id_sucursal : Mapped[int] = Column(Integer, ForeignKey("stores.id"), nullable=False)
    branch : Mapped["Store"] = relationship("Store", back_populates="returns")