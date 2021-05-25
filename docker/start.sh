#!/usr/bin/env bash
exec gunicorn "$@" app:app