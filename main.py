from queue_factory import QueueFactory
from detailed_summary import DetailedSummary
from resumed_summary import ResumedSummary


queue = QueueFactory.choose_queue("priority")
queue.refresh_queue()
print(queue.attend_customer(10))
queue.refresh_queue()
print(queue.attend_customer(5))

print(queue.summary(DetailedSummary("20/03/2022", 201)))
print(queue.summary(ResumedSummary("20/03/2022", 201)))
