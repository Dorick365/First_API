
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


@app.get("/bonnuit")
def hello():
    return {"message": "Bonnuit monsieur, I am your API"}


class Customer(BaseModel):
    annual_income: float = Field(gt=0)
    loan_amount: float = Field(ge=0)
    existing_monthly_emi: float = Field(ge=0)

class Workout(BaseException):
    dist_km: float
    dist_min: float

@app.post("/risk-score")
def risk_score(customer: Customer):
    monthly_income = customer.annual_income / 12

    loan_to_income = (
        customer.loan_amount / customer.annual_income
    )

    emi_to_income = (
        customer.existing_monthly_emi / monthly_income
    )

    if loan_to_income > 0.5 or emi_to_income > 0.4:
        assessment = "Review required"
    else:
        assessment = "Within basic screening limits"

    return {
        "loan_to_income_ratio": round(loan_to_income, 2),
        "existing_emi_to_monthly_income_ratio": round(
            emi_to_income, 2
        ),
        "assessment": assessment,
    }

@app.get("/workout")
def calc_pace(workout: Workout):
    pace = workout.dist_min/workout.dist_km

    return
    {
        "Distance" : workout.dist_km,
        "Minutes" :  workout.dist_min,
        "Pace" : pace
    }
