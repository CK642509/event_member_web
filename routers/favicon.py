from fastapi import APIRouter
from starlette.responses import FileResponse

router = APIRouter()

@router.get('/favicon.ico')
async def favicon():
    return FileResponse("icons/john.ico")