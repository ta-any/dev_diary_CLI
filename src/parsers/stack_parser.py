# Возвращает: tech=["Python"], cats=["backend"]

from typing import List, Tuple

TECH_KEYWORDS = {
    "Python": ["python", "fastapi", "django", "flask", "pydantic"],
    "JavaScript": ["js", "react", "node", "express", "vue"],
    "PostgreSQL": ["postgres", "postgresql", "psql"],
    # ...
}
CATEGORIES = {
    "backend": ["api", "server", "auth", "database", "endpoint"],
    "testing": ["test", "pytest", "mock", "coverage"],
    "docs": ["doc", "readme", "swagger", "openapi"],
}

def parse(text: str) -> Tuple[List[str], List[str]]:
    """
        args text: str
        return (tech=["Python"], cats=["backend"])
    """
    return (["Python", "FastAPI", "JWT"], ["backend", "bugfix"])