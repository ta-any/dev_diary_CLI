# from pathlib import Path
# from typing import Optional

# from .json_storage import JSONStorage


# def get_storage(data_dir: Optional[Path] = None):
#     """
#     Фабрика хранилища.
#     На текущем этапе всегда возвращает JSONStorage.
#     Позволяет легко заменить реализацию в будущем.
#     """
#     return JSONStorage(data_dir=data_dir)