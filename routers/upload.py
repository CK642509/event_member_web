from http.client import HTTPException
from urllib import response
from fastapi import APIRouter, Request, UploadFile, HTTPException, Response
from fastapi.responses import FileResponse, JSONResponse

router = APIRouter()

@router.post(
    "/upload",
    tags=["test"],
    summary="This is summary",
    description="The descriptions")
async def upload(request: Request, file: UploadFile):
    try:
        _form = await request.form()
        title = _form["title"]
        file_buffer = await file.read()
        print(title)

        header = {"status": "OK"}

        # path = "path"
        # return FileResponse(path, headers=header)

        content = {
            "title": title
        }


        return JSONResponse(content=content, headers=header)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))