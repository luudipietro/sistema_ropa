from sistema_ropa.app.extensions import Base
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy import Column, Integer, String, Float

class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True, index=True)
    total = Column(Float, nullable=False)
    metodo_pago = Column(String, nullable=False)

    product: Mapped["Product"] = relationship("Product", back_populates="purchases")

    def __repr__(self):
        return f"Purchase {self.id!r} Product ID: {self.product_id!r} Quantity: {self.quantity!r} Total Price: {self.total_price!r}"