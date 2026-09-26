from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.db.database import get_db, engine
from app.models.user import User
from app.db.database import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Game Library API")

@app.get("/")
def root():
    return {"message": "Game Library API is running"}

@app.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    try:
        result = db.execute(text("SELECT 1")).scalar()
        return {"status": "success", "database_connected": True, "result": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}