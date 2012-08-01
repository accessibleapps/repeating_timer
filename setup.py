from distutils.core import setup

__version__ = 0.1
__doc__ = """Simple module with a Repeating Timer class for scheduling something to happen over and over again."""
__author__ = "Christopher Toth"

setup(
 name = 'repeating_timer',
 version = str(__version__),
 author = __author__,
 author_email = 'q@q-continuum.net',
 description = __doc__,
 py_modules = ["repeating_timer"],
 classifiers = [
  'Development Status :: 3 - Alpha',
  'Intended Audience :: Developers',
  'Programming Language :: Python',
  'License :: OSI Approved :: MIT License',
  'Topic :: Software Development :: Libraries',
 ],
)
