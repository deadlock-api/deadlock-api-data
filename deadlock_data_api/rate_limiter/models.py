# import logging
# import time
#
# from fastapi import HTTPException
# from pydantic import BaseModel
#
# LOGGER = logging.getLogger(__name__)
#
#
# class RateLimitStatus(BaseModel):
#     key: str
#     count: int
#     limit: int
#     period: int
#     oldest_request_time: float
#
#     @property
#     def remaining(self) -> int:
#         return max(self.limit - self.count, 0)
#
#     @property
#     def is_limited(self) -> bool:
#         return self.count > self.limit
#
#     @property
#     def next_request_in(self) -> float:
#         if self.count < self.limit:
#             return 0
#         age_of_last_request = time.time() - self.oldest_request_time
#         return max(self.period - age_of_last_request, 0)
#
#     @property
#     def headers(self) -> dict[str, str]:
#         return {
#             "RateLimit-Limit": str(self.limit),
#             "RateLimit-Period": str(self.period),
#             "RateLimit-Remaining": str(self.remaining),
#             "RateLimit-Reset": str(self.next_request_in),
#             "Retry-After": str(self.next_request_in),
#         }
#
#     def raise_for_limit(self):
#         if self.is_limited:
#             raise HTTPException(
#                 status_code=429,
#                 detail={
#                     "error": "rate_limit_exceeded",
#                     "message": "Rate limit exceeded, please check the headers for more information.",
#                 },
#                 headers=self.headers,
#             )
#
#
# class RateLimit(BaseModel):
#     limit: int
#     period: int
#     path: str | None = None
