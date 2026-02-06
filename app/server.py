from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "OK"}

@app.post("/process")
def process(data: dict):
    if "value" not in data:
        raise HTTPException(status_code = 400, detail = "Missing 'value' field")
    return {"received": data["value"]}

@app.get("/error")
def error():
    raise Exception("Internal Server Error")
