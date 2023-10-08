from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def mensage():
    return "hello world!!"