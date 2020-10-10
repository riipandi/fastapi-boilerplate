# FastAPI Boilerplate
Boilerplate for FastAPI using Pipenv and Docker.

## Development Requirements
- Python >= 3.7
- Pipenv >= 2020.6.2

## Quick Start
```sh
# Development
pipenv shell
pipenv install
pipenv run start
pipenv run test

# Using Makefile
make install

# Running localhost
make run

# Deploy using Docker
make deploy

# Run test
make test
```

## API Documentation
1. Swagger Documentation: http://localhost:5000/docs
2. Redocs Documentation: http://localhost:5000/redoc

## Project structure
Files related to application are in the `app` or `tests` directories. Application parts are:

    app
    ├── core             - application configuration, startup events, logging, routes.
    ├── db               - database related.
    │   └── migration    - database migration.
    ├── models           - models for this application.
    ├── resources        - application endpoint / controllers.
    ├── services         - logic that is not just crud related.
    ├── static           - static files directory.
    └── main.py          - FastAPI application creation and configuration.
    │
    tests                - pytest

> For detailed explanation on how things work, check out [FastAPI docs](https://fastapi.tiangolo.com/).

## LICENSE
```
The MIT License (MIT)

Copyright (c) Aris Ripandi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```
