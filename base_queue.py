class BaseQueue:
    current_password: str = ""
    served_customers: list = []
    code: int = 0
    queue: list = []

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
