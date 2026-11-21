import uuid
from fastapi import APIRouter, HTTPException, status
from app.schemas import IssueCreate, IssueOut, IssueUpdate, IssueStatus
from app.storage import load_data, save_data

router = APIRouter(prefix="/api/v1/issues", tags=["issues"])

# The decorator connects this Python function to an HTTP method and URL.
# response_model documents the response and checks its shape before sending.
@router.get("/", response_model=list[IssueOut])
async def get_issues():
    """Retrieve all issues"""
    issues = load_data()
    return issues

# POST creates a new issue. FastAPI validates the JSON body as IssueCreate
# before this function runs, and returns 201 to indicate a resource was made.
@router.post("/", response_model=IssueOut, status_code=status.HTTP_201_CREATED)
def create_issue(payload: IssueCreate):
    """Create a new issue."""
    issues = load_data()
    # UUIDs provide a unique identifier without needing a database counter.
    new_issue = {
        "id": str(uuid.uuid4()),
        "title": payload.title,
        "description": payload.description,
        "priority": payload.priority,
        "status": IssueStatus.open,
    }
    issues.append(new_issue)
    # Save after changing the list so the new issue survives a server restart.
    save_data(issues)
    return new_issue

# The {issue_id} part is a URL parameter. FastAPI passes its value into the
# matching function argument below.
@router.get("/{issue_id}", response_model=IssueOut)
def get_issue(issue_id: str):
    """Retrieve an issue by ID."""
    issues = load_data()
    for issue in issues:
        if issue["id"] == issue_id:
            return issue
    # Raising HTTPException stops normal processing and sends an HTTP 404.
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")

@router.put("/{issue_id}", response_model=IssueOut)
def update_issue(issue_id: str, payload: IssueUpdate):
    """Update an existing issue by ID."""
    issues = load_data()
    for i, issue in enumerate(issues):
        if issue["id"] == issue_id:
            # Only replace fields the client supplied; omitted fields stay as-is.
            if payload.title is not None:
                issues[i]["title"] = payload.title
            if payload.description is not None:
                issues[i]["description"] = payload.description
            if payload.priority is not None:
                issues[i]["priority"] = payload.priority
            if payload.status is not None:
                issues[i]["status"] = payload.status
            save_data(issues)
            return issues[i]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")

@router.delete("/{issue_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_issue(issue_id: str):
    """Delete an existing issue by ID."""
    issues = load_data()
    for i, issue in enumerate(issues):
        if issue["id"] == issue_id:
            # Remove the matching item, then persist the shorter list.
            del issues[i]
            save_data(issues)
            # 204 means success with no response body.
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")




