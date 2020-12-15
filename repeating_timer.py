from logging import getLogger
logger = getLogger("repeating_timer")

import threading

class RepeatingTimer(threading.Thread):
 """Call a function after a specified number of seconds, it will then repeat again after the specified number of seconds
    Note: If the function provided takes time to execute, this time is NOT taken from the next wait period

 t = RepeatingTimer(30.0, f, *args, **kwargs)
 t.start()
 t.cancel() # stop the timer's actions
 """

 def __init__(self, interval, function, daemon=True, *args, **kwargs):
  threading.Thread.__init__(self)
  self.daemon = daemon
  self.interval = interval
  self.function = function
  self.args = args
  self.kwargs = kwargs
  self.finished = threading.Event()
  self.running = False


 def cancel(self):
  """Stop the timer if it hasn't finished yet"""
  self.finished.set()
 stop = cancel

 def run(self):
  logger.debug("Starting timer %r which will run every %r seconds", self.ident, self.interval)
  self.running = True
  while not self.finished.is_set():
   self.finished.wait(self.interval)
   if self.finished.is_set():  #In case someone has canceled while waiting
    self.running = False
    break
   try:
    self.function(*self.args, **self.kwargs)
   except:
    logger.exception("Error calling function %r with args %r and kwargs %r", self.function, args, kwargs)
 logger.debug("Timer %r terminated", self.ident)
