from ..models import DevDiaryEntry
from typing import List
from datetime import date
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from cli.commands.add import Add

def add_entry(text: str, duration: int = None, commit: str = None) -> DevDiaryEntry: 
    T = Add(text, duration, commit)
    task = T.create_entry()
    T.save_entry([task])

    print(20 * "===")
    print("Task")
    print(task)
    print(20 * "===")
    return task
def get_entries(from_date: date, to_date: date) -> List[DevDiaryEntry]:
    pass
# def generate_report(period: Literal["day", "week", "month"]) -> ReportData
# def search(query: str) -> List[DevDiaryEntry]