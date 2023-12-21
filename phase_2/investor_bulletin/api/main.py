from uvicorn import run
from fastapi import FastAPI
from dotenv import load_dotenv
from api.routes import init_routes

app = init_routes(FastAPI(
    title="Investor Bulletin API",
    description="API for Investor Bulletin",
    version="0.1.0",
    contact={
        "name": "Mohammed Balhaddad",
        "email": "mb@mbalhaddad.com",
    },
    license_info={
        "name": "MIT License",
    }
))

load_dotenv()

if __name__ == "__main__":
    run("api.main:app")
