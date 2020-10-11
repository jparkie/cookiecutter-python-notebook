PYTHON_ARGS =

TEST_ARGS =

DOCKER_BASE = docker run \
	--volume $$(pwd):/repo \
	--volume /var/run/docker.sock:/var/run/docker.sock \
	--publish 8888:8888

DOCKER_RUN = $(DOCKER_BASE) \
	cookiecutter_py37_python_notebook

DOCKER_INTERACTIVE = $(DOCKER_BASE) \
	--interactive \
	--tty \
	--entrypoint bash \
	cookiecutter_py37_python_notebook

.docker/cookiecutter_py37_python_notebook: Dockerfile.develop
	docker build --tag cookiecutter_py37_python_notebook --file Dockerfile.develop .
	mkdir -p .docker
	touch .docker/cookiecutter_py37_python_notebook

help:
	@echo "Welcome to {{cookiecutter.project}}!"
	@echo ""
	@echo "This project is preferably managed with Docker. Please have Docker installed."
	@echo ""
	@echo "    uninstall-docker"
	@echo "        Remove Docker image cookiecutter_py37_python_notebook"
	@echo "    init-hooks"
	@echo "        Initialize project hooks"
	@echo "    init"
	@echo "        Initialize project directory"
	@echo "    interactive"
	@echo "        Start an interactive, Dockerized bash session"
	@echo "    jupyter"
	@echo "        Start an interactive, Dockerized Jupyter session"
	@echo "    python PYTHON_ARGS=\"--version\""
	@echo "        Execute Python within a Docker container"
	@echo "    test TEST_ARGS=\"*\""
	@echo "        Test the Python project"
	@echo "    pre-commit"
	@echo "        Execute pre-commit hooks"
	@echo "        See https://pre-commit.com/ for more information"
	@echo "    clean"
	@echo "        Clean the Python project"

uninstall-docker:
	rm -rf .docker
	docker rmi --force cookiecutter_py37_python_notebook

init-hooks:
	curl https://pre-commit.com/install-local.py | python -
	$(HOME)/bin/pre-commit install

init: .docker/cookiecutter_py37_python_notebook
	$(DOCKER_RUN) tox -e venv

interactive: .docker/cookiecutter_py37_python_notebook
	$(DOCKER_INTERACTIVE)

jupyter: .docker/cookiecutter_py37_python_notebook
	$(DOCKER_INTERACTIVE) -c 'jupyter notebook --allow-root --ip=0.0.0.0'

python: .docker/cookiecutter_py37_python_notebook
	$(DOCKER_RUN) python3 $(PYTHON_ARGS)

test: .docker/cookiecutter_py37_python_notebook
	$(DOCKER_RUN) tox -- $(TEST_ARGS)

pre-commit:
	$(HOME)/bin/pre-commit run --all-files

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	rm -rf .tox

.PHONY: help uninstall-docker init-hooks init interactive jupyter python test pre-commit clean