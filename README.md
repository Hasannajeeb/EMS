# ems

A tiny but scalable Event management system

License: MIT

## Basic Commands

### Type checks

Running type checks with mypy:

    $ mypy ems

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

TODO: Unit Test, Integration Test and End to End tests need to be implemented

TODO: CICD pipeline setup to increase the confidence of development on each merge to the main branch

TODO: pre-commit hooks needs to be setup to run test basic checks each time the developers push something to the repo

#### Running tests with pytest

    $ pytest


### documentation can be accessed locally using the following url
http://localhost:8000/api/docs/