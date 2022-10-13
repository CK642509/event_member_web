import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from config import Settings
from routers.routers import add_routers

app = FastAPI()
app_config = Settings()

# add routers
add_routers(app)

# mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")


if __name__ == "__main__":
    uvicorn.run(app, host=app_config.host,
                port=app_config.port, log_level="info")