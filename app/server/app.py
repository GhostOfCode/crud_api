from fastapi import FastAPI
from .routes.user import router as UserRouter

app = FastAPI(title="CRUD_API")

#  Main methods of API (routes) with tag "User"
app.include_router(UserRouter, tags=["User"], prefix="/user")


#  Welcome
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this test CRUD app!"}
