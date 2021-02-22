from setuptools import setup, find_packages

req_tests = ["pytest"]
req_lint = ["flake8", "flake8-docstrings"]
req_dev = req_tests + req_lint

setup_options = {
    "name": "dd",
    "version": "0.0.1",
    "packages": find_packages(),
    "python_requires": ">=3.8",
    "install_requires": [],
    "extras_require": {
        "tests": req_tests,
        "lint": req_lint,
        "dev": req_dev
    },
    "package_dir": {"": "."},
}

setup(**setup_options)
