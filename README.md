# fastapi-localcache
To implement a local cache with FastAPI, you can utilize a caching library like cachetools and integrate it into your FastAPI application. Here's an example of how you can implement a simple local cache using cachetools with FastAPI:

We then create a TTLCache object from cachetools, specifying the maximum size of the cache (maxsize) and the expiration time for each item (ttl).

Next, we define a route /data/{key} using the @app.get() decorator. The {key} is a path parameter that represents the key used to retrieve the data.

Installation 

# create virtual environment 
` python -m venv dev-cache`

` dev-cache/Scripts/activate` # for windows 
` dev-cache\bin\activate` # for linux

# Install dependency 

`python -m pip install -r requirements.txt`

# Run application 
`python app.py`

#Open any brower 
1. http://127.0.0.1:8000/data/1
2. First time it will store in cache 
3. another time it will read from cache
