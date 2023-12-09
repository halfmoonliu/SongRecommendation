install:
<<<<<<< HEAD
	brew install portaudio
	pip install --upgrade pip &&\
		pip install -r requirements.txt
||||||| merged common ancestors
	pip install --upgrade pip &&\
		pip install -r requirements.txt
=======
	pip install --upgrade pip && pip install -r requirements.txt
>>>>>>> abc71dbbf804cf99d2a7d987a01155e36d2919d9

test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py

format:
	black *.py 

lint:
	# Disable comment to test speed
	# pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py
	# Ruff linting is 10-100X faster than pylint
	ruff check *.py mylib/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	# Deploy goes here

all: install lint test format deploy

job:
	python run_job.py