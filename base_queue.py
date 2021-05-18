import abc
from typing import List, Union

from constants import MAX_STANDARD_SIZE, MIN_STANDARD_SIZE
from detailed_summary import DetailedSummary
from resumed_summary import ResumedSummary

Classes = Union[DetailedSummary, ResumedSummary]


class BaseQueue(metaclass=abc.ABCMeta):

    def __init__(self):
        self.current_password: str = ""
        self.served_customers: List[str] = []
        self.code: int = 0
        self.queue: List[str] = []

    @abc.abstractmethod
    def generate_current_password(self) -> None:
        ...

    @abc.abstractmethod
    def attend_customer(self, cashier: int) -> str:
        ...

    def refresh_queue(self) -> None:
        self.reset_queue()
        self.generate_current_password()
        self.insert_customer()

    def insert_customer(self):
        self.queue.append(self.current_password)

    def reset_queue(self) -> None:
        if self.code >= MAX_STANDARD_SIZE:
            self.code = MIN_STANDARD_SIZE
        else:
            self.code += 1

    def summary(self, summary: Classes) -> dict:
        return summary.make_summary(self.served_customers)
