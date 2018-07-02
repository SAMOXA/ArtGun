from unittest import TestCase
from interfaces.messages.baseMsg import BaseMsg
from interfaces.messages.baseMsg import BaseMsgFieldNotExist


class TestLibThreadedQueueWorker(TestCase):
    def test_interface_msg_baseMsg_simple(self):
        msg = BaseMsg('1', '2', 100)

        result = msg.get_field('source')
        self.assertEqual(result, '1')
        result = msg.get_field('destination')
        self.assertEqual(result, '2')
        result = msg.get_field('tag')
        self.assertEqual(result, 100)
        result = msg.get_field('base_version')
        self.assertEqual(result, '0.1')

    def test_interface_msg_baseMsg_field_not_exist(self):
        msg = BaseMsg('1', '2', 100)

        try:
            msg.get_field('field_not_exist')
            self.assertRaises(Exception)
        except BaseMsgFieldNotExist as detail:
            self.assertEqual(detail.field, 'field_not_exist')
