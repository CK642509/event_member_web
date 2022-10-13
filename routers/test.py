from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get(
    "/",
    tags=["test"],
    summary="This is summary",
    description="The descriptions")
async def get_test(request: Request) -> dict:
    # return {"message": "Hello World! test"}
    return templates.TemplateResponse("test.html", {"request": request})