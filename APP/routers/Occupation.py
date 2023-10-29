from APP.routers.baseRouter import *
from APP.model import Occupation


router = APIRouter(
    prefix="/Occupation",
    tags=["Occupation"],
    responses={404: {"detail": "Not found"}},
    dependencies=[],
)


@router.get("/Count")
async def count():
    return Occupation.CountOccupation()
