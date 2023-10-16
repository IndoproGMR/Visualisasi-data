from typing import Union
from fastapi import FastAPI
from model.conn import connect_to_mysql, close_mysql_connection
from pprint import pprint
from fastapi.middleware.cors import CORSMiddleware


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
    db = connect_to_mysql()

    if db:

        # pprint(db)
        cursor = db.cursor()

        query = "SELECT `Occupation`,COUNT(*) as total FROM `Sleep_health_and_lifestyle_dataset` GROUP BY `Occupation`;"

        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        close_mysql_connection(db)

        json_results = [{"X": row[0], "Y": row[1]}
                        for row in results]

        return json_results

    return {"message": "Gagal terhubung ke database MySQL"}


@app.get("/test/conn")
def test_conn():
    db = connect_to_mysql()

    if db:

        return {"message": "Terhubung ke database MySQL"}
    return {"message": "Gagal terhubung ke database MySQL"}
