class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    total = Column(Float, nullable=False)

    def __repr__(self):
        return f"Promocion {self.id!r} Descripcion: {self.descripcion!r} Descuento: {self.descuento_porcentaje!r}%"