from fastapi import FastAPI
from api.routes import users, llm


app = FastAPI()


app.include_router(users.router)
app.include_router(llm.router)