BLACK_OPTIONS=--line-length 120
ISORT_OPTIONS=--line-length 120 --profile black

format:
	isort $(ISORT_OPTIONS) .
	black $(BLACK_OPTIONS) .

run:
	pipenv run python engine/main.py

test:
	pipenv run python -m unittest discover tests

load_test_data:
	pipenv run python scripts/load_trade_data