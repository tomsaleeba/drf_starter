> opinionated starter template (or examle) of how I like using django-rest-framework

## Using the right Python version
You must use Python 3.5.x for this project. We're limited by what [DREST](https://github.com/AltSchool/dynamic-rest#compatibility-table) supports.

To get started from a fresh clone:
  1. install [pyenv](https://github.com/pyenv/pyenv)
  1. install [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)
  1. install the required version of python with:
      ```bash
      cd drf_starter/
      pyenv install $(pyenv local)
      ```
  1. create a virtual environment (using `pyenv`):
      ```bash
      pyenv virtualenv drf_starter
      ```
  1. activate the virtual environment:
      ```bash
      pyenv activate drf_starter
      ```
  1. install the dependencies for this project:
      ```bash
      pip install -r requirements.txt
      ```
  1. continue on like you normally would

## Run with docker
Make sure you have `docker` and `docker-compose` installed first.

  1. make sure you're in the root of this repo
  1. start the stack
      ```bash
      docker-compose up -d
      # or if you need to force a rebuild of the app container
      docker-compose up --build -d
      ```
  1. migrate the database:
      ```bash
      docker exec -it drf_app sh -c 'python manage.py migrate'
      ```
  1. make some calls on the API
      ```bash
      curl localhost:8000/
      ```
  1. shutdown the stack
      ```bash
      docker-compose down            # leaves DB data volume existing
      docker-compose down --volumes  # destroys the DB data volume
      ```
