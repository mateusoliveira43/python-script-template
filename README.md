# CLY?! Build CLIs without dependencies!

[![Continuos Integration](https://github.com/mateusoliveira43/cly/actions/workflows/ci.yml/badge.svg)](https://github.com/mateusoliveira43/cly/actions)
[![Continuos Delivery](https://github.com/mateusoliveira43/cly/actions/workflows/cd.yml/badge.svg)](https://github.com/mateusoliveira43/cly/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=mateusoliveira43_python-cli-script-template&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=mateusoliveira43_python-cli-script-template)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
![Python versions](https://img.shields.io/badge/Python-3.7%20|%203.8%20|%203.9%20|%203.10%20|%203.11-success)
![PyPy versions](https://img.shields.io/badge/PyPy-3.8%20|%203.9-success)

- [Arquivo README em português](docs/README_PT.md)

A framework to create command line interfaces with Python, using only Python's standard libraries, like [argparse](https://docs.python.org/3/library/argparse.html).

Check the project's documentation [here](https://mateusoliveira43.github.io/cly/).

## Requirements

To use (or contribute to) the framework, it is necessary the following tools:

- [Python](https://wiki.python.org/moin/BeginnersGuide/Download) 3.7 or higher

## Development

Choose one of the next sections to setup your development environment.

### Python

To create a virtual environment, run
```
python3 -m venv .venv
```

To activate the virtual environment, run
```
source .venv/bin/activate
```

To install the framework's development requirements in the virtual environment, run
```
pip install -r requirements/dev.txt
```

To add the framework's tools to the path, run
```
pip install -e .
```

To deactivate the virtual environment, run `deactivate`.

Run the commands of the following sections with the virtual environment active.

### Poetry

To install the framework's development requirements in a virtual environment, run
```
poetry install
```

To activate the virtual environment, run
```
poetry shell
```
To deactivate the virtual environment, run `CTRL+D` or `exit`.

To update the requirements file, run
```
poetry export --format requirements.txt --output requirements/dev.txt --with dev
```

Run the commands of the following sections with the virtual environment active.

### Docker

To connect to project's Docker container shell, run
```
docker/run.sh
```
To exit the container's shell, run `CTRL+D` or `exit`.

To run Dockerfile linter, run
```
docker/lint.sh
```

To run Docker image security vulnerability scan, run
```
docker/scan.sh
```
It is needed to have an account in [Docker Hub](https://hub.docker.com/).

To remove the project's containers, images, volumes and networks, run
```
docker/down.sh
```

To change Docker configuration, change the variables in `.env` file.

Run the commands of the following sections in the container's shell.

## Quality

The quality measures of the framework are reproduced by the continuos integration (CI) pipeline of the project. CI configuration in [`.github/workflows/ci.yml`](.github/workflows/ci.yml) file.

### Tests

To run tests and coverage report, run
```
pytest
```

To see the html report, check the `tests/coverage-results/htmlcov/index.html` file generated by the command.

Tests and coverage configuration in [`pyproject.toml`](pyproject.toml) file.

### Type checking

To run Python type checker, run
```
mypy .
```

Python type checker configuration in [`pyproject.toml`](pyproject.toml) file.

### Linter

To run Python linter, run
```
prospector
prospector --profile tests/.prospector.yaml tests
```

Python linter configuration in [`.prospector.yaml`](.prospector.yaml) and [`tests/.prospector.yaml`](tests/.prospector.yaml) files.

### Code formatters

To check Python code imports format, run
```
isort --check --diff .
```

To format Python code imports, run
```
isort .
```

To check Python code format, run
```
black --check --diff .
```

To format Python code, run
```
black .
```

isort and black configuration in [`pyproject.toml`](pyproject.toml) file.

To check all repository's files format, run
```
ec -verbose
```

File format configuration in [`.editorconfig`](.editorconfig) file.

### Security vulnerability scanners

To check common security issues in Python code, run
```
bandit --recursive cly
```

To check known security vulnerabilities in Python dependencies, run
```
safety check --file requirements/dev.txt --full-report
```

### Documentation

To generate the project's documentation diagrams, run
```
(cd docs/images && python ../generate_diagrams.py)
```

To check the project's documentation generation, run
```
sphinx-apidoc --module-first --private --output-dir docs/modules cly
sphinx-build -W -T -v -n -a docs public
```

To generate the project's documentation, run
```
sphinx-apidoc --module-first --private --output-dir docs/modules cly
sphinx-build -v -n -a docs public
```
To see the documentation, check the `public/index.html` file that the command generated.

Sphinx configuration in [`docs/conf.py`](docs/conf.py) file.

The documentation is updated automatically by the continuous deploy (CD) pipeline of the project. CD configuration in [`.github/workflows/cd.yml`](.github/workflows/cd.yml) file.

### SonarCloud Code Analysis

[SonarCloud](https://sonarcloud.io/) analyzes the source code of the project through the CI pipeline.

## Pre-commit

To configure pre-commit automatically when cloning the repo, run
```
pip install pre-commit
git config --global init.templateDir ~/.git-template
pre-commit init-templatedir --hook-type commit-msg --hook-type pre-commit ~/.git-template
```
Must be installed globally. More information [here](https://pre-commit.com/#automatically-enabling-pre-commit-on-repositories).

To configure pre-commit locally, run
```
pre-commit install --hook-type commit-msg --hook-type pre-commit
```
with your virtual environment active.

To test it, run
```
pre-commit run --all-files
```

pre-commit configuration in [`.pre-commit-config.yaml`](.pre-commit-config.yaml) file.

## License

This repository is licensed under the terms of [MIT License](LICENSE).
