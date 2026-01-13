# Добавить запись в журнал

import sys
from pathlib import Path

# Добавляем путь к корню проекта
project_root = Path(__file__).parent.parent.parent.parent  
sys.path.insert(0, str(project_root))


try:
    from src.core.models import DevDiaryEntry
except ImportError:
    import os
    os.chdir(project_root)
    from src.core.models import DevDiaryEntry

try:
    from src.parsers.stack_parser import parse
except ImportError:
    import os
    os.chdir(project_root)
    from src.parsers.stack_parser import parse

class Add():
    def __init__(self,text: str, duration: int = None, commit: str = None ):
        self.text = text
        self.duration = duration
        self.commit = commit
    
    def create_entry(self) -> DevDiaryEntry:
        """Создает и возвращает запись"""
        tech, cats = parse(self.text)

        return DevDiaryEntry(
            text=self.text,
            duration_minutes=self.duration,
            git_commit=self.commit,
            tags=["bug", "auth", "security"],  # Примерные теги
            detected_tech=tech,  
            detected_categories=cats, 
            project="AuthService"  # Пример
        )