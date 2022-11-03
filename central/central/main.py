from fastapi import FastAPI

from central.adopter.api import api_router
from central.container import Container


def create_app() -> FastAPI:
    container = Container()
    container.init_resources()
    container.wire(packages=["central"])

    if container.config()["env"]["env"] == "development":
        from central.development import dev_setup

        dev_setup(container)

    app = FastAPI()
    app.include_router(api_router)

    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8080)
