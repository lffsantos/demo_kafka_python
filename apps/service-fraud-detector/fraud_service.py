import time

from decimal import Decimal

from apps.core.consumer.service_runner import ServiceRunner
from models import Order


class FraudDetectorService(ServiceRunner):
    def __init__(self):
        super().__init__(FraudDetectorService)
        self.start(1)

    def parse(self, record):
        print("------------------------------------------")
        print("Fraud email")

        message = record.value
        order = Order(**message.payload)

        print("%s:%d:%d: key=%s value=%s" % (record.topic, record.partition,
                                             record.offset, record.key,
                                             order))

        if self.was_processed(order):
            print(f'Order {order.order_id} was already processed')
        try:
            time.sleep(1)
        except InterruptedError as error:
            raise error

        if self.is_fraud(order):
            print("Order is a fraud!")
        else:
            print("Approved Order!!")

    @classmethod
    def get_consumer_group(cls):
        return FraudDetectorService.__name__

    @classmethod
    def get_topic(cls):
        return "ECOMMERCE_FRAUD"

    @staticmethod
    def was_processed(order):
        return False

    @staticmethod
    def is_fraud(order):
        return Decimal(order.amount) >= Decimal("120")


if __name__ == '__main__':
    fraud_service = FraudDetectorService()
