import random
from threading import Lock, Condition, Semaphore
import time
class Producer():
    def __init__(self, scheduler, producer_id):
        self.scheduler =scheduler
        self.producer_id = producer_id

    def produce(self):
        while True:
            value = random.randint(0, 100)
            self.scheduler.insert(value)
            print("producer_id={0}|produce value={1}".format(self.producer_id, value))

class Consumer():
    def __init__(self,scheduler, consumer_id):
        self.scheduler =scheduler
        self.consumer_id = consumer_id

    def consume(self):
        while True:
            value = self.scheduler.remove()
            print("consumer_id={0}|consume value={1}".format(self.consumer_id, value))

class Scheduler():
    def __init__(self, capacity):
        self.producer_semaphore = Semaphore(capacity)
        self.consumer_semaphore = Semaphore(capacity)

        self.lock = Lock()
        self.capacity = capacity
        self.queue = [0] * self.capacity
        self.start = 0
        self.end = 0
        self.length = 0

    def __is_empty(self):
        return self.length == 0

    def __is_full(self):
        return self.length == self.capacity


    def insert(self, value):
        """ busy waiting here"""

        self.producer_semaphore.acquire()

        self.lock.acquire()

        self.queue[self.end] = value
        self.end = (self.end + 1) % self.capacity
        self.length += 1

        self.lock.release()

        self.consumer_semaphore.release()

    def remove(self):
        self.consumer_semaphore.acquire()
        self.lock.acquire()

        value = self.queue[self.start]
        self.start = (self.start + 1) % self.capacity
        self.length -= 1
        self.lock.release()

        self.producer_semaphore.release()
        return value
