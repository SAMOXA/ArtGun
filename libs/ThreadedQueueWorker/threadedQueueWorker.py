import queue
import logging
import threading


def request_worker_thread(in_queue, out_queue, worker_fn):
    while True:
        req = in_queue.get()
        if req is None:
            break
        out_queue.put(worker_fn(req))


def response_worker_thread(out_queue, done_fn):
    while True:
        resp = out_queue.get()
        if resp is None:
            break
        done_fn(resp)


class ThreadedQueueWorker:
    thread_started = False

    def __init__(self, worker_fn, done_fn):
        self.out_queue = queue.Queue()
        self.in_queue = queue.Queue()
        self.worker_fn = worker_fn
        self.done_fn = done_fn
        self.requestThread = threading.Thread(target=request_worker_thread, args=[self.in_queue, self.out_queue, self.worker_fn])
        self.responseThread = threading.Thread(target=response_worker_thread, args=[self.out_queue, self.done_fn])

    def __del__(self):
        if self.thread_started is True:
            self.stop_threads()

    def start_threads(self):
        self.thread_started = True
        self.requestThread.start()
        self.responseThread.start()

    def stop_threads(self):
        self.in_queue.put(None)
        self.requestThread.join()
        self.out_queue.put(None)
        self.responseThread.join()
        self.thread_started = False

    def push(self, req):
        self.in_queue.put(req)
