Repeating Timer: A simple threaded repeating timer, because the stdlib doesn't have one
==========================================================================================

For whatever reason, threading.Timer doesn't allow you to call the same function more than once. So, here you go.

.. code-block:: pycon

    >>> t = RepeatingTimer(30.0, to_call, *args, **kwargs)

