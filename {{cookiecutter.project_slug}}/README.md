# {{cookiecutter.project}}

{{cookiecutter.description}}

## Makefile

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

## Configuration Files

- [`Dockerfile.develop`](https://docs.docker.com/engine/reference/builder/) - Configures a Docker container used for development.
- [`Makefile`](https://www.gnu.org/software/make/) - Simplifies various project management processes into `make` targets.
- [`requirements.txt`](https://pip.pypa.io/en/stable/user_guide/) - List of dependencies for running the notebooks.
- [`requirements-dev.txt`](https://pip.pypa.io/en/stable/user_guide/) - List of dependencies for developing the notebooks.
- [`tox.ini`](https://tox.readthedocs.io/en/latest/) - Configures and builds a consistent environment for continuous integration and coverage checks.

## Contact

**Email**: [{{cookiecutter.author_email}}](mailto:{{cookiecutter.author_email}})

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [jparkie/cookiecutter-python-notebook](https://github.com/jparkie/cookiecutter-python-notebook) project template.
