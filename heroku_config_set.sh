#!/bin/sh

heroku config:set LANGUAGE=$LANGUAGE
heroku config:set TIME_ZONE=$TIME_ZONE
heroku config:set CLOUDINARY_NAME=$CLOUDINARY_NAME
heroku config:set CLOUDINARY_API_KEY=$CLOUDINARY_API_KEY
heroku config:set CLOUDINARY_API_SECRET=$CLOUDINARY_API_SECRET
heroku config:set CLOUDINARY_DEFAULT_POST_IMAGE=$CLOUDINARY_DEFAULT_POST_IMAGE
heroku config:set DB_NAME=$DB_NAME
heroku config:set DB_USER=$DB_USER
heroku config:set DB_PASSWORD=$DB_PASSWORD
heroku config:set DB_HOST=$DB_HOST
heroku config:set DB_PORT=$DB_PORT
heroku config:set SECRET_KEY=$(python -c "import secrets; print(secrets.token_hex())")
