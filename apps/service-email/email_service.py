import time

from apps.core.consumer.service_runner import ServiceRunner


class EmailService(ServiceRunner):
    def __init__(self):
        super().__init__(EmailService)
        self.start(5)

    def parse(self, record):
        print("------------------------------------------");
        print("Send email")
        print("%s:%d:%d: key=%s value=%s" % (record.topic, record.partition,
                                             record.offset, record.key,
                                             record.value))
        try:
            time.sleep(1)
        except InterruptedError as error:
            raise error

        print("Email sent")

    @classmethod
    def get_consumer_group(cls):
        return EmailService.__name__

    @classmethod
    def get_topic(cls):
        return "ECOMMERCE_SEND_EMAIL"


if __name__ == '__main__':
    email_service = EmailService()
