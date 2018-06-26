from unittest import TestCase
from libs.ThreadedQueueWorker.threadedQueueWorker import ThreadedQueueWorker


class TestLibThreadedQueueWorker(TestCase):
    def test_lib_threadedQueueWorker_simple(self):
        self.output = 0

        def worker_fn(params):
            params.output += 1
            return params

        def done_fn(resp):
            resp.output += 1

        worker = ThreadedQueueWorker(worker_fn, done_fn)
        worker.start_threads()
        worker.push(self)
        worker.stop_threads()

        self.assertEqual(self.output, 2)

    def test_lib_threadedQueueWorker_add_before_run(self):
        self.output = 0

        def worker_fn(params):
            params.output += 1
            return params

        def done_fn(resp):
            resp.output += 1

        worker = ThreadedQueueWorker(worker_fn, done_fn)
        worker.push(self)
        worker.start_threads()
        worker.stop_threads()

        self.assertEqual(self.output, 2)

    def test_lib_threadedQueueWorker_multiple(self):
        self.output = 0

        def worker_fn(params):
            params.output += 1
            return params

        def done_fn(resp):
            resp.output += 1

        worker = ThreadedQueueWorker(worker_fn, done_fn)
        worker.push(self)
        worker.push(self)
        worker.push(self)
        worker.push(self)
        worker.push(self)
        worker.start_threads()
        worker.stop_threads()

        self.assertEqual(self.output, 10)

    def test_lib_threadedQueueWorker_delay(self):
        self.output = 0

        def worker_fn(params):
            params.output += 1
            return params

        def done_fn(resp):
            resp.output += 1

        worker = ThreadedQueueWorker(worker_fn, done_fn)
        worker.push(self)
        worker.push(self)
        worker.push(self)
        worker.push(self)
        worker.push(self)
        worker.start_threads()
        worker.stop_threads()

        self.assertEqual(self.output, 10)