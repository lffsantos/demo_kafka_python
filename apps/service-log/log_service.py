import re
from apps.core.consumer.kafka_service import KafkaService


class LogService:

    def start(self):
        service = KafkaService(re.compile("ECOMMERCE.*"), self.parse, LogService.__name__, {})
        service.run()

    def parse(self, record):
        print("------------------------------------------")
        print("LOG: " + record.topic)
        print(
            "%d:%d: key=%s value=%s" % (record.partition, record.offset, record.key, record.value))


if __name__ == '__main__':
    log_service = LogService()
    log_service.start()
