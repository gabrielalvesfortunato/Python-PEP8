import abc


class BaseQueue(metaclass=abc.ABCMeta):
    current_password: str = ""
    served_customers: list = []
    code: int = 0
    queue: list = []

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
        if self.code >= 200:
            self.code = 0
        else:
            self.code += 1

    def statistics(self, day: str, agency: int, flag: str = None) -> dict:
        if flag != "detail":
            statistic = {f'{agency}-{day}': len(self.served_customers)}
        else:
            statistic = {
                "day": day,
                "agency": agency,
                "served customers": self.served_customers,
                "number of served customers": len(self.served_customers)
            }

        return statistic
