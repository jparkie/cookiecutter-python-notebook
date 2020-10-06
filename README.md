# cookiecutter-python-notebook

Cookiecutter template for a Jupyter Python 3 notebook.

## Requirements

### cookiecutter

Please follow instructions at https://cookiecutter.readthedocs.io/en/latest/installation.html.

#### pip

```
pip install cookiecutter
```

#### Homebrew (macOS)

```
brew install cookiecutter
```
#### Ubuntu

```
sudo apt-get install cookiecutter
```

## Installation

Please execute the following command to create a new Jupyter Python 3 notebook.

```
cookiecutter git@github.com:jparkie/cookiecutter-python-notebook.git
```

### Configurations

```
> cookiecutter git@github.com:jparkie/cookiecutter-python-notebook.git
project [example]:
project_slug [example]:
version [0.1.0]:
description [N/A]:
author_email [N/A]:
```

## Features

### Dockerfile + Makefile

- A `Dockerfile.develop` with Python 3.7, tox, and tox-venv is provided to self-contain the project.
- A `Makefile` is provided to execute various project commands within a Docker container.

#### Makefile

```
> make help
Welcome to {{cookiecutter.project}}!

This project is preferably managed with Docker. Please have Docker installed.

    uninstall-docker
        Remove Docker image cookiecutter_py37_python_notebook
    init-hooks
        Initialize project hooks
    init
        Initialize project directory
    interactive
        Start an interactive, Dockerized bash session
    jupyter
        Start an interactive, Dockerized Jupyter session
    python PYTHON_ARGS="--version"
        Execute Python within a Docker container
    test TEST_ARGS="*"
        Test the Python project
    pre-commit
        Execute pre-commit hooks
        See https://pre-commit.com/ for more information
    clean
        Clean the Python project
```

### Project Structure

```
> tree -a ./
./
├── .dockerignore
├── .gitignore
├── .gitkeep
├── .pre-commit-config.yaml
├── Dockerfile.develop
├── Makefile
├── README.md
├── data
│   ├── .gitkeep
│   ├── external
│   │   └── .gitkeep
│   ├── interim
│   │   └── .gitkeep
│   ├── processed
│   │   └── .gitkeep
│   └── raw
│       └── .gitkeep
├── notebooks
│   └── .gitkeep
├── references
├── reports
│   ├── .gitkeep
│   └── figures
│       └── .gitkeep
├── requirements-dev.txt
├── requirements.txt
├── setup.py
├── src
│   └── __init__.py
└── tox.ini

10 directories, 20 files
```