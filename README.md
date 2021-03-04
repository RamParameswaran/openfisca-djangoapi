# openfisca-djangoapi

A database and Django webserver layer for serving OpenFisca rulesets

## Install and run locally (developers)

Clone this repo:

```
$ git clone git@github.com:RamParameswaran/openfisca-djangoapi.git
$ cd openfisca-djangoapi
```

Create virtual environment (python 3.7) and install requirements

```
# We're using `virtualenvwrapper` to create the virtual env here, but you can use any other virtual env tool...
# NOTE - make sure Python 3.7 is installed on your machine!

$ mkvirtualenv openfisca-django --python=python3.7
$ pip install -r services/app/requirements.txt
```

Run the Django server locally

```
# First try running the Django server locally
$ python app/manage.py runserver

# The webserver should return:

System check identified no issues (0 silenced).

    You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
    Run 'python manage.py migrate' to apply them.
    March 01, 2021 - 03:29:31
    Django version 3.1.7, using settings 'config.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

# Next run a database migration and create an admin user
$ python app/manage.py migrate
$ python app/manage.py createsuperuser
# Enter usename and password

# Launch the webserver locally
$ python app/manage.py runserver
```

Ingest an OpenFisca ruleset into the database

```
# By default the database will be empty. To ingest data from an OpenFisca API:

# 1) Make sure you've set the `OPENFISCA_API_URL` environment variable in
# a .env file in the project root directory
# e.g. OPENFISCA_API_URL=https://dpie-ess-dev.herokuapp.com

# 2) run the Django `fetch_all` command
$ python app/manage.py fetch_all

```

Log into the admin backend

```
# Launch the webserver locally
$ python app/manage.py runserver

# On your browser naviate to http://localhost:8000/admin/
# Enter the superuser username and password that your just created

et voila!
```

## Docker

> We recommend you use Docker for local development **and** deployment. This ensures parity between development and production environments.

<em>First ensure that the `OPENFISCA_API_URL` environment variable is correctly set in the file `docker-compose.yml`</em>

Install docker and docker-compose on your machine (if you don't already have it installed):
- docker: https://docs.docker.com/get-docker/
- docker-compose: https://docs.docker.com/compose/install/

Init project:

```
$ cd openfisca-djangoapi
$ docker-compose build
```

Setup database:

```
$ docker-compose run app setup_db
$ docker-compose run app fetch_data
```

Launch:

```
$ docker-compose up app
```

Launch Nginx _(optional)_:

```
$ docker-compose up web
```

_Now your django app is available on http://localhost, but it's optional for development_

### Container commands

The image has

Run a command:

```
$ docker-compose run app <command>
```

Available commands:

| Command  | Description                                                                     |
| -------- | ------------------------------------------------------------------------------- |
| dev      | Start a normal Django development server                                        |
| bash     | Start a bash shell                                                              |
| manage   | Start manage.py                                                                 |
| setup_db | Setup the initial database. Any existing DB will be destroyed first.
| fetch_data | Ingests OpenFisca ruleset. Configure _$OPENFISCA_API_URL_ in docker-compose.yml |
| lint     | Run pylint                                                                      |
| python   | Run a python command                                                            |
| shell    | Start a Django Python shell                                                     |
| uwsgi    | Run uwsgi server                                                                |
| help     | Show this message                                                               |

#### Example: Create a Django superuser (to access the admin portal)

```
$ docker-compose run app manage createsuperuser
```

## Awesome resources

See [additional_resources.md](docs/additional_resources.md) to learn more about all the different components used in this repository.

