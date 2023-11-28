from APP.routers.baseRouter import *
from APP.model import StreesLvl

# from ..config.dependencies import *


router = APIRouter(
    prefix="/Stress",
    tags=["Stress"],
    responses={404: {"detail": "Not found"}},
    dependencies=[],
)


@router.get("/StresswithBMI")
async def StresswithBMI():
    return StreesLvl.StresswithBMI()
