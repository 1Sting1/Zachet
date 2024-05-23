import unittest
from stack_operations import stack_operations
from stack_label_updater import stack_label_updater
from mock_label import mock_label

class TestObserverPattern(unittest.TestCase):
    def test_observer_updates_label(self):
        # Создаем экземпляр stack_operations
        stack_ops = stack_operations()
        mock_label_cl = mock_label()

        label_updater = stack_label_updater(mock_label_cl, stack_ops)
        self.assertEqual(mock_label_cl.text, "")
        stack_ops.push(5, None)
        stack_ops.push(10, None)

        self.assertEqual(mock_label_cl.text, "5, 10")

        stack_ops.delfromstack()

        self.assertEqual(mock_label_cl.text, "5")