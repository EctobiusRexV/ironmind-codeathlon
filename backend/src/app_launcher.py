import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .item_route import router as item_router
from .health_route import router as health_router
from .program_route import router as program_router
from .sexe_route import router as sexe_router
from .events import eventsRouter


def launch():
    print("Launching app...")
    app = __setup_app()
    uvicorn.run(app, host="0.0.0.0", port=8080)

def __setup_app() -> FastAPI:
    app = FastAPI(root_path="/api") # API is accessed via /api on the frontend container

    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(item_router)
    app.include_router(health_router)
    app.include_router(program_router)
    app.include_router(sexe_router)
    app.include_router(eventsRouter)

    return app