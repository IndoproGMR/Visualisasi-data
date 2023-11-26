from APP.model.baseModel import *


def Count_Gender():
    db = connect_to_mysql()
    if db:
        query = "SELECT Gender,COUNT(*) as total FROM Sleep_health_and_lifestyle_dataset GROUP BY Gender;"

        results = getDatabyQuery(db, query)
        json_results = [{"X": row[0], "Y": row[1]} for row in results]

        return json_results
    return {"message": "Gagal terhubung ke database MySQL"}


def Count_Age():
    db = connect_to_mysql()
    if db:
        query = "SELECT Age,COUNT(*) as total FROM Sleep_health_and_lifestyle_dataset GROUP BY Age ORDER BY Age;"

        results = getDatabyQuery(db, query)
        json_results = [{"X": row[0], "Y": row[1]} for row in results]

        return json_results
    return {"message": "Gagal terhubung ke database MySQL"}


def Count_Occupation():
    db = connect_to_mysql()
    if db:
        query = "SELECT Occupation,COUNT(*) as total FROM Sleep_health_and_lifestyle_dataset GROUP BY Occupation ORDER BY total DESC;"

        results = getDatabyQuery(db, query)
        json_results = [{"X": row[0], "Y": row[1]} for row in results]

        return json_results
    return {"message": "Gagal terhubung ke database MySQL"}


def Count_SleepDuration():
    db = connect_to_mysql()
    if db:
        query = "SELECT `Sleep Duration`,COUNT(*) as total FROM Sleep_health_and_lifestyle_dataset GROUP BY `Sleep Duration` ORDER BY `Sleep Duration` DESC;"

        results = getDatabyQuery(db, query)
        json_results = [{"X": row[0], "Y": row[1]} for row in results]

        return json_results
    return {"message": "Gagal terhubung ke database MySQL"}


def Count_QualityofSleep():
    db = connect_to_mysql()
    if db:
        query = "SELECT `Quality of Sleep`,COUNT(*) as total FROM Sleep_health_and_lifestyle_dataset GROUP BY `Quality of Sleep` ORDER BY `Quality of Sleep` DESC;"

        results = getDatabyQuery(db, query)
        json_results = [{"X": row[0], "Y": row[1]} for row in results]

        return json_results
    return {"message": "Gagal terhubung ke database MySQL"}


def Count_PhysicalActivityLevel():
    db = connect_to_mysql()
    if db:
        query = "SELECT `Physical Activity Level`,COUNT(*) as total FROM Sleep_health_and_lifestyle_dataset GROUP BY `Physical Activity Level` ORDER BY `Physical Activity Level` DESC;"

        results = getDatabyQuery(db, query)
        json_results = [{"X": row[0], "Y": row[1]} for row in results]

        return json_results
    return {"message": "Gagal terhubung ke database MySQL"}


def Count_StressLevel():
    db = connect_to_mysql()
    if db:
        query = "SELECT `Stress Level`,COUNT(*) as total FROM Sleep_health_and_lifestyle_dataset GROUP BY `Stress Level` ORDER BY `Stress Level` DESC;"

        results = getDatabyQuery(db, query)
        json_results = [{"X": row[0], "Y": row[1]} for row in results]

        return json_results
    return {"message": "Gagal terhubung ke database MySQL"}


def Count_BMICategory():
    db = connect_to_mysql()
    if db:
        query = "SELECT `BMI Category`,COUNT(*) as total FROM Sleep_health_and_lifestyle_dataset GROUP BY `BMI Category` ORDER BY `BMI Category` DESC;"

        results = getDatabyQuery(db, query)
        json_results = [{"X": row[0], "Y": row[1]} for row in results]

        return json_results
    return {"message": "Gagal terhubung ke database MySQL"}


def Count_BloodPressure():
    db = connect_to_mysql()
    if db:
        query = "SELECT `Blood Pressure`,COUNT(*) as total FROM Sleep_health_and_lifestyle_dataset GROUP BY `Blood Pressure` ORDER BY `Blood Pressure` DESC;"

        results = getDatabyQuery(db, query)
        json_results = [{"X": row[0], "Y": row[1]} for row in results]

        return json_results
    return {"message": "Gagal terhubung ke database MySQL"}


def Count_HeartRate():
    db = connect_to_mysql()
    if db:
        query = "SELECT `Heart Rate`,COUNT(*) as total FROM Sleep_health_and_lifestyle_dataset GROUP BY `Heart Rate` ORDER BY `Heart Rate` DESC;"

        results = getDatabyQuery(db, query)
        json_results = [{"X": row[0], "Y": row[1]} for row in results]

        return json_results
    return {"message": "Gagal terhubung ke database MySQL"}


def Count_DailySteps():
    db = connect_to_mysql()
    if db:
        query = "SELECT `Daily Steps`,COUNT(*) as total FROM Sleep_health_and_lifestyle_dataset GROUP BY `Daily Steps` ORDER BY `Daily Steps` DESC;"

        results = getDatabyQuery(db, query)
        json_results = [{"X": row[0], "Y": row[1]} for row in results]

        return json_results
    return {"message": "Gagal terhubung ke database MySQL"}


def Count_SleepDisorder():
    db = connect_to_mysql()
    if db:
        query = "SELECT `Sleep Disorder`,COUNT(*) as total FROM Sleep_health_and_lifestyle_dataset GROUP BY `Sleep Disorder` ORDER BY `Sleep Disorder` DESC;"

        results = getDatabyQuery(db, query)
        json_results = [{"X": row[0], "Y": row[1]} for row in results]

        return json_results
    return {"message": "Gagal terhubung ke database MySQL"}
