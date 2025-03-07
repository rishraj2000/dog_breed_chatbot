import os
import pandas as pd
from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain_experimental.agents.agent_toolkits import create_csv_agent

# Load CSV file
csv_file_path = 'cleaned_dog_breeds.csv'
df_csv = pd.read_csv(csv_file_path)

# Set your Groq API key here
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
my_model = os.getenv("model", "")

llm = ChatGroq(
    temperature=0,
    model=my_model,
    api_key=GROQ_API_KEY,  # Pass API key explicitly
    max_tokens=8000
)

# Create CSV Agent
agent = create_csv_agent(
    llm,
    csv_file_path,
    verbose=True,
    allow_dangerous_code=True,
    max_iterations=100,
    handle_parsing_errors=True
)

# Initialize FastAPI
app = FastAPI()

# Request Model
class QueryRequest(BaseModel):
    user_id: str
    query: str

# Response Model
class QueryResponse(BaseModel):
    answer: str

@app.post("/query", response_model=QueryResponse)
async def query_data(request: QueryRequest):
    response = agent.invoke(request.query)
    answer_str = response.get("output", str(response))
    return {"answer": answer_str}
