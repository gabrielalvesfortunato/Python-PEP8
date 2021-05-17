from base_queue import BaseQueue


class PriorityQueue(BaseQueue):
    def generate_current_password(self) -> None:
        self.current_password = f'PRT{self.code}'

    def refresh_queue(self) -> None:
        self.reset_queue()
        self.generate_current_password()
        self.queue.append(self.current_password)

    def attend_customer(self, cashier: int) -> str:
        current_customer: str = self.queue.pop(0)
        self.served_customers.append(current_customer)
        return f'Current customer: {current_customer}, ' \
               f'go to the cashier: {cashier}'
