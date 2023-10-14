import random

import uvicorn
from fastapi import FastAPI

fastapp = FastAPI()


@fastapp.get("/")
def show_test():
    """Простая эмуляция внешнего сервера."""
    value = random.choice(["True", "False"])
    return {"answer": value}


if __name__ == "__main__":
    uvicorn.run(fastapp)
