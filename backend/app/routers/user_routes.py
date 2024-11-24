from fastapi import APIRouter, Depends
from app.models.user import UserRegister, UserLogin, UserPreferences
from app.utils.jwt_auth import create_access_token, get_current_user

router = APIRouter()

@router.post("/register")
async def register_user(user: UserRegister):
    return {"message": f"User {user.email} registered successfully."}

@router.post("/login")
async def login_user(user: UserLogin):
    token = create_access_token(data={"sub": user.email})
    return {"token": token}

@router.get("/preferences")
async def get_preferences(current_user: str = Depends(get_current_user)):
    return {"language": "en", "tone": "formal"}

@router.put("/preferences")
async def update_preferences(preferences: UserPreferences, current_user: str = Depends(get_current_user)):
    return {"message": "Preferences updated."}
