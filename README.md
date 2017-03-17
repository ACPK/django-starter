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

# Add Sendgrid
`heroku addons:create sendgrid:starter`

# Configure Django env vars
`heroku config:set DJANGO_SETTINGS_MODULE="project.settings.production"`
`heroku config:set DJANGO_SECRET_KEY="`openssl rand -base64 32`"`

# Configure Sendgrid env vars
`heroku config:set EMAIL_HOST="smtp.sendgrid.net"`
`heroku config:set EMAIL_HOST_USER="`heroku config:get SENDGRID_USERNAME`"`
`heroku config:set EMAIL_HOST_PASSWORD="`heroku config:get SENDGRID_PASSWORD`"`

# Configure AWS S3 env vars
`heroku config:set AWS_ACCESS_KEY_ID="ID-HERE"`
`heroku config:set AWS_SECRET_ACCESS_KEY="KEY-HERE"`
`heroku config:set AWS_STORAGE_BUCKET_NAME="BUCKET-NAME-HERE"`

# Deploy to Heroku
`git push heroku master`

# Setup Database
`heroku run python manage.py migrate`
