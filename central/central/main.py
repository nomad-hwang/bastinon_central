from fastapi import FastAPI

from central.container import Container


def create_app() -> FastAPI:
    container = Container()
    container.init_resources()
    container.wire(modules=[__name__])

    db = container._database()

    app = FastAPI()
    # app.include_router(api_router, prefix="/api")
    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8080)
