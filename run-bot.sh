#!/bin/sh
export PYTHONUNBUFFERED=TRUE
PATH=$PATH:/home/ubuntu/.local/bin
poetry install --no-root
exec poetry run python3 ./bot.py
