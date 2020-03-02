import pika
import logging
from configuration import RABBITMQ_HOST


class QueueManager:
    def __init__(self):
        self._connection = None
        self._queue = None

        self.channel = None

    @property
    def queue(self) -> str:
        """
        Queue name accessor
        :return: string
        """
        return self._queue

    @queue.setter
    def queue(self, queue_name: str) -> None:
        """
        Queue name mutator
        :param queue_name: string
        :return: None
        """
        self._queue = queue_name

    def connect(self) -> None:
        """
        Connection
        :return: None
        """
        params = pika.ConnectionParameters(host=RABBITMQ_HOST)
        self._connection = pika.BlockingConnection(parameters=params)

    def declare_queue(self, name: str) -> bool:
        """
        Queue declaration
        :param name: string
        :return: bool
        """
        if self._connection.channel():
            self.channel = self._connection.channel()
            self.channel.queue_declare(name)
            return True

        return False


class Receiver(QueueManager):
    """
    Defines rabbitmq receiver
    """
    def __init__(self):
        super().__init__()

    def callback(self, method: str, props: str, body: str):
        """
        callback declared in
        :param method: string
        :param props: string
        :param body: strin
        :return: None
        """
        logging.info(f'logging callback {body}')

    def consume(self) -> bool:
        """
        Start consuming
        :return: bool
        """
        if self.channel:
            logging.info('Start consuming....')
            self.channel.basic_consume(queue=self._queue,
                                       on_message_callback=self.callback,
                                       auto_ack=True
                                       )
            self.channel.start_consuming()
            return True

        return False


class Sender(QueueManager):
    def __init__(self):
        super().__init__()

    def publish(self, routing_key: str, body: str):
        """
        Publish content on givent routing key
        :param routing_key: str
        :param body: str
        :return: None
        """
        if self.channel:
            self.channel.basic_publish(exchange='',
                                       routing_key=routing_key,
                                       body=body)
            self._connection.close()
            return True

        return False
