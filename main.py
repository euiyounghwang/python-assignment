
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from controller import (rest_api_router)
import datetime
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


''' http://localhost:7777/docs '''

@app.get("/v1", tags=['API'],  
         status_code=200,
         description="Default GET API", 
         summary="Default GET API")
async def root():
    print('root')
    return {"message": "Hello World"}


# router
app.include_router(rest_api_router.app, tags=["assignment"], )