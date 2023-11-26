from APP.routers.baseRouter import *

# from APP.model import Occupation


router = APIRouter(
    # prefix="/",
    tags=["html"],
    responses={404: {"detail": "Not found"}},
    dependencies=[],
)


@router.get("/", response_class=HTMLResponse)
async def root(request: Request):
    data = [{"test": "isi data"}]
    # return view(request, "view/test.html", data)
    return view(request, "view/index.html", data)


@router.get("/Occupation", response_class=HTMLResponse)
async def Pekerjaan(request: Request):
    return view(request, "view/Pekerjaan.html")
