#!make

SHELL := /bin/bash

confirm-erase:
	@echo "This operation will erase stored data. Proceed? (yN) " && read ans && [ $${ans:-N} = y ]

reset: confirm-erase
	@docker compose down -v
	@docker compose up -d --build

build:
	@tailwindcss -i ./flask_app/static/src/main.css -o ./flask_app/static/dist/main.css --minify

runserver: build
	@flask run --debug

pre-commit:
	@pre-commit run --all-files
