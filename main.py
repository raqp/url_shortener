import secrets
import uvicorn
from fastapi import FastAPI, Response, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from models import URL
from src.database.db import Database
from src.middleware import ValidatorMiddleware

app = FastAPI()
database = Database()

app.add_middleware(ValidatorMiddleware,
                   include_endpoints={'/short', 'delete', '/long/{url:path}'})


@app.post('/short')
async def create_short_url(url: URL):
    if not database.get_short_url(url=url.url):
        short_url = f'http://short.com/{secrets.token_urlsafe(8)}'
        database.insert(long_url=url.url, short_url=short_url)
        data = {'short_url': short_url}
        return JSONResponse(content=jsonable_encoder(data), status_code=200)
    else:
        return Response(content="URL already exists", status_code=400)


@app.delete('/delete', status_code=status.HTTP_204_NO_CONTENT)
async def delete(url: URL):
    database.delete(url=url.url)


@app.get('/long/{url:path}')
async def get(url: str):
    result = database.get_long_url(url=url)
    data = {'original_url': result}
    return JSONResponse(content=jsonable_encoder(data), status_code=200)

