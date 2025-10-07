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
