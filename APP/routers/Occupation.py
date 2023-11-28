from APP.routers.baseRouter import *
from APP.model import Occupation


router = APIRouter(
    prefix="/Occupation",
    tags=["Occupation"],
    responses={404: {"detail": "Not found"}},
    dependencies=[],
)


@router.get("/OccupationWithSleepDisorder")
async def OccupationWithSleepDisorder():
    return Occupation.OccupationWithSleepDisorder()


@router.get("/OccupationWithPhysicalActivityLevel")
async def OccupationWithPhysicalActivityLevel():
    return Occupation.OccupationWithPhysicalActivityLevel()
