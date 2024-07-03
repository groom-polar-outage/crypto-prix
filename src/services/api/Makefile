version = $(shell poetry version -s)
env:
	poetry install

env-update:
	poetry update

fmt:
	poetry run ruff check --fix
	poetry run ruff format

build-push:
	docker build --tag liningunplugthespian/crypto-prix-api:$(version) .
	docker push liningunplugthespian/crypto-prix-api:$(version)