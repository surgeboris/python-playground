venv=PATH=./bin:$$PATH PYTHONPATH=./lib/python3.8/site-packages:$$PYTHONPATH

all:
	make test_only

measure:
	python measure.py
test:
	${venv} pytest -v
test_watch:
	${venv} ptw -- -v
test_only:
	${venv} ptw -- -v -m only
