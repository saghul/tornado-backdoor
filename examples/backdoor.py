
import signal

from tornado.ioloop import IOLoop
from tornado_backdoor import BackdoorServer


def handle_SIGINT(signum, frame):
    io_loop = IOLoop.instance()
    io_loop.add_callback(io_loop.stop)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, handle_SIGINT)
    server = BackdoorServer()
    server.listen(1234)
    IOLoop.instance().start()

