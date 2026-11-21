from typing import Any
from fastapi.responses import JSONResponse


class Response:

    @staticmethod
    def s(param1: Any = None, param2: Any = None, code: int = 200):
        message, data = False, []

        if param2 is None:
            if isinstance(param1, dict) and "message" in param1 and len(param1) == 1:
                message = param1["message"]
            elif isinstance(param1, str):
                message = param1
            elif param1 is not None:
                data = param1
        elif isinstance(param1, str):
            message, data = param1, {"token": param2} if isinstance(param2, str) else param2
        elif isinstance(param2, str):
            message, data = param2, {"token": param1} if isinstance(param1, str) else param1
        else:
            data, message = param1, param2

        return Response._send(True, message, data, code)

    @staticmethod
    def e(message: Any = "Error occurred", code: int = 400, data: Any = None):
        if isinstance(message, dict):
            data = {k: v for k, v in message.items() if k != "message"} or data or []
            message = message.get("message", "Error occurred")

        return Response._send(False, message, data, code)

    @staticmethod
    def _send(status: bool, message: Any, data: Any, code: int):
        http_code = code if 100 <= code <= 599 else (200 if status else 500)

        return JSONResponse(
            status_code=http_code,
            content={
                "status": status,
                "status_code": code,
                "message": message,
                "data": [] if data is None or data is False else data,
            },
            headers={
                "X-Content-Type-Options": "nosniff",
                "X-Frame-Options": "DENY",
                "Referrer-Policy": "strict-origin-when-cross-origin",
            },
        )