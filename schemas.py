from typing import List
from pydantic import BaseModel

class data_Mahasiswa(BaseModel):
    #__tablename__="Mahasiswa"
    nim = int
    nama = str
    ip1 = float
    ip2 = float
    ip3 = float
    ip4 = float
    sks = int
    predict_ontime = bool