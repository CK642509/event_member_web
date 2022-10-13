from routers.index import router as index_router
from routers.test import router as test_router
from routers.favicon import router as favicon_router
from routers.upload import router as upload_router

def add_routers(app):
    app.include_router(index_router, tags=["index"])
    app.include_router(test_router, prefix="/test", tags=["test", "example"])
    app.include_router(favicon_router)
    app.include_router(upload_router)
    return app