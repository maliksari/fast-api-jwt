import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.api:app",host = "0.0.0.0",port =8081,reload = True)