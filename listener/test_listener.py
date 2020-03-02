import unittest
from configuration import fake_bucket, ADD_EVENT, DEL_EVENT, MOD_EVENT, CUT_EVENT
from unittest.mock import patch
from listener import Listen


class TestListener(unittest.TestCase):
    @patch('listener.Observer')
    def test_listen_changes(self, mock_observer):
        dir_listener = Listen()

        created = dir_listener.observe(fake_bucket, ADD_EVENT)
        self.assertTrue(created, 'File creation error')

        deleted = dir_listener.observe(fake_bucket, DEL_EVENT)
        self.assertTrue(deleted, 'File deletion error')

        modified = dir_listener.observe(fake_bucket, MOD_EVENT)
        self.assertTrue(modified, 'File modification error')

        moved = dir_listener.observe(fake_bucket, CUT_EVENT)
        self.assertTrue(moved, 'File cutting error')

        weird_action = dir_listener.observe(fake_bucket, 'boo')
        self.assertFalse(weird_action, 'Non existent action error')


if __name__ == '__main__':
    unittest.main()
