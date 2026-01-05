from fastapi import FastAPI, Response, Request, Depends, HTTPException
from sqlmodel import Session, select
from database import engine, create_db_and_tables
from models import User
from auth import create_access_token, create_refresh_token, decode_token, pwd_context

app = FastAPI(title="Trade Finance Explorer API")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/auth/login")
async def login(response: Response, login_data: dict):
    with Session(engine) as session:
        user = session.exec(select(User).where(User.email == login_data["email"])).first()
        if not user or not pwd_context.verify(login_data["password"], user.password):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        # Set refresh token in HttpOnly cookie
        refresh_token = create_refresh_token({"sub": user.email})
        response.set_cookie(key="refresh_token", value=refresh_token, httponly=True)
        
        return {"access_token": create_access_token({"sub": user.email, "role": user.role})}