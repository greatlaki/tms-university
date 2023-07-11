# tms-university

### Required tools
Make sure you have installed following tools:

- python >= 3.11
- [pyenv](https://github.com/pyenv/pyenv)
- [poetry](https://python-poetry.org/)
- [pre-commit](https://pre-commit.com/)
- docker >= 24.0.2
- docker compose >= 2.19.1

### Setting up the project

#### Clone the repository (clone with SSH)
`git@github.com:greatlaki/e-wallet.git`

#### Set a local python 3.11.* version
`pyenv local 3.11.*`<br>
#### Install poetry
`pip install poetry`<br>
#### Create a `pyproject.toml`
`poetry init`<br>
#### Create new poetry virtualenv
`poetry env use 3.11.*`<br>
#### Install dependencies
`poetry install`

#### Install pre commit hooks
`pre-commit install`

Go to the folder where you cloned the project. Add variables to the dotenv file
### Variables of the dotenv file

### Django settings

| Name                    | Sample                                                 |
|-------------------------|--------------------------------------------------------|
| SQLALCHEMY_DATABASE_URL | postgresql://postgres:postgres@localhost:5432/postgres |


#### Setting up Migrations
`alembic upgrade heads`