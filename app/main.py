from fastapi import FastAPI
import uvicorn
from routers.csv_handler import router as csv_router
from routers.rooms_ruoter import router as rooms_router
from routers.soldiers_router import router as soldier_router



app = FastAPI()
app.include_router(csv_router)
app.include_router(rooms_router)
app.include_router(soldier_router)



if __name__ == "__main__":
    uvicorn.run(app)
