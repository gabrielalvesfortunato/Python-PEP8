from typing import Union

from normal_queue import NormalQueue
from priority_queue import PriorityQueue
from constants import NORMAL_QUEUE_TYPE, PRIORITY_QUEUE_TYPE


class QueueFactory:

    @staticmethod
    def choose_queue(queue_type) -> Union[NormalQueue, PriorityQueue]:
        if queue_type == NORMAL_QUEUE_TYPE:
            return NormalQueue()
        elif queue_type == PRIORITY_QUEUE_TYPE:
            return PriorityQueue()
        else:
            raise NotImplementedError("Queue type doesn't exist.")
