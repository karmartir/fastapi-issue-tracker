# FastAPI provides the tools for building the web API.
from fastapi import FastAPI
# Import the issue routes so they can be connected to the main application.
from app.routes.issues import router as issues_router
# This middleware measures request time and adds it to the response.
from app.middleware.timer import timing_middleware
# CORS middleware controls which browser-based websites can call this API.
from fastapi.middleware.cors import CORSMiddleware


# Create the main application object. The development server loads this `app`
# variable to receive incoming requests and send responses.
app = FastAPI()

# Register timing middleware so each response includes how long the request
# took in its `X-Process-Time` header. See app/middleware/timer.py for details.
app.middleware("http")(timing_middleware)

# Allow browser frontends hosted on another origin to call this API. These
# wildcard settings allow any origin, method, and header, which is convenient
# while learning; a deployed app should specify only the origins it trusts.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # Which website origins may make browser requests.
    allow_credentials=True,   # Allow browser requests to include credentials.
    allow_methods=["*"],      # Allow all HTTP methods, such as GET, POST, and DELETE.
    allow_headers=["*"],      # Allow browser requests to use any HTTP headers.
)
# Register the issue endpoints. Their shared URL prefix, /api/v1/issues, is
# defined on the router in app/routes/issues.py.
app.include_router(issues_router)

#  Thanks To Brad Traversy for the FastAPI crash course which I used as a reference for this project.
#  https://github.com/bradtraversy/fastapi-issue-tracker/blob/main/docs/crash_course.md
# Future upgraded todo: Add authentication and authorization.
