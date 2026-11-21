from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login")
def login():
    # Yahan Response ko import nahi kiya gaya hai, yeh direct globally chalega!
    return Response.s("Login successful!", {"token": "sample_token_12345"})
