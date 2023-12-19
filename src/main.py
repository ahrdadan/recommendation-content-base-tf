from enum import Enum
from fastapi import FastAPI
from recommenders.content_base.predict_cb import get_lomba_recommendations
import time

class ModelName(str, Enum):
    cb = "cb"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()

@app.get("/")
def read_root():
    return {"Status": "Ok"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/models/{model_name}")
async def predict_model(
    model_name: ModelName, 
    id: int = None,
    num: int = 5,
    retrain: bool = False
):
    if model_name is ModelName.cb:
        if id:
            cb_result = get_lomba_recommendations(id, top_n=num)
            return {"model_name": model_name, "id": id, 'num': num, 'items': cb_result}
        else:
            return {"model_name": model_name, "message": "Ini adalah content base recommenders", 'status':"Oke"}
        # if retrain:

    
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
