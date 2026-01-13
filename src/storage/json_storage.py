import json
import shutil
from datetime import datetime
from pathlib import Path
from typing import List, Protocol
import logging

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from core.models import DevDiaryEntry

logger = logging.getLogger(__name__)

class IStorage(Protocol):
    """Абстрактный интерфейс хранилища записей."""
    def save(self, entries: List[DevDiaryEntry]) -> None:
        ...

    def load(self) -> List[DevDiaryEntry]:
        ...

    def backup(self) -> Path:
        ...


class JSONStorage:
    """Реализация хранилища на основе JSON-файла."""

    def __init__(self, data_dir: Path | None = None):
        self.data_dir = data_dir or Path.home() / ".devdiary"
        self.data_dir.mkdir(exist_ok=True)
        self.entries_file = self.data_dir / "entries.json"

    def _backup_current(self) -> Path | None:
        """Создаёт резервную копию текущего файла entries.json, если он существует."""
        if not self.entries_file.exists():
            return None

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"entries_{timestamp}.bak.json"
        backup_path = self.data_dir / backup_name
        shutil.copy2(self.entries_file, backup_path)
        return backup_path

    def _serialize_entry(self, entry: DevDiaryEntry) -> dict:
        """Преобразует Pydantic-модель в словарь, совместимый с JSON."""
        data = entry.model_dump()
        # Убеждаемся, что UUID и datetime сериализованы как строки
        data["id"] = str(data["id"])
        data["timestamp"] = data["timestamp"].isoformat()
        return data

    def _deserialize_entry(self, data: dict) -> DevDiaryEntry:
        """Восстанавливает Pydantic-модель из словаря."""
        return DevDiaryEntry(**data)

    def save(self, entries: List[DevDiaryEntry]) -> None:
        """Сохраняет список записей в JSON-файл."""
        try:
            # Упрощенный вариант: просто сохраняем в файл
            serialized_entries = [self._serialize_entry(entry) for entry in entries]
            
            with self.entries_file.open("w", encoding="utf-8") as f:
                json.dump(serialized_entries, f, ensure_ascii=False, indent=2)
                
            logger.debug(f"Успешно сохранено {len(entries)} записей в {self.entries_file}")
            
        except Exception as e:
            logger.error(f"Ошибка при сохранении в {self.entries_file}: {e}")
            raise

    def load(self) -> List[DevDiaryEntry]:
        """Загружает записи из JSON-файла. Возвращает пустой список, если файл отсутствует."""
        if not self.entries_file.exists():
            return []

        try:
            with self.entries_file.open("r", encoding="utf-8") as f:
                raw_data = json.load(f)
            return [self._deserialize_entry(item) for item in raw_data]
        except (json.JSONDecodeError, KeyError, ValueError) as e:
            raise RuntimeError(f"Ошибка чтения {self.entries_file}: {e}")

    def backup(self) -> Path:
        """Публичный метод для ручного создания бэкапа."""
        backup_path = self._backup_current()
        if backup_path is None:
            raise FileNotFoundError("Нет файла для резервного копирования.")
        return backup_path
    

def get_storage(data_dir: Path | None = None) -> JSONStorage:
    """
    Фабричная функция для получения экземпляра хранилища.
    Используется для инъекции зависимостей.
    """
    return JSONStorage(data_dir)
