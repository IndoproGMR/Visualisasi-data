from APP.model.baseModel import *


def CountOccupation():
    db = connect_to_mysql()
    if db:
        query = "SELECT `Occupation`,COUNT(*) as total FROM `Sleep_health_and_lifestyle_dataset` GROUP BY `Occupation` ORDER BY total DESC;"

        results = getDatabyQuery(db, query)

        json_results = [{"X": row[0], "Y": row[1]} for row in results]

        return json_results

    return {"message": "Gagal terhubung ke database MySQL"}


def OccupationWithSleepDisorder():
    db = connect_to_mysql()
    if db:
        query = "SELECT `Occupation`, AVG(CASE WHEN `Sleep Disorder` = 'Insomnia' THEN 1 ELSE 0 END) AS 'Insomnia', AVG(CASE WHEN `Sleep Disorder` = 'None' THEN 1 ELSE 0 END) AS 'None', AVG(CASE WHEN `Sleep Disorder` = 'Sleep Apnea' THEN 1 ELSE 0 END) AS 'Sleep Apnea' FROM `Sleep_health_and_lifestyle_dataset` GROUP BY Occupation ORDER BY `Occupation`;"

        results = getDatabyQuery(db, query)

        json_results = [
            {"Lable": row[0], "Insomnia": row[1], "None": row[2], "SleepApnea": row[3]}
            for row in results
        ]

        return json_results

    return {"message": "Gagal terhubung ke database MySQL"}


def OccupationWithPhysicalActivityLevel():
    db = connect_to_mysql()
    if db:
        query = "SELECT `Occupation`,AVG(`Physical Activity Level`) as `Physical Activity Level` FROM `Sleep_health_and_lifestyle_dataset` GROUP BY `Occupation` ORDER BY `Physical Activity Level` Desc"

        results = getDatabyQuery(db, query)

        json_results = [{"X": row[0], "Y": row[1]} for row in results]

        return json_results

    return {"message": "Gagal terhubung ke database MySQL"}
