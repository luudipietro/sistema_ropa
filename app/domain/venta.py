from sistema_ropa.app.extensions import Base
from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    subtotal = Column(Float, nullable=False)
    descuento = Column(Float, nullable=False)
    total = Column(Float, nullable=False)

    id_store : Mapped[int] = mapped_column(Integer, ForeignKey("stores.id"))
    store : Mapped["Store"] = relationship("Store", back_populates="sales")