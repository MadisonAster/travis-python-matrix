<div align=justify>

<div align=center>

Travis Python Matrix
====================

[![last updated](https://img.shields.io/github/last-commit/brandtbucher/travis-python-matrix.svg?label=updated&style=for-the-badge)](https://github.com/brandtbucher/travis-python-matrix)[![build status](https://img.shields.io/travis/com/brandtbucher/travis-python-matrix/master.svg?style=for-the-badge)](https://travis-ci.com/brandtbucher/travis-python-matrix)[![issues](https://img.shields.io/github/issues-raw/brandtbucher/travis-python-matrix.svg?label=issues&style=for-the-badge)](https://github.com/brandtbucher/travis-python-matrix/issues)

<br>

</div>

The snippet below contains the necessary boilerplate to get consistent versions of `python` and `pip` executables on all three of Travis's supported operating systems. Simply add your own `script`, `install`, or other configurations in order to build and test cross-platform with minimal effort!

```yml
# https://github.com/brandtbucher/travis-python-matrix

# CPython 3.7.3 / CPython 3.6.8 / CPython 3.5.2
# Ubuntu 16.04 (Xenial Xerus) / Windows 10 / macOS 10.14 (Mojave)

# Just comment out any matrix entries you don't need.

matrix:

  include:
  
    - name: CPython 3.7.3 on Ubuntu 16.04 (Xenial Xerus)
      language: python
      os: linux
      dist: xenial
      python: 3.7.3

    - name: CPython 3.6.8 on Ubuntu 16.04 (Xenial Xerus)
      language: python
      os: linux
      dist: xenial
      python: 3.6.8
      
    - name: CPython 3.5.2 on Ubuntu 16.04 (Xenial Xerus)
      language: python
      os: linux
      dist: xenial
      python: 3.5.2

    - name: CPython 3.7.3 on Windows 10
      language: shell
      os: windows
      before_install:
        - export PATH=/c/Python37:/c/Python37/Scripts:$PATH
        - choco install python --version 3.7.3

    - name: CPython 3.6.8 on Windows 10
      language: shell
      os: windows
      before_install:
        - export PATH=/c/Python36:/c/Python36/Scripts:$PATH
        - choco install python --version 3.6.8

    - name: CPython 3.5.2 on Windows 10
      language: shell
      os: windows
      before_install:
        - export PATH=/c/Python35:/c/Python35/Scripts:$PATH
        - choco install python --version 3.5.2.20161029

    - name: CPython 3.7.3 on macOS 10.14 (Mojave)
      language: shell
      os: osx
      osx_image: xcode10.2
      before_install:
        - export PATH=/Users/travis/.pyenv/shims:$PATH PYENV_VERSION=3.7.3
        - CFLAGS="-I$(xcrun --show-sdk-path)/usr/include" pyenv install $PYENV_VERSION

    - name: CPython 3.6.8 on macOS 10.14 (Mojave)
      language: shell
      os: osx
      osx_image: xcode10.2
      before_install:
        - export PATH=/Users/travis/.pyenv/shims:$PATH PYENV_VERSION=3.6.8
        - CFLAGS="-I$(xcrun --show-sdk-path)/usr/include" pyenv install $PYENV_VERSION

    - name: CPython 3.5.2 on macOS 10.14 (Mojave)
      language: shell
      os: osx
      osx_image: xcode10.2
      before_install:
        - export PATH=/Users/travis/.pyenv/shims:$PATH PYENV_VERSION=3.5.2
        - CFLAGS="-I$(xcrun --show-sdk-path)/usr/include" pyenv install $PYENV_VERSION

# Change anything below to suit your CI needs.
# Python and pip exectuables are just named "python" and "pip" on all platforms!

install: pip --version

script: python --version
```

Support
-------

Unchecked boxes aren't included in the above snippet. They can be copied-and-pasted from `.travis.yml`.

### Python Versions

- [X] CPython 3.7.3
- [ ] CPython 3.7.2
- [ ] CPython 3.7.1
- [ ] CPython 3.7.0
- [X] CPython 3.6.8
- [ ] CPython 3.6.7
- [ ] CPython 3.6.6
- [ ] CPython 3.6.5
- [ ] CPython 3.6.4
- [ ] CPython 3.6.3
- [X] CPython 3.5.2

### Operating Systems

- [X] Ubuntu 16.04 (Xenial Xerus)
- [X] Windows 10
- [X] macOS 10.14 (Mojave)
- [ ] macOS 10.13 (High Sierra)
- [ ] macOS 10.12 (Sierra)
 
Background
----------
 
This project was inspired by Steve Dower's talk at PyCon 2019, entitled ["Python on Windows is Okay, Actually"](https://www.youtube.com/watch?v=uoI57uMdDD4). I quickly realized that I was one of the engineers who hadn't really tried hard enough to run CI against Windows, because it seemed like too much work to be useful (and, as Steve notes at [23:45](https://youtu.be/uoI57uMdDD4?t=1425), I just *really didn't want to*).
 
Every solution I could find on the internet for true, cross-platform CI had drawbacks in that they either:

- Required me to use multiple CI providers.
- Only supported one Python minor version, or different patch versions per platform.
- Needed ugly, opaque hacks and shell scripting to work around different `python` and `pip` invocations.
- Took lots of trial-and-error to set up properly.

I figured that this was the sort of problem that should only be solved once, then shared with everybody else. So, I decided to make a drop-in Travis matrix for simple, consistent cross-platform CI against multiple Python versions. Within minutes of this repository going live, it had already found several sneaky, Windows-only bugs in [a medium-sized project's quickstart guide](https://github.com/InvestmentSystems/static-frame/pull/51)!

Enjoy!

</div>
