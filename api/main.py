from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models.api_models import UserInput, SelectedOption
from api.pipeline import deployment_recommendation_request, process_deployment_request

app = FastAPI()

# Optional: Allow Streamlit frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend domain for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze_deployment(input_data: UserInput):
    try:
        results = await deployment_recommendation_request(input_data.requirements)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post('/deploy')
async def deploy_selection(selected_option: SelectedOption):
    try:
        return await process_deployment_request(selected_option= selected_option.option.upper())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))