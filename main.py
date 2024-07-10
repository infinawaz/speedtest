from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import speedtest


app = FastAPI()


@app.get("/")
def read_root():
    with open("index.html") as f:
        return HTMLResponse(f.read())
    
@app.get("/speedtest")
def run_speedtest():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download()
    upload_speed = st.upload()
    ping = st.results.ping
    return {
        "download_speed": download_speed,
        "upload_speed": upload_speed,
        "ping": ping
    }


@app.get("/api/x")
def read():
    return {"Hello": "X"}

@app.get("/api/x/z")
def read():
    return {"Hello": "Z"}   


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)