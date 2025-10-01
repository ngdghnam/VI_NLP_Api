from fastapi import FastAPI
from middleware import cors_middleware
from middleware import logging_middleware

app: FastAPI = FastAPI()

info: dict = {
    "members": [
        {"name": "Nguyễn Đặng Hoài Nam", "role": "Full Stack Developer"},
        {"name": "Nguyễn Xuân Quỳnh", "role": "Project Manager"},
        {"name": "Trần Xuân Hương", "role": "Designer"},
        {"name": "Trần Xuân Hương", "role": "Designer"},
        {"name": "Nguyễn Hoàng Hương Giang", "role": "Business Analyst"},
        {"name": "Lưu Hà Vy", "role": "Product Owner"},
    ],
    "Version": "1.0.0"
}

cors_middleware.add(app)
logging_middleware.add(app)

@app.get("/")
def readRoot(): 
    return {"message": "Wel come to VI NLP AI AGENTS PLATFORM", "Information": info}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="main:app", port=5000, reload=True)