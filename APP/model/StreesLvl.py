from APP.model.baseModel import *


def StresswithBMI():
    db = connect_to_mysql()
    if db:
        query = "SELECT `Physical Activity Level`, AVG(CASE WHEN `BMI Category` = 'Overweight' THEN `Stress Level` ELSE 0 END) AS 'Overweight', AVG(CASE WHEN `BMI Category` = 'Normal' THEN `Stress Level` ELSE 0 END) AS 'Normal', AVG(CASE WHEN `BMI Category` = 'Obese' THEN `Stress Level` ELSE 0 END) AS 'Obese', AVG(CASE WHEN `BMI Category` = 'Normal Weight' THEN `Stress Level` ELSE 0 END) AS 'Normal Weight' FROM `Sleep_health_and_lifestyle_dataset` GROUP BY `Physical Activity Level` ORDER BY `Physical Activity Level`;"

        results = getDatabyQuery(db, query)

        pprint(results)

        json_results = [
            {
                "Lable": row[0],
                "Overweight": row[1],
                "Normal": row[2],
                "Obese": row[3],
                "Normal Weight": row[4],
            }
            for row in results
        ]

        return json_results

    return {"message": "Gagal terhubung ke database MySQL"}
