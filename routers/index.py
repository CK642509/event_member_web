from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", tags=["index"])
async def index(request: Request) -> dict:
    # return {"message": "Hello World!"}
    return templates.TemplateResponse("index.html", {"request": request})