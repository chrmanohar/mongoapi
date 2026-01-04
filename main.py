from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import os
from dotenv import load_dotenv
load_dotenv()
app = FastAPI()
MONGO_URI = os.getenv("MONGO_URL")
client = AsyncIOMotorClient(MONGO_URI)
db = client["testmd"]
table = db["testmd"]

class Studentdata(BaseModel):
    name: str
    age: int
    grade: str

@app.post("/add_student")
async def student_data_insert(stu: Studentdata):
    result = table.insert_one(stu.dict())
    return {"id": str(result), "message": "Student data inserted successfully"}
   