from typing import List, Dict, Union


class DetailedSummary:
    def __init__(self, day: str, agency: int) -> None:
        self.day = day
        self.agency = agency

    def make_summary(self, served_customers: List[str]) -> dict:
        summary: Dict[str, Union[str, int, list]] = {
            "day": self.day,
            "agency": self.agency,
            "served customers": served_customers,
            "number of served customers": len(served_customers)
        }
        return summary
