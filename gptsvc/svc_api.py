from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def get_hello():
    """_summary_

    Returns:
        _type_: _description_
    """
    print("request hello received")
    return {"message": "Hello World!!!"}