from fastapi import FastAPI
import cdd_python

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    cdd_python.init()
    print("cdd-python initialized")


@app.get("/")
def read_root():
    return {"message": "Hello, World!!"}


@app.get("/audit")
def audit():
    cdd_python.run()
    return {"message": "Audit triggered, check console for results"}
