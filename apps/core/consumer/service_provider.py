from apps.core.consumer.kafka_service import KafkaService


class ServiceProvider:
    factory = None

    def __init__(self, factory):
        self.factory = factory

    def call(self):
        my_service = self.factory.create()
        service = KafkaService(
            my_service.get_consumer_group,
            my_service.get_topic,
            self.factory.parse,
            {}
        )
        service.run()
