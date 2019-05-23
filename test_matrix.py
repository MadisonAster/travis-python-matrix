import os
import platform
import sys


NAME = os.environ["TRAVIS_JOB_NAME"]

PLATFORMS = {
    "darwin": "macOS",
    "linux": "Ubuntu",
    "win32": "Windows",
}


def test_platform() -> None:
    assert PLATFORMS[sys.platform] in NAME


def test_python_implementation() -> None:
    assert platform.python_implementation() in NAME


def test_python_version() -> None:
    assert platform.python_version() in NAME
