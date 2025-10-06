from fastapi import FastAPI, Request
from middleware import cors_middleware
from middleware import logging_middleware
from middleware import ip_middleware
from controller.crawl_controller import router as crawlRouter
from database.database import database

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
ip_middleware.add(app)

app.include_router(crawlRouter)
database.check_connection()
    
@app.get("/")
def readRoot(request: Request): 
    # client_host = request.state.client_ip
    return {"message": "Wel come to VI NLP AI AGENTS PLATFORM", "Information": info}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="main:app", port=5000, reload=True)