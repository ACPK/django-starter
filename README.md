Django Starter Project
======================

This is meant to be a quick jumping point for starting new Django projects. You should be able to
fork the repo, make a few changes and be ready for deployment to Heroku within a few minutes.

Heroku
------

# Create the project on Heroku
`heroku create [app-name]`

# Add Postgres
`heroku addons:create heroku-postgresql:hobby-dev`

# Configure environment vars
`heroku config:set DJANGO_SETTINGS_MODULE="project.settings.production"`
`heroku config:set DJANGO_SECRET_KEY="`openssl rand -base64 32`"`

# Deploy to Heroku
`git push heroku master`

# Setup Database
`heroku run python manage.py migrate`
