from typing import List, Dict, Union


class ResumedSummary:
    def __init__(self, day: str, agency: int) -> None:
        self.day = day
        self.agency = agency

    def make_summary(self, served_customers: List[str]) -> dict:
        summary: Dict[str, Union[List[str], str, int]] = {
            f'{self.agency} - {self.day}': len(served_customers)
        }
        return summary
