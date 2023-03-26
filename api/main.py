from fastapi import FastAPI
from services.getData import get10, getPort, query

app = FastAPI()

@app.get("/")
async def root():
    return get10()




@app.get("/port/{portNumber}")
async def get_port(portNumber: int):
    return getPort(portNumber)


@app.get("/query/{querystr}")
async def get_query(querystr: str):
    return query(querystr)