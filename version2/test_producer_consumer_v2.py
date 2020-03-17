import unittest

from  threading import Thread
from  producer_consumer import  Producer, Consumer, Scheduler
class MyTestCase(unittest.TestCase):
    def create_producers(self, scheduler, n = 3):
        threads = []
        def run(producer):
            producer.produce()
        for i in range(n):
            producer = Producer(scheduler, str(i))

            threads.append(Thread(target=run, args=(producer, )))
        return threads


    def create_consumers(self, scheduler, n = 3):
        threads = []
        def run(consumer):
            consumer.consume()

        for i in range(n):
            consumer = Consumer(scheduler, str(i))
            threads.append(Thread(target=run, args=(consumer, )))

        return threads

    def test_producer_and_consumer(self):
        scheduler = Scheduler(10)
        consumers = self.create_consumers(scheduler, 2)
        producers = self.create_producers(scheduler, 3)

        for c in consumers:
            c.start()
        for p in producers:
            p.start()


if __name__ == '__main__':
    unittest.main()
