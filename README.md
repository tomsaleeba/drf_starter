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
      ./dev-stack.sh
      ```
  1. the output of the previous command will show you the environment variables you should define so your local dev
     instance of the app works as expected
  1. remember to migrate the DB if you haven't already
      ```bash
      python manage.py migrate
      ```
  1. to stop the stack
      ```bash
      ./dev-stack.sh down
      # or, to delete all the data too
      ./dev-stack.sh down --volumes
      ```

## API Keys
By default, this API is public read-only and requires a token to write. To get yourself a token:

  1. create a user
      ```bash
      username=tom
      python manage.py createsuperuser --username $username --email $username@local
      ```
  1. generate a token for the user. Note: running this again will return the existing key.
      ```bash
      python manage.py drf_create_token $username
      ```
  1. use the token in a call (we're using [httpie](https://httpie.org/))
      ```bash
      http :8000/locations/ name=firstloc Authorization:'Bearer 8cb15bb2468ba29922b07cdd935c623b3c709a76' 
      ```
  1. to regenerate a key for a user, add the `-r` flag
      ```bash
      python manage.py drf_create_token -r $username
      ```
  1. you can also generate tokens via the `/admin/` page in your browser


## Loading sample data
We have some sample data (a fixture) to make it easier to try this API, to load it:

  1. if your stack is already running, we need to stop it and destroy any data
      ```bash
      docker-compose down --volumes  # for the full stack, or
      ./dev-stack.sh down --volumes  # for the dev stack
      ```
  1. now start the stack again
      ```bash
      docker-compose up -d  # for the full stack, or
      ./dev-stack.sh        # for the dev stack
      ```
  1. migrate the database
      ```bash
      ./manage.py migrate
      ```
  1. load the fixture
      ```bash
      ./manage.py loaddata drf_starter/the_app/test/the_app_test_fixtures.json 
      ```

## To document:

  1. health checks (`/ht/` endpoint)
  1. S3 integration
  1. schema endpoint (`/schema/` or `OPTIONS` on any list endpoint)
  1. coreapi docs (no support for old versions)
  1. versioning

## TODO

  1. change requests for non existing fields `?include[]=blah` from 500 to 4xx response
