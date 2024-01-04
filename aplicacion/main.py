from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pymongo import MongoClient

app = FastAPI()

client = MongoClient('mongodb://mongo:27017/')
db = client['local']

@app.get("/")
def read_root():
    return {"message": "Desafío 8. DevOps Engineer"}


@app.get("/get_data/{item_id}")
def read_item(item_id: int):
    data = db.mi_coleccion.find_one({"_id": item_id})
    if data:
        return data
    else:
        raise HTTPException(status_code=404, detail="Item not found")


@app.post("/add_data/{item_id}")
def create_item(item_id: int, payload: dict):
    result = db.mi_coleccion.update_one({"_id": item_id}, {"$set": payload}, upsert=True)
    return {"status": "success", "modified_count": result.modified_count}
