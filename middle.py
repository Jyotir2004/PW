from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response, JSONResponse
from fastapi import Request
import time

EXCLUDED_PATHS = {"/", "/about", "/greet", "/docs", "/openapi.json", "/redoc", "/docs/oauth2-redirect", "/wish", "/register","/view/{patient_id}"}
VALID_TOKEN = "Bearer my secret token"


class mymiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        print("before request")
        response = await call_next(request)
        print("after request")
        return response


class Authmiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.url.path in EXCLUDED_PATHS:
            return await call_next(request)
        token = request.headers.get("Authorization")
        if not token or token != VALID_TOKEN:
            return Response(status_code=401, content="Unauthorized: send Authorization: Bearer my secret token")
        response = await call_next(request)
        return response


class Timingmiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start = time.perf_counter()
        response = await call_next(request)
        end = time.perf_counter()
        process_time = end - start
        print("process time", process_time)
        return response


class ErrorHandlingmiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as e:
            print("Unhandled error:", e)
            return JSONResponse(status_code=500, content={"detail": str(e)})
