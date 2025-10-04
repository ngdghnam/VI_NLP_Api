from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from config.env import settings

class Database:
    def __init__(self):
        self.DATABASE_URL = (
            f"{settings.DB_DIALECT}+mysqlconnector://"
            f"{settings.DB_USER}:{settings.DB_PASSWORD}@"
            f"{settings.DB_HOST}:{settings.DB_PORT}/"
            f"{settings.DB_NAME}"
        )
        self.engine = create_engine(self.DATABASE_URL, echo=True)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_db(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()

    def check_connection(self):
        try:
            with self.engine.connect() as conn:
                conn.execute("SELECT 1")
            print("Database connected successfully!")
            return True
        except OperationalError as e:
            print(f"Database connection failed: {e}")
            return False

# Khởi tạo instance nếu cần dùng chung
database = Database()

