from base_queue import BaseQueue


class NormalQueue(BaseQueue):
    def generate_current_password(self) -> None:
        self.current_password = f'NRM{self.code}'

    def attend_customer(self, cashier: int) -> str:
        current_customer: str = self.queue.pop(0)
        self.served_customers.append(current_customer)
        return f'Current customer: {current_customer}, ' \
               f'go to the cashier: {cashier}'
