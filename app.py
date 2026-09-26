from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import pandas as pd
import joblib

from src.feature_extraction import extract_features


# Create FastAPI application
app = FastAPI(
    title="Phishing URL Detector",
    description="Machine Learning based phishing URL detection system"
)


# Connect static files
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


# Connect HTML templates
templates = Jinja2Templates(
    directory="templates"
)


# Load trained model
model = joblib.load("model.pkl")

# Load feature names
feature_names = joblib.load("feature_names.pkl")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@app.get("/predict")
async def predict(url: str):

    # Extract features from URL
    features = extract_features(url)

    # Convert features into DataFrame
    feature_df = pd.DataFrame(
        [features],
        columns=feature_names
    )

    # Make prediction
    prediction = model.predict(feature_df)[0]

    # Get probability
    probabilities = model.predict_proba(feature_df)[0]

    phishing_probability = probabilities[1]

    # Convert prediction to readable result
    if prediction == 1:
        result = "PHISHING"
    else:
        result = "LEGITIMATE"

    return {
        "url": url,
        "prediction": result,
        "phishing_probability": round(
            phishing_probability * 100,
            2
        )
    }