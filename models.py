from database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class data_Mahasiswa(Base):
    __tablename__="Mahasiswa"
    nim = Column(Integer,primary_key=True)
    nama = Column(String)
    ip1 = Column(float)
    ip2 = Column(float)
    ip3 = Column(float)
    ip4 = Column(float)
    sks = Column(Integer)
    predict_ontime = Column(Boolean)
