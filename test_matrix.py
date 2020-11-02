import os
import platform
import struct

import distro

import numpy


def test_matrix() -> None:
    print('test_matrix!!!!!!!!!!!')
    python_implementation = platform.python_implementation()
    python_version = platform.python_version()
    architecture = struct.calcsize("P") * 8
    system = platform.system()

    if system == "Darwin":
        system = "macOS"
        version = platform.mac_ver()[0]
        if version.startswith("10.15"):
            version = "10.15 (Catalina)"
        elif version.startswith("10.14"):
            version = "10.14 (Mojave)"
        elif version.startswith("10.13"):
            version = "10.13 (High Sierra)"
        elif version.startswith("10.12"):
            version = "10.12 (Sierra)"
        else:
            assert False, version
        assert architecture == 64, architecture
    elif system == "Windows":
        version = "{} ({}-bit)".format(
            platform.win32_ver()[0],
            architecture,
        )
    elif system == "Linux":
        system = distro.name()
        version = distro.version()
        if system == "Ubuntu":
            if version == "16.04":
                version += " (Xenial Xerus)"
            else:
                assert False, version
        else:
            assert False, system
        assert architecture == 64, architecture
    else:
        assert False, system