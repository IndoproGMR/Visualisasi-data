import json
from typing import Union
from pprint import pprint

from model.conn import connect_to_mysql,getDatabyQuery


def CountOccupation():

    db = connect_to_mysql()
    if db:
        query = "SELECT `Occupation`,COUNT(*) as total FROM `Sleep_health_and_lifestyle_dataset` GROUP BY `Occupation`;"

        results = getDatabyQuery(db,query)

        json_results = [{"X": row[0], "Y": row[1]}
                        for row in results]

        return json_results
    
    return {"message": "Gagal terhubung ke database MySQL"}