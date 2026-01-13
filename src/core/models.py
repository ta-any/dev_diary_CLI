from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field, validator
from uuid import uuid4

class DevDiaryEntry(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    text: str
    duration_minutes: Optional[int] = None
    git_commit: Optional[str] = None
    tags: List[str] = []
    detected_tech: List[str] = []      # ["Python", "FastAPI"]
    detected_categories: List[str] = [] # ["backend", "refactoring"]
    project: Optional[str] = None