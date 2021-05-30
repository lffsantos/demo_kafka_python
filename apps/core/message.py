from apps.core.correlation_id import CorrelationId


class Message:
    payload = None
    id: CorrelationId

    def __init__(self, correlation_id: CorrelationId, payload: object):
        self.id = correlation_id
        self.payload = payload
