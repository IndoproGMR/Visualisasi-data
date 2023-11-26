from APP.routers.baseRouter import *
from APP.model import index_count


router = APIRouter(
    prefix="/Count",
    tags=["Count"],
    responses={404: {"detail": "Not found"}},
    dependencies=[],
)


@router.get("/Gender")
async def Gender():
    return index_count.Count_Gender()


@router.get("/Age")
async def Age():
    return index_count.Count_Age()


@router.get("/Occupation")
async def Occupation():
    return index_count.Count_Occupation()


@router.get("/SleepDuration")
async def SleepDuration():
    return index_count.Count_SleepDuration()


@router.get("/QualityofSleep")
async def QualityofSleep():
    return index_count.Count_QualityofSleep()


@router.get("/PhysicalActivityLevel")
async def PhysicalActivityLevel():
    return index_count.Count_PhysicalActivityLevel()


@router.get("/StressLevel")
async def StressLevel():
    return index_count.Count_StressLevel()


@router.get("/BMICategory")
async def BMICategory():
    return index_count.Count_BMICategory()


@router.get("/BloodPressure")
async def BloodPressure():
    return index_count.Count_BloodPressure()


@router.get("/HeartRate")
async def HeartRate():
    return index_count.Count_HeartRate()


@router.get("/DailySteps")
async def DailySteps():
    return index_count.Count_DailySteps()


@router.get("/SleepDisorder")
async def SleepDisorder():
    return index_count.Count_SleepDisorder()
