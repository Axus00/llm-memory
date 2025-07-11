from fastapi import FastAPI, HTTPException, status, APIRouter
from models.user import User, list_all_users


app = FastAPI()
router = APIRouter()


@router.get("/users/", response_model=User)
async def get_user():
    users = list_all_users()


    if(users is None):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay usuarios en la base de datos")
    
    return users

app.include_router(router)