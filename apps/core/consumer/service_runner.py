from abc import ABCMeta, abstractmethod
from concurrent.futures import ThreadPoolExecutor

from apps.core.consumer.kafka_service import KafkaService


class ServiceRunner(metaclass=ABCMeta):

    service = None

    def __init__(self, service):
        self.service = service

    def start(self, thread_count):
        self._create_provider()
        print("aoaoa")
        with ThreadPoolExecutor(max_workers=thread_count) as executor:
            print("oi")
            future = executor.submit(self.provider)

    def _create_provider(self):
        kafka_service = KafkaService(
            self.service.get_topic(), self.parse, self.service.get_consumer_group(), {}
        )
        kafka_service.run()
        print("aoaoa")

    @abstractmethod
    def parse(self, record):
        pass

    @abstractmethod
    def get_consumer_group(self):
        pass

    @abstractmethod
    def get_topic(self):
        pass
