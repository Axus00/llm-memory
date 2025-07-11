from pydantic import BaseModel


class User(BaseModel):
    id: str
    name: str
    age: int
    email: str
    is_active: bool
    has_chat_active: bool


def __init__(self, name, age, email, is_active, has_chat_active):
    self.name = name
    self.age = age
    self.email = email
    self.is_active = is_active
    self.has_chat_active = has_chat_active


user_db = {
    "id": "user_one",
    "name": "Fernando",
    "age": 25,
    "email": "fernando.gomez@blackbirdlabs.com.co",
    "is_active": True,
    "has_chat_active": False
}


def list_all_users():
    try:
        if not user_db:
            return {"message": "no hay usuarios existentes"}
        return user_db
    except Exception as e:
        raise f"ha ocurrido un error inesperado {str(e)}"
