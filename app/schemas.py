from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional

class IssueStatus(str, Enum):
    # Restrict issue status to these exact values. Inheriting from str means
    # the values also serialize naturally as JSON strings.
    open = "open"
    in_progress = "in_progress"
    closed = "closed"

class IssuePriority(str, Enum):
    # A second set of allowed string values, used for issue priority.
    low = "low"
    medium = "medium"
    high = "high"

class IssueCreate(BaseModel):
    # Fields and rules for a request that creates a new issue. FastAPI asks
    # Pydantic to validate the incoming JSON against this model.
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=5, max_length=1000)
    priority: IssuePriority = IssuePriority.medium

class IssueUpdate(BaseModel):
    # Fields accepted when editing an issue. None defaults make each field
    # optional, so a client can send only the values it wants to change.
    title: Optional[str] = Field(default=None, max_length=100)
    description: Optional[str] = Field(default=None, max_length=1000)
    priority: Optional[IssuePriority] = None
    status: Optional[IssueStatus] = None

class IssueOut(BaseModel):
    # Shape of an issue returned by the API. FastAPI uses this response model
    # to validate and serialize route results.
    id: str
    title: str
    description: str
    priority: IssuePriority
    status: IssueStatus
