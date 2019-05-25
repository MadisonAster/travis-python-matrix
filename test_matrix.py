import os
import platform

import distro


def test_matrix() -> None:

    python_implementation = platform.python_implementation()
    python_version = platform.python_version()
    system = platform.system()

    if system == "Darwin":
        system = "macOS"
        version = platform.mac_ver()[0]
        if version.startswith("10.14"):
            version += " (Mojave)"
        elif version.startswith("10.13"):
            version += " (High Sierra)"
        elif version.startswith("10.12"):
            version += " (Sierra)"
        else:
            assert False, version
    elif system == "Windows":
        version = platform.win32_ver()
    elif system == "Linux":
        system = distro.name()
        version = distro.version(pretty=True)
    else:
        assert False, version

    name = "{} {} on {} {}".format(
        platform.python_implementation(),
        platform.python_version(),
        system, version,
    )

    assert name == os.environ["TRAVIS_JOB_NAME"]
