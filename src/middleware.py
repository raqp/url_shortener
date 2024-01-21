import validators
from validators.utils import ValidationError
from fastapi import Request, Response

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp


class ValidatorMiddleware(BaseHTTPMiddleware):
    def __init__(self, include_endpoints: set,  app: ASGIApp):
        super().__init__(app)
        self.include_endpoints = include_endpoints or set()

    async def dispatch(self, request: Request, call_next):
        if request.url.path in self.include_endpoints:
            if request.method == "GET":
                url = request.get('path')[6:] if request.get('path') else None
            else:
                body = await request.json()
                url = body.get('url')
            if isinstance(validators.url(url), ValidationError):
                return Response(content="Invalid URL", status_code=400)
        response = await call_next(request)
        return response
