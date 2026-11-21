import time
from fastapi import Request

async def timing_middleware(request: Request, call_next):
    # Start a high-resolution timer before passing the request to the next
    # middleware or route handler.
    start = time.perf_counter()
    response = await call_next(request)
    # Add elapsed time to the outgoing response so API clients can inspect it.
    response.headers["X-Process-Time"] = f"{time.perf_counter() - start:.4f}s"
    return response
