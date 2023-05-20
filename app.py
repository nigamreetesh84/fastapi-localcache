from fastapi import FastAPI, Depends, HTTPException
from typing import List
from datetime import datetime
from cachetools import TTLCache

cache = TTLCache(maxsize=100, ttl=60)


app = FastAPI(
    title="Client Details API",
    version="1.0.0",
    description="API for cache",
)



@app.get("/data/{key}")
def get_data(key: str):
    # Check if the data is already present in the cache
    if key in cache:
        print("Getting from cache")
        return {"data": cache[key]}

    # If the data is not in the cache, retrieve it from the data source
    # For example, fetch the data from a database or an external API
    # Here, we simulate fetching the data by concatenating the key with "data"
    data = key + " data"

    # Store the data in the cache
    print("Storing in cache")
    cache[key] = data

    return {"data": data}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
