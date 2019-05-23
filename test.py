import os
import sys


IMPLEMENTATIONS = {
    "cpython": "CPython",
}

PLATFORMS = {
    "darwin": "macOS",
    "linux": "Ubuntu",
    "win32": "Windows",
}


def test_platform():
    assert PLATFORMS[sys.platform] in os.environ["TRAVIS_JOB_NAME"]


def test_python_version():
    assert '.'.join(sys.version_info[:3]) in os.environ["TRAVIS_JOB_NAME"]


def test_python_implementation():
    assert IMPLEMENTATIONS[sys.implementation.name] in os.environ["TRAVIS_JOB_NAME"]
