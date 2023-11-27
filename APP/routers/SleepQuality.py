from APP.routers.baseRouter import *
from APP.model import SleepQuality

# from ..config.dependencies import *


router = APIRouter(
    prefix="/SleepQuality",
    tags=["SleepQuality"],
    responses={404: {"detail": "Not found"}},
    dependencies=[],
)


@router.get("/QualityWithDuration")
async def QualityWithDuration():
    return SleepQuality.QualityWithDuration()
