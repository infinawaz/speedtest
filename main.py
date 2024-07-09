from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import speedtest


app = FastAPI()


@app.get("/")
def read_root():
    with open("index.html") as f:
        return HTMLResponse(f.read())


@app.get("/api/x")
def read():
    return {"Hello": "X"}

@app.get("/api/x/z")
def read():
    return {"Hello": "Z"}   


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)