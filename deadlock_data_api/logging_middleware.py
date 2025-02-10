import json
import logging
import time
from collections.abc import Callable
from typing import Any
from uuid import uuid4

from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import Message

from deadlock_data_api.utils import AsyncIteratorWrapper


class RouterLoggingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI, *, logger: logging.Logger) -> None:
        self._logger = logger
        super().__init__(app)

    async def dispatch(self, req: Request, call_next: Callable) -> Response:
        request_id = str(uuid4())
        logging_dict = {"X-API-REQUEST-ID": request_id}

        await self.set_body(req)
        res, res_dict = await self._log_response(call_next, req, request_id)
        request_dict = await self._log_request(req)
        logging_dict.update({"request": request_dict, "response": res_dict})

        self._logger.info(logging_dict)
        return res

    async def set_body(self, request: Request):
        receive_ = await request._receive()

        async def receive() -> Message:
            return receive_

        request._receive = receive

    async def _log_request(self, req: Request) -> dict[str, Any]:
        path = req.url.path
        if req.query_params:
            path += f"?{req.query_params}"

        request_logging = {"method": req.method, "path": path, "ip": req.client.host}

        try:
            api_key = req.headers.get("X-API-Key", req.query_params.get("api_key"))
            request_logging["X-API-Key"] = api_key
        except Exception:
            pass

        try:
            request_logging["body"] = await req.json()
        except json.JSONDecodeError:
            pass

        return request_logging

    async def _log_response(
        self, call_next: Callable, req: Request, req_id: str
    ) -> tuple[Response, dict[str, Any]]:
        start_time = time.perf_counter()
        res = await self._execute_request(call_next, req, req_id)
        execution_time = time.perf_counter() - start_time

        overall_status = "successful" if res.status_code < 400 else "failed"
        res_logging = {
            "status": overall_status,
            "status_code": res.status_code,
            "time_taken": f"{execution_time:0.4f}s",
        }

        resp_body = [section async for section in res.__dict__["body_iterator"]]
        res.__setattr__("body_iterator", AsyncIteratorWrapper(resp_body))
        return res, res_logging

    async def _execute_request(self, call_next: Callable, req: Request, req_id: str) -> Any | None:
        try:
            res = await call_next(req)
            res.headers["X-API-Request-ID"] = req_id
            return res
        except Exception as e:
            self._logger.exception({"path": req.url.path, "method": req.method, "reason": e})
