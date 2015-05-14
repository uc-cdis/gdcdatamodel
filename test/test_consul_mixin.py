from zug.consul_mixin import ConsulMixin
from unittest import TestCase


class ConsulMixinTest(TestCase):
    def setUp(self):
        self.worker = ConsulMixin()
        self.worker.key = 'id1'

    def tearDown(self):
        self.worker.cleanup()

    def test_acquire_lock(self):
        self.worker.start_consul_session(delay='0s')
        self.assertTrue(self.worker.get_consul_lock())

    def test_key_set(self):
        self.worker.start_consul_session(delay='0s')
        self.worker.get_consul_lock()
        self.worker.consul_key_set({'test': 'value'})
        self.worker.set_consul_state('downloading')
        self.assertEqual(self.worker.consul.kv[self.worker.consul_key],
                         {'test': 'value', 'state': 'downloading'})

    def test_key_set_without_locking(self):
        self.worker.key = 'id1'
        self.assertFalse(self.worker.consul_key_set('value'))
        self.assertFalse(self.worker.set_consul_state('downloading'))

    def test_acquire_locked_key(self):
        worker2 = ConsulMixin()
        worker2.key = 'id1'
        worker2.start_consul_session(delay='0s')
        self.assertTrue(worker2.get_consul_lock())
        self.assertFalse(self.worker.get_consul_lock())
        worker2.cleanup()
