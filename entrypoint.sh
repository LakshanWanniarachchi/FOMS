#!/bin/sh

gunicorn -c gunicorn.conf.py main:app
