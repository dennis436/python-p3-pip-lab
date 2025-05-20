import sys
import requests
import pytest

def python_version():
    return sys.version_info  # Returns something like (3, 8, 13, 'final', 0)

def requests_version():
    return requests.__version__  # Returns a string like '2.27.1'

def pytest_version():
    return pytest.__version__  # Returns a string like '7.1.3'
