from fastapi import FastAPI
from starlette.exceptions import HTTPException
from fastapi.exceptions import RequestValidationError
from App.src.utils.response import Response


def register_custom_handlers(app: FastAPI):
    app.add_exception_handler(HTTPException, lambda r, e: Response.e(e.detail or "Error occurred", e.status_code))
    app.add_exception_handler(RequestValidationError, lambda r, e: Response.e("Validation Error", 422, e.errors()))
    app.add_exception_handler(Exception, lambda r, e: Response.e("Internal Server Error", 500))