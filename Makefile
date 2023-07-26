#!make

SHELL := /bin/bash

build:
	@tailwindcss -i ./static/src/main.css -o ./static/dist/main.css --minify

runserver: build
	@python app.py
	
pre-commit:
	@pre-commit run --all-files
