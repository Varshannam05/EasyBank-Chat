from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS Middleware to allow frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all for testing, replace with specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define input and output models
class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    response: str

# Updated responses
responses: Dict[str, str] = {
    "How can I open a new savings account?": "To open a new savings account, you can visit our nearest branch with valid ID proof, address proof, and a passport-sized photo. Alternatively, you can apply online through our website or mobile app.",
    "How can I check my account balance?": "You can check your account balance via internet banking, our mobile app, or by visiting the nearest ATM. Alternatively, you can send an SMS to our banking number or contact customer support.",
    "What documents are required to apply for a personal loan?": "You'll need ID proof, address proof, income proof (salary slips or IT returns), and bank statements for the last 6 months.",
    "How can I increase my credit card limit?": "To increase your credit card limit, you can submit an online request via internet banking, call customer care, or visit your nearest branch. Ensure you have a good credit history for approval.",
    "How do I register for online banking?": "You can register for online banking by visiting our website and clicking on the 'Register' option. Enter your account details, set a password, and follow the instructions to activate your account.",
    "What should I do if I forget my internet banking password?": "If you forget your password, click on the 'Forgot Password' option on the login page. Follow the steps to reset it using your registered mobile number or email."
}

@app.post("/agent-assist/", response_model=QueryResponse)
async def agent_assist(request: QueryRequest):
    """
    Endpoint to provide chatbot assistance.
    """
    query = request.query
    response = responses.get(query, "I'm sorry, I currently don't have a response for that query.")
    return {"response": response}

@app.get("/")
async def root():
    """
    Root endpoint to verify the server is running.
    """
    return {"message": "Agent Assistance System is running!"}
