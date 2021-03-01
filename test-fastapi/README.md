 # Test fast api
This repo is just to test ans work with fast api

## installation
You need first to install fast api lib
```
pip install fastapi
```
And uvicorn, which is a "is a lightning-fast ASGI server implementation"
```
pip install uvicorn[standard]
```
## start the application
To start the app you just need to execute =: 
```
uvicorn main:app --reload
```
You have some basics option, like, select the port, which is 
--port [port number]
```
uvicorn main:app --reload --port 2394
```
Will start the server on the port 2394 ^^


### more info
- For [Uvicorn](https://www.uvicorn.org/)
- For [Fast API](https://fastapi.tiangolo.com/)

