===================================
A backdoor for Tornado applications
===================================

Having a Python interative interpreter running alongside you application
can come useful for debugging. This module runs a Python interactive
interpreter over a TCP connection, where multiple clients can connect and
which does not block the server from handling requests.

Source code is on `GitHub <http://github.com/saghul/tornado-backdoor>`_.


Using it
========

Check `backdoor.py` located in the examples directory. It will run a
backdoor server on port 1234. You can connect to it using netcat
as follows:

::

    nc localhost 1234


Author
======

Saúl Ibarra Corretgé <saghul@gmail.com>


License
=======

tornado-backdoor uses the MIT license, check LICENSE file.

