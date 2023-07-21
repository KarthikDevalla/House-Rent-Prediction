from fastapi import FastAPI, Request
import pickle
import warnings
warnings.filterwarnings('ignore')
import numpy as np
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")
model=pickle.load(open('model_weights.pkl','rb'))
scalar=pickle.load(open('scalar.pkl','rb'))

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("webpage.html", {"request": request})


@app.post('/predict')
async def predict(request:Request):
    data= await request.json()
    data = data["data"]
    area_value_transformed = scalar.transform([[float(data["area"])]])
    q = np.array([int(data["bedroom"]), data["layout_type"], data["property_type"],area_value_transformed[0], data["furnish_type"], int(data["bathroom"]), data["city"]])
    q = q.reshape(1, 7)
    output = model.predict(q)[0]
    return round(output,2)
