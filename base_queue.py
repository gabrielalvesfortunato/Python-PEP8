import abc
from typing import List, Dict, Union

from constants import MAX_STANDARD_SIZE, MIN_STANDARD_SIZE


class BaseQueue(metaclass=abc.ABCMeta):
    current_password: str = ""
    served_customers: List[str] = []
    code: int = 0
    queue: List[str] = []

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

    def statistics(self, day: str, agency: int, flag: str = None) -> dict:
        statistic: Dict[str, Union[List[str], str, int]] = {}
        if flag != "detail":
            statistic[f'{agency}-{day}'] = len(self.served_customers)
        else:
            statistic = {
                "day": day,
                "agency": agency,
                "served customers": self.served_customers,
                "number of served customers": len(self.served_customers)
            }

        return statistic
