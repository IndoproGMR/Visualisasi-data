from fastapi import FastAPI
from model.conn import connect_to_mysql, close_mysql_connection
from pprint import pprint
from fastapi.middleware.cors import CORSMiddleware

from model.Occupation import *


app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/Occupation")
def Occupation():
    return CountOccupation()



@app.get("/test/conn")
def test_conn():
    db = connect_to_mysql()

    if db:

        return {"message": "Terhubung ke database MySQL"}
