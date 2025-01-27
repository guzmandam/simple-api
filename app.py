from fastapi import FastAPI
from typing import Dict, Any

app = FastAPI()

@app.post("/api/data/")
def receive_data(watch_data: Dict[Any, Any]):
	return {"ok": watch_data}
