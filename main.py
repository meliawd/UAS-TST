from fastapi import FastAPI, Body, Depends
from pydantic import BaseModel, Field
from auth import AuthHandler
from kelulusan import mahasiswa, UserSchema, UserLoginSchema
from auth_bearer import JWTBearer
from auth_handler import signJWT
from sqlalchemy import orm
from sqlalchemy.orm import Session
from database import engine, get_db
from schemas import data_Mahasiswa

import pickle
import pandas as pd
import numpy as np
import json
import uvicorn
import models,database
import schemas

pickle_in = open("mahasiswa.pkl","rb")
model_ml = pickle.load(pickle_in)
pengguna = []
app = FastAPI()
models.Base.metadata.create_all(engine)

@app.get("/welcome")
# menampilkan pesan selamat datang
def welcome():
        return {"message": "Selamat datang di service prediksi ketepatan waktu kelulusan kuliah"}

def check_user(data: UserLoginSchema): #fungsi pembantu
    for user in pengguna:
        if user.username == data.username and user.password == data.password:
            return True
    return False

@app.post("/user/signup", tags=["user"])
async def create_user(user: UserSchema = Body(...)):
    pengguna.append(user) # replace with db call, making sure to hash the password first
    return signJWT(user.username)

@app.post("/login", tags=["user"])
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.username)
    return {
        "error": "Masukkan kembali username dan password Anda"
    }

@app.post("/add", tags=["Data"], dependencies=[Depends(JWTBearer())])
# menambahkan data API baru ke database
async def add_mahasiswa(new_mahasiswa:data_Mahasiswa,db:Session=Depends(get_db)):
        new_mahasiswa = models.data_Mahasiswa(**new_mahasiswa.dict())
        db.add(new_mahasiswa)
        db.commit()
        db.refresh(new_mahasiswa)
        return new_mahasiswa
    
@app.get("/show", tags=["Data"], dependencies=[Depends(JWTBearer())])
async def retrieve_all_mahasiswa(db:Session= Depends(get_db)):
    db_mahasiswa = db.query(models.data_Mahasiswa).all()
    if db_mahasiswa == []:
        raise HTTPException(status_code=404, detail="Tidak ada data mahasiswa dalam database")
    return db_mahasiswa

@app.post('/predict', tags=["Prediction"], dependencies=[Depends(JWTBearer())])
async def predict_kelulusan(data:mahasiswa):
    data = data.dict()
    ip1 = data['ip1']
    ip2 = data['ip2']
    ip3 = data['ip3']
    ip4 = data['ip4']
    sks = data['sks']
    prediksi = model_ml.predict([[ip1, ip2, ip3, ip4, sks]])
    return {"prediksi" : prediksi[0]}

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)