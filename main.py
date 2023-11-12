import uvicorn

from core.config import config

if __name__ == "__main__":
    uvicorn.run(
        app="core.server:app",
        host="0.0.0.0",  # optional: specify the host, default is '127.0.0.1
        port=8001,
        reload=True if config.ENVIRONMENT != "production" else False,
        workers=1,
    )
