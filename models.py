from database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, FLOAT
from sqlalchemy.orm import relationship

class data_Mahasiswa(Base):
    __tablename__="Mahasiswa"
    nim = Column(Integer,primary_key=True)
    nama = Column(String)
    ip1 = Column(FLOAT)
    ip2 = Column(FLOAT)
    ip3 = Column(FLOAT)
    ip4 = Column(FLOAT)
    sks = Column(Integer)
    predict_ontime = Column(Boolean)
