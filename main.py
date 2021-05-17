from normal_queue import NormalQueue
from priority_queue import PriorityQueue

test_queue = NormalQueue()
test_queue.refresh_queue()
test_queue.refresh_queue()
print(test_queue.attend_customer(5))
print(test_queue.attend_customer(10))

print("\n|------------------------------------|\n")

test_queue_2 = PriorityQueue()
test_queue_2.refresh_queue()
test_queue_2.refresh_queue()
test_queue_2.refresh_queue()
print(test_queue_2.attend_customer(10))
print(test_queue_2.attend_customer(1))

print("\n|------------------------------------|\n")

print(test_queue_2.statistics("10/01/2020", 2001, "detail"))
