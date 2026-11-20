from fastapi import FastAPI
from app.routes.issues import router as issues_router
from app.middleware.timer import timing_middleware
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

app.middleware("http")(timing_middleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(issues_router)

#  Thanks To Brad Traversy for the FastAPI crash course which I used as a reference for this project.
#  https://github.com/bradtraversy/fastapi-issue-tracker/blob/main/docs/crash_course.md
# Future upgraded todo: Add authentication and authorization.