from APP.model.baseModel import *


def QualityWithDuration():
    db = connect_to_mysql()
    if db:
        query = "SELECT `Sleep Duration`,`Quality of Sleep` FROM `Sleep_health_and_lifestyle_dataset` ORDER BY `Sleep Duration` ASC;"

        results = getDatabyQuery(db, query)

        json_results = [{"X": row[0], "Y": row[1]} for row in results]

        return json_results

    return {"message": "Gagal terhubung ke database MySQL"}
