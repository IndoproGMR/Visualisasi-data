from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


from APP.routers import Occupation
from APP.routers import htmlview
from APP.routers import Index_Counts
from APP.routers import SleepQuality
from APP.routers import StreesLvl


app = FastAPI()

app.mount("/css", StaticFiles(directory="web/css"), name="css")
app.mount("/js", StaticFiles(directory="web/js"), name="js")
app.mount("/img", StaticFiles(directory="web/img"), name="img")

app.add_middleware(
    CORSMiddleware,
    allow_origins={"*"},
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route
app.include_router(Occupation.router)
app.include_router(htmlview.router)
app.include_router(Index_Counts.router)
app.include_router(SleepQuality.router)
app.include_router(StreesLvl.router)
