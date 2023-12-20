from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Sepatu(Base):
    __tablename__ = 'data_sepatu'
    No: Mapped[str] = mapped_column(primary_key=True)
    Merk_Sepatu: Mapped[str] = mapped_column()
    Harga: Mapped[int] = mapped_column()
    Kualitas_Material: Mapped[int] = mapped_column()
    Desain: Mapped[int] = mapped_column()
    Kenyamanan: Mapped[int] = mapped_column()
    Durabilitas: Mapped[int] = mapped_column()  
    
    def __repr__(self) -> str:
        return f"Sepatu(No={self.No!r}, Harga={self.Harga!r})"
