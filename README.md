<div align=justify>

<div align=center>

Travis Python Matrix
====================

[![last updated](https://img.shields.io/github/last-commit/brandtbucher/travis-python-matrix.svg?label=updated&style=for-the-badge)](https://github.com/brandtbucher/travis-python-matrix)[![build status](https://img.shields.io/travis/com/brandtbucher/travis-python-matrix/master.svg?style=for-the-badge)](https://travis-ci.com/brandtbucher/travis-python-matrix)[![issues](https://img.shields.io/github/issues-raw/brandtbucher/travis-python-matrix.svg?label=issues&style=for-the-badge)](https://github.com/brandtbucher/travis-python-matrix/issues)

<br>

</div>

`.travis.yml` contains the necessary boilerplate to get consistent versions of `python` and `pip` executables on all three of Travis's supported operating systems. Simply add your own `script`, `install`, or other configurations in order to build and test cross-platform with minimal effort!

Supported Python Versions
-------------------------

- [X] CPython 3.7.3
- [X] CPython 3.6.8
- [X] CPython 3.5.2

Supported Operating Systems
----------------------------

*Unchecked boxes are disabled by default. They can be enabled by uncommenting them in `.travis.yml`.*

- [X] Ubuntu 16.04 (Xenial Xerus)
- [X] Windows Server 1803
- [X] macOS 10.14 (Mojave)
- [ ] macOS 10.13 (High Sierra)
- [ ] macOS 10.12 (Sierra)
 
Background
----------
 
This project was inspired by Steve Dower's talk at PyCon 2019, entitled ["Python on Windows is Okay, Actually"](https://www.youtube.com/watch?v=uoI57uMdDD4). I realized that I was one of the developers who hadn't really tried hard enough to run CI against Windows, because it seemed like too much work to be useful (and, as Steve notes at [23:45](https://youtu.be/uoI57uMdDD4?t=1425), I just *really didn't want to*).
 
Every solution I could find on the internet for true, cross-platform CI had drawbacks in that it either:

- Required me to use multiple CI providers.
- Only supported one major Python version.
- Required ugly, opaque hacks and shell scripting to work around different `python` and `pip` invocations.
- Required lots of trial-and-error to set up properly.

I figured that this is the sort of problem that should only be solved once, and shared with everybody else. So, I decided to make a simple, drop-in Travis matrix for simple, consistent cross-platform CI for multiple Python versions. Within minutes of this repository going live, it had already found several sneaky, Windows-only bugs in [a medium-sized project's quickstart guide](https://github.com/InvestmentSystems/static-frame/pull/51)!

Enjoy!

</div>
