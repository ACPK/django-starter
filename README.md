Django Starter Project
======================

This is meant to be a quick jumping point for starting new Django projects. You should be able to
fork the repo, make a few changes and be ready for deployment to Heroku within a few minutes.

[![TravisCI Build Status](https://api.travis-ci.org/inputlogic/django-starter.svg?branch=master)](https://travis-ci.org/inputlogic/django-starter)

Specifics
---------

- Python 3.6.x
- Django 1.10.x
- Postgres

Structure
---------

- `apps/` All Django apps exist here
- `libs/` All custom Python libraries (not specific to an app) exist here
- `project/settings/` All Django settings exist here
- `project/settings/common.py` Common settings across all environments
- `project/settings/local.py` Local (development) specific settings
- `project/settings/production.py` Product (Heroku) specific settings
- `static/` All static files such as CSS, JS etc
- `templates/` HTML templates

Local Development
-----------------

##### Ensure Python 3 is installed
```
$ brew install python3
```

##### Ensure Postgres is installed
```
$ brew install postgresql
$ createdb postgres
$ createuser --superuser postgres
```

##### Clone repo
```
$ git clone git@github.com:inputlogic/django-starter
$ cd django-stater
```

##### Setup virtual environment
```
$ virtualenv -p `which python3` env
$ . env/bin/activate
```

##### Setup database
```
$(env) ./manage migrate
```

##### Run it!
```
$(env) ./manage runserver
```

Heroku
------

##### Create the project on Heroku*
```
$ heroku create [app-name]
```

##### Add Postgres
```
$ heroku addons:create heroku-postgresql:hobby-dev
```

##### Add Sendgrid
```
$ heroku addons:create sendgrid:starter
```

##### Configure Django env vars
```
$ heroku config:set DJANGO_SETTINGS_MODULE="project.settings.production"`
$ heroku config:set DJANGO_SECRET_KEY="`openssl rand -base64 32`"
```

##### Configure Sendgrid env vars
```
$ heroku config:set EMAIL_HOST="smtp.sendgrid.net"
$ heroku config:set EMAIL_HOST_USER="`heroku config:get SENDGRID_USERNAME`"
$ heroku config:set EMAIL_HOST_PASSWORD="`heroku config:get SENDGRID_PASSWORD`"
```

##### Configure AWS S3 env vars
```
$ heroku config:set AWS_ACCESS_KEY_ID="ID-HERE"
$ heroku config:set AWS_SECRET_ACCESS_KEY="KEY-HERE"
$ heroku config:set AWS_STORAGE_BUCKET_NAME="BUCKET-NAME-HERE"
```

##### Deploy to Heroku
```
$ git push heroku master
```

##### Setup database
```
$ heroku run python manage.py migrate
```

##### Setup admin
```
$ heroku run python manage.py createsuperuser
```


Celery
------

##### Message Broker
```
pip install celery
brew update
brew install rabbitmq
```

##### Run RabbitMQ Servers
```
/usr/local/sbin/rabbitmq-server
```

##### Stopping RabbitMQ Servers
```
rabbitmqctl stop
```

##### Run RabbitMQ with PATH set
`export PATH=$PATH:/usr/local/sbin` add to ~/.bash_profile or ~/.profile 
`rabbitmq-server` run the server using a window
`rabbitmq-server -detached` run the server in the background

##### Creating a new rabbitmq user
`'amqp://guest:guest@localhost:5672//'` default broker_url
```
rabbitmqctl add_user myuser mypassword
rabbitmqctl add_vhost myvhost
rabbitmqctl set_user_tags myuser mytag
rabbitmqctl set_permissions -p myvhost myuser "".*" ".*" ".*"
```

##### Running Celery Locally
```
celery --app=project.settings.celery.app worker --loglevel=INFO
```