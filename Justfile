install:
    poetry install

lint: install
    poetry run ruff format fileshare
    poetry run ruff check --fix fileshare

run-dev: install
    poetry run python fileshare/main.py

run-prod: install
    poetry run gunicorn -b :5555 fileshare.main:app
