from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware

class ClientIPMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # LẤY IP TỪ HEADER (KHI CHẠY SAU PROXY)
        x_forwarded_for = request.headers.get("x-forwarded-for")
        if x_forwarded_for:
            client_ip = x_forwarded_for.split(",")[0].strip()
        else:
            # NẾU KHÔNG CÓ HEADER THÌ DÙNG IP GỐC
            client_ip = request.client.host

        # GÁN VÀO request.state ĐỂ DÙNG Ở ROUTE KHÁC
        request.state.client_ip = client_ip

        response = await call_next(request)
        return response

def add(app: FastAPI):
    app.add_middleware(ClientIPMiddleware)