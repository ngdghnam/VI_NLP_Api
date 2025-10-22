# VI NLP API

## Hướng dẫn sử dụng

### Bước 1: Tạo file .env

Check theo file `.env.example` để tạo các biến môi trường cần thiết cho việc chạy và thao tác với phần mềm

### Bước 2: Tạo môi trường ảo

#### Prequisites - Yêu cầu trước khi cài đặt

Cài đặt thư viện _virtualenv_ của Python:

`pip install virtualenv`

#### Hướng dẫn tạo môi trường ảo

Sau khi đã cài đặt xong, mở thư mục gốc của source code và mở terminal lên nhập câu lệnh sau:

`python -m venv .venv`

Câu lệnh này sẽ tạo môi trường ảo để bạn cài đặt tất cả các gói package (thư viện cần thiết) cho dự án.

Sau khi tạo xong, nhập tiếp lệnh này để tiến hành cho môi trường ảo hoạt động:

`.venv/Scripts/activate`

### Bước 3: Cài đặt các Package cho toàn bộ dự án

Giữ nguyên Terminal tại thư mục gốc của dự án, tiến hành nhập câu lệnh:

`pip install -r requirements.txt`

Lệnh này sẽ đọc toàn bộ package có trong file txt và tiến hành cài đặt toàn bộ package vào môi trường ảo.

### Bước 3: Tải và sử dụng MYSQL

Xem và làm theo hướng dẫn sử dụng tại link sau: [Hướng dẫn cài đặt MYSQL](https://youtu.be/dq1L1Lrbg6s?si=WOJrrvMIIdm-yt3c)

### Bước 4: Hướng dẫn cài đặt Docker

Xem và học theo tutorial: [Docker cơ bản A - Z](https://youtube.com/playlist?list=PLncHg6Kn2JT4kLKJ_7uy0x4AdNrCHbe0n&si=zPy2kzzbNcQMuOyW)

Cài đặt Docker: [Cài đặt & Setup Docker](https://www.docker.com/)

### Bước 5: setup N8N với Docker

Bạn có thể tìm hướng dẫn setup Docker chi tiết tại trang chủ của họ: [Install Docker với n8n](https://docs.n8n.io/hosting/installation/docker/)

Trong project này, chúng ta sẽ đi nhanh. Tại terminal thư mục nguồn, chạy 2 câu lệnh lần lượt sau:

`docker pull docker.n8n.io/n8nio/n8n`

`docker run --name=<your_container_name> -p 5678:5678 -d docker.n8n.io/n8nio/n8n`

Sau khi chạy thành công, truy cập vào `localhost:5678` để chạy n8n.

### Bước 6: Import file và chạy Server

1. Hãy import file json workflow vào trong n8n để chạy kết quả
2. tại terminal nguồn, chạy câu lệnh: `python -u main.py`

## Cấu trúc thư mục

Cấu trúc dự án được chia như sau:

server/
│
├── **pycache**/ # Python cache files (tự động tạo)
├── .venv/ # Môi trường ảo Python
│
├── alembic/ # Database migration
│ ├── versions/ # Các file migration
│ └── env.py # Cấu hình Alembic
│
├── config/ # Cấu hình ứng dụng
│ ├── **init**.py
│ ├── database.py # Cấu hình database
│ ├── settings.py # Cài đặt chung
│ └── security.py # Cấu hình bảo mật
│
├── constant/ # Hằng số và enum
│ ├── **init**.py
│ ├── status.py # Status codes
│ ├── roles.py # User roles
│ └── messages.py # Message templates
│
├── controller/ # Business logic layer
│ ├── **init**.py
│ ├── user_controller.py
│ ├── auth_controller.py
│ └── product_controller.py
│
├── core/ # Core functionality
│ ├── **init**.py
│ ├── security.py # Authentication, JWT
│ ├── dependencies.py # FastAPI dependencies
│ └── exceptions.py # Custom exceptions
│
├── database/ # Database models và schemas
│ ├── **init**.py
│ ├── base.py # Base model class
│ └── session.py # Database session
│
├── decorator/ # Custom decorators
│ ├── **init**.py
│ ├── auth_required.py # Authentication decorator
│ └── rate_limit.py # Rate limiting decorator
│
├── dto/ # Data Transfer Objects
│ ├── **init**.py
│ ├── user_dto.py # User request/response DTOs
│ └── product_dto.py # Product DTOs
│
├── html/ # HTML templates
│ ├── base.html # Base template
│ ├── index.html # Homepage
│ └── email/ # Email templates
│ └── welcome.html
│
├── logs/ # Application logs
│ ├── app.log
│ └── error.log
│
├── middleware/ # Middleware functions
│ ├── **init**.py
│ ├── cors.py # CORS middleware
│ ├── logging.py # Request logging
│ └── error_handler.py # Error handling
│
├── model/ # Database models (ORM)
│ ├── **init**.py
│ ├── user.py # User model
│ ├── product.py # Product model
│ └── base.py # Base model
│
├── n8n/ # N8N automation workflows
│ └── workflows/
│
├── prompt/ # AI prompts (nếu dùng AI)
│ └── templates/
│
├── repository/ # Data access layer
│ ├── **init**.py
│ ├── user_repository.py
│ ├── product_repository.py
│ └── base_repository.py
│
├── service/ # Business services
│ ├── **init**.py
│ ├── user_service.py # User business logic
│ ├── auth_service.py # Authentication logic
│ └── email_service.py # Email sending
│
├── spec/ # API specifications
│ └── openapi.yaml # OpenAPI/Swagger spec
│
├── utils/ # Utility functions
│ ├── **init**.py
│ ├── helpers.py # Helper functions
│ ├── validators.py # Validation functions
│ └── formatters.py # Data formatting
│
├── .env # Environment variables (không commit)
├── .env.example # Environment variables template
├── .gitignore # Git ignore rules
├── .llm.env # LLM configuration
├── alembic.ini # Alembic configuration
├── main.py # Application entry point
├── README.md # Documentation
└── requirements.txt # Python dependencies
