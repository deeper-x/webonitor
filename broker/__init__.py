import pika
import logging
from configuration import RABBITMQ_HOST


class Receiver:
    def __init__(self):
        self.__connection = None
        self.__queue = None

        self.channel = None

    @property
    def queue(self) -> str:
        """
        Queue name accessor
        :return: string
        """
        return self.__queue

    @queue.setter
    def queue(self, queue_name: str) -> None:
        """
        Queue name mutator
        :param queue_name: string
        :return: None
        """
        self.__queue = queue_name

    def connect(self) -> None:
        """
        Connection
        :return: None
        """
        params = pika.ConnectionParameters(host=RABBITMQ_HOST)
        self.__connection = pika.BlockingConnection(parameters=params)

    def declare_queue(self, name: str) -> bool:
        """
        Queue declaration
        :param name: string
        :return: bool
        """
        if self.__connection.channel():
            self.channel = self.__connection.channel()
            self.channel.queue_declare(name)
            return True

        return False

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
            self.channel.basic_consume(queue=self.__queue,
                                       on_message_callback=self.callback,
                                       auto_ack=True
                                       )
            self.channel.start_consuming()
            return True

        return False
