import unittest
from unittest.mock import patch
from broker import Receiver, Sender
from configuration import QUEUE_NAME


class TestReceiver(unittest.TestCase):
    @patch('broker.pika')
    def test_receiver(self, mock_pika):
        r = Receiver()
        r.connect()

        r.queue = QUEUE_NAME
        r.declare_queue(QUEUE_NAME)
        is_cons = r.consume()
        assert mock_pika.is_called_once()
        self.assertTrue(is_cons, 'Mock queue not consumed')

    @patch('broker.pika')
    def test_sender(self, mock_pika):
        s = Sender()
        s.connect()
        s.queue = QUEUE_NAME
        s.declare_queue(QUEUE_NAME)
        s.publish('routing_key', 'hello')


if __name__ == '__main__':
    unittest.main()
