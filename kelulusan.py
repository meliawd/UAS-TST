from pydantic import BaseModel, Field

#Class dari data mahasiswa
class mahasiswa(BaseModel):
    ip1: float 
    ip2: float 
    ip3: float 
    ip4: float
    sks: int

class UserSchema(BaseModel):
    nim: int = Field(...)
    username: str = Field(...)
    password: str = Field(...)
    class Config:
        schema_extra = {
            "example": {
                "nim": "10000000",
                "username": "zzzz",
                "password": "apaya"
            }
        }

class UserLoginSchema(BaseModel):
    username: str = Field(...)
    password: str = Field(...)
    class Config:
        schema_extra = {
            "example": {
                "username": "zzzz",
                "password": "apaya"
            }
        }