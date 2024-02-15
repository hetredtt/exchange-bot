from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import ExchangeModule.controller as ExchangeModule

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ExchangeModule.router, tags=["Exchange Module"])