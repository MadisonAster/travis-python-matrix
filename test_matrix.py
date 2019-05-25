import os
import platform


def test_matrix() -> None:

    python_implementation = platform.python_implementation()
    python_version = platform.python_version()
    system = platform.system()
    version = platform.version()

    if system == "Darwin":
        system = "macOS"
        version = platform.mac_ver()[0]
        if version.startswith("10.14"):
            alias = "Mojave"
        elif version.startswith("10.13"):
            alias = "High Sierra"
        elif version.startswith("10.12"):
            alias = "Sierra"
    elif system == "Windows":
        alias = platform.win32_ver()
    else:
        alias = platform.release()


    name = "{} {} on {} {} ({})".format(
        platform.python_implementation(),
        platform.python_version(),
        system, version, alias,
    )

    assert name == os.environ["TRAVIS_JOB_NAME"], name
