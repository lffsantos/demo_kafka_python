import uuid
from decimal import Decimal
from random import random

from apps.core.correlation_id import CorrelationId
from apps.core.dispatcher.kafka_dispatcher import KafkaDispatcher
from models import Order

if __name__ == '__main__':
    order_dispatcher = KafkaDispatcher()
    email = " teste@email.com"
    orderId = str(uuid.uuid4())
    amount = Decimal(str(random() * 500 + 1))

    order = Order(orderId, amount, email)
    print(order)
    correlation_id = CorrelationId('__name__')
    order_dispatcher.send("ECOMMERCE_FRAUD", email, correlation_id, order)
    print("main")

# package br.com.alura.ecommerce;
#
# import br.com.alura.ecommerce.dispatcher.KafkaDispatcher;
#
# import java.math.BigDecimal;
# import java.util.UUID;
# import java.util.concurrent.ExecutionException;
#
# public class NewOrderMain {
#
#     public static void main(String[] args) throws ExecutionException, InterruptedException {
#         try (var orderDispatcher = new KafkaDispatcher<Order>()) {
#             var email = Math.random() + "@email.com";
#             for (var i = 0; i < 10; i++) {
#
#                 var orderId = UUID.randomUUID().toString();
#                 var amount = new BigDecimal(Math.random() * 5000 + 1);
#
#                 var id = new CorrelationId(NewOrderMain.class.getSimpleName());
#
#                 var order = new Order(orderId, amount, email);
#                 orderDispatcher.send("ECOMMERCE_NEW_ORDER", email,
#                         id, order);
#             }
#         }
#     }
#
# }
