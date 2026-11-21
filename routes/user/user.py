from fastapi import APIRouter

# APIRouter banayein
router = APIRouter(prefix="/user", tags=["User"])


@router.get("/profile")
def get_profile():
    return {
        "status": "success",
        "message": "User profile data!"
    }
