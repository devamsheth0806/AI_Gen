from pydantic import BaseModel

class UserInput(BaseModel):
    requirements: str

class SelectedOption(BaseModel):
    selected_option: str

class Recommendation(BaseModel):
    label: str
    description: str
    monthly_cost: float

class RecommendationResponse(BaseModel):
    summary: str