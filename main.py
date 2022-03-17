from fastapi import FastAPI, Depends
import pandas as pd
import uvicorn
from model import Feature_type, model
import numpy as np

app = FastAPI(title="API1", description="with FastAPI by Daniele Grotti", version="1.0")
# model = None
# @api1.on_event("startup")
# def load_model():
#     global model


@app.get("/", status_code=200)
def home():
    return {" ---->          http://localhost:8000/docs     <----------"}


@app.get("/predict", status_code=200)
async def predict_get(data: Feature_type= Depends()):              # depends() input nelle celle
    try:
        data = pd.DataFrame(data)
        data = data.T
        data.rename(columns=data.iloc[0], inplace = True)
        data= data.iloc[1:]
        
        y_pred = model.predict(data)[0]
        return {y_pred[0]}
    except:
        return {"prediction": "error"}

# @app.post("/predict", status_code=200)
# async def predict_post(data: Feature_type= Depends()):              # depends() input nelle celle
#     try:
#         data = pd.DataFrame(data)
#         data = data.T
#         data.rename(columns=data.iloc[0], inplace = True)
#         data= data.iloc[1:].values #must have array
        
#         y_pred = model.predict(data)[0]
#         return {"prediction":y_pred}
#     except:
#         return {"prediction": "error"}    

# @app.put("/predict", status_code=200)
# async def predict_put(data: Feature_type= Depends()):              # depends() input nelle celle
#     try:
#         data = pd.DataFrame(data)
#         data = data.T
#         data.rename(columns=data.iloc[0], inplace = True)
#         data= data.iloc[1:].values #must have array
        
#         y_pred = model.predict(data)[0]
#         return {"prediction":y_pred}
#     except:
#         return {"prediction": "error"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

