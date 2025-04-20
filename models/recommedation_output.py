from pydantic import BaseModel

class Option(BaseModel):
    description: str
    monthly_cost: float

class RecommendationOutput(BaseModel):
    A: Option
    B: Option
    C: Option