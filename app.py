from fastapi import FastAPI
from typing import Dict, Any

app = FastAPI()

@app.post("/api/data/")
def receive_data(watch_data: Dict[Any, Any]):
    print("###### Received data ######")
    print(watch_data)
    print("###########################")
    
    return {
        "ok": watch_data
    }
