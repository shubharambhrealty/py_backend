import builtins
from fastapi import FastAPI
from App.src.utils.response import Response
from App.py_custom.mathod import register_custom_handlers

# Response ko globally register karna (bina kisi file me import kiye direct use karne ke liye)
builtins.Response = Response  # type: ignore[attr-defined]

# Routers ko Response register hone ke baad import karein
from routes.auth.auth import router as auth_router
from routes.user.user import router as user_router

app = FastAPI(title="My First API")

# Custom Exception Handlers register karna (405 Method Not Allowed, 404 Not Found etc. ke liye)
register_custom_handlers(app)

# Routers include karna
app.include_router(auth_router)
app.include_router(user_router)


# Root Route
@app.get("/")
def home():
    return Response.s("Welcome to my FastAPI backend!")
