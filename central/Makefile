format:
	pipenv run black .
	pipenv run isort .

run:
	make format
	PYTHONPATH=. PYTHONDONTWRITEBYTECODE=1 pipenv run python central/main.py

build:
	make format
	docker build -t foo . && docker run -it foo

install:
	pipenv install --dev

test:
	pipenv run pytest
