# Добавить запись в журнал

import sys
from pathlib import Path


project_root = Path(__file__).parent.parent.parent.parent  
sys.path.insert(0, str(project_root))

# sys.path.insert(0, str(Path(__file__).parent.parent))
# from core.models import DevDiaryEntry
# from parsers.stack_parser import parse
# from storage.json_storage import IStorage

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

try:
    from src.storage.json_storage import get_storage
except ImportError:
    import os
    os.chdir(project_root)
    from src.storage.json_storage import get_storage
    
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
    def save_entry(self, modul: DevDiaryEntry) -> bool:
        storage = get_storage() 
        storage.save(modul)

        return True