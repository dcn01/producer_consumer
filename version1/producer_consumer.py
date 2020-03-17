import random
from threading import Lock
import time

class Producer():
    def __init__(self, scheduler, producer_id):
        self.scheduler =scheduler
        self.producer_id = producer_id

    def produce(self):
        while True:
            value = random.randint(0, 100)
            ans = self.scheduler.insert(value)
            if ans:
                print("producer_id={0}|produce value={1}".format(self.producer_id, value))

class Consumer():
    def __init__(self,scheduler, consumer_id):
        self.scheduler =scheduler
        self.consumer_id = consumer_id

    def consume(self):
        while True:
            value = self.scheduler.remove()

            if value != False:
                print("consumer_id={0}|consume value={1}".format(self.consumer_id, value))

class Scheduler():
    def __init__(self, capacity):
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
        if self.__is_full():
            print("queue is full")
            return False

        self.lock.acquire()
        self.queue[self.end] = value
        self.end = (self.end + 1) % self.capacity
        self.length += 1
        self.lock.release()

        return True

    def remove(self):
        if self.__is_empty():
            print("queue is empty")
            return False

        self.lock.acquire()
        value = self.queue[self.start]
        self.start = (self.start + 1) % self.capacity
        self.length -= 1
        self.lock.release()

        return value

