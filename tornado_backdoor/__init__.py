
__all__ = ('BackdoorServer')

import functools
import sys

from code import InteractiveConsole
from cStringIO import StringIO

from tornado.netutil import TCPServer


class BackdoorShell(InteractiveConsole):

    def __init__(self, stream):
        InteractiveConsole.__init__(self)
        self._stream = stream
        self.ps1 = getattr(sys, 'ps1', '>>> ')
        self.ps2 = getattr(sys, 'ps2', '... ')
        # Write banner
        self.write('Python %s on %s (%s)\n' % (sys.version, sys.platform, self.__class__.__name__))
        self.write(self.ps1)

    def push(self, line):
        try:
            more = InteractiveConsole.push(self, line)
        except KeyboardInterrupt:
            self.write('\nKeyboardInterrupt\n')
            self.resetbuffer()
            more = False
        if more:
            self.write(self.ps2)
        else:
            self.write(self.ps1)

    def runcode(self, code):
        fake_stdout = StringIO()
        sys.stdout = fake_stdout
        sys.stderr = fake_stdout
        try:
            InteractiveConsole.runcode(self, code)
        finally:
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__
            self.write(fake_stdout.getvalue())

    def write(self, data):
        self._stream.write(data)


class Connection(object):

    def __init__(self, stream, address):
        self.address = address
        self.shell = BackdoorShell(stream)
        self.stream = stream

        self._read_line()

    def _read_line(self):
        self.stream.read_until('\n', self._handle_read)

    def _handle_read(self, data):
        self.shell.push(data.rstrip('\n'))
        self._read_line()


class BackdoorServer(TCPServer):
    connections = []

    def handle_stream(self, stream, address):
        conn = Connection(stream, address)
        close_cb = functools.partial(self._connection_closed, conn)
        stream.set_close_callback(close_cb)
        self.connections.append(conn)

    def _connection_closed(self, connection):
        self.connections.remove(connection)

