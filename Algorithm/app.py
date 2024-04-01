from Algorithm.passwordGenerator.password_generator import PasswordGenerator
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class PasswordInput(BaseModel):
    base_password: str = "password"
    num_levels: int = 3
    size_of_level: int = 12
    percentage_of_candidates: float = 0.5

@app.post("/generate-password/")
async def generate_password(input_data: PasswordInput):
    base_password = input_data.base_password
    num_levels = input_data.num_levels
    size_of_level = input_data.size_of_level
    percentage_of_candidates = input_data.percentage_of_candidates

    generator = PasswordGenerator(base_password, num_levels, size_of_level, percentage_of_candidates)

    try:
        password_set = generator.execute_algorithm()
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while generating password: " + str(e))


    return {"password_set": password_set}


@app.options("/generate-password/")
async def options_generate_password():
    return {"allow": "POST"}