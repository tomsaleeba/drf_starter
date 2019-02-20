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

We've split the docker stack into two: the app and all the infrastructure to run the app. This affords us more
flexibility as we can either run the whole stack, or just run the infrastructure and run our app locally during dev. The
downside of doing this is that we have to explicitly name our docker-compose file in our commands. It's worth it though.

To run the whole stack:

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


If you only want to run the infrastructure, so you can run the app on your machine, you can do so by specifying the
docker-compose files to use. Our app is defined in a separate file so by excluding the `docker-compose.override.yml`
file -- that is automatically looked for and contains our app definition -- and including a separate override file, we
run just the bits we want and have them accessible.

  1. start just the infrastructure of the stack (everything but the app)
      ```bash
      docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d
      ```
  1. look in the `docker-compose.override.yml` file to see what environment variables the app expects. You may want to
     set some of these before starting the app so it points to the docker stack components. You can see the ports that
     we expose on the stack in the `docker-compose.dev.yml` file. For example
      ```bash
      export DATABASE_URL=postgres://user:password@localhost:5432/drf_db
      export AWS_ACCESS_KEY_ID=somekey
      export AWS_SECRET_ACCESS_KEY=somekey
      export S3_BUCKET=some-bucket
      export AWS_S3_ENDPOINT_URL=http://localhost:9000  # using minio
      ```
  1. remember to migrate the DB if you haven't already
      ```bash
      python manage.py migrate
      ```
  1. to stop the stack
      ```bash
      docker-compose -f docker-compose.yml -f docker-compose.dev.yml down -d
      # or
      docker-compose -f docker-compose.yml -f docker-compose.dev.yml down -d --volumes
      ```

## To document:

  1. health checks (`/ht/` endpoint)
  1. API keys
  1. S3 integration
