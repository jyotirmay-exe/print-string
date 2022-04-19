<h1>An awesome way to print strings in Python</h1>

Just a fun project to print strings with a twist.

It basically uses the in-built `random` module's `randint` method to generate random numbers within the printable ASCII characters' charcode range and matches it with a string given as input. This continues till it gets the right characters at the right indexes before terminating.

The current version of the project is not capable enough to handle anything other than ASCII codes `65-122` (both inclusive) - which includes ```A-Z, [, \, ], ^, _, `, a-z and 32 (blank space)```. Entering anything beyond this will lead to it getting stuck at that position.

Change `time.sleep()` value in `src/main.py` to `1` for more fun 😉

**Python version 3.5+ needed, although works with any Python 3 version but may cause trouble at times**