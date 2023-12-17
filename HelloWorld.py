from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def helloWorld():
    content="""
    <html>
        <head>
            <title>Hello World!</title>
        </head>
        <body>
            <h1>Hello World!</h1>
            <a>This is a dummy microservice.\n
            That's all!</a>
        </body>
    </html>
    """
    return HTMLResponse(content=content)

if __name__ == "__main__":
    uvicorn.run("HelloWorld:app",
                host="127.0.0.1",
                port=8000,
                reload=True,
                log_level="debug")