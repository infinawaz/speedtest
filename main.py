from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import speedtest

app = FastAPI()

app.mount("/", StaticFiles(directory="static", html=True), name="static")

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
