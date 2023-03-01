BLACK_OPTIONS=--line-length 120
ISORT_OPTIONS=--line-length 120 --profile black

format:
	isort $(ISORT_OPTIONS) .
	black $(BLACK_OPTIONS) .

run:
	pipenv run python main.py