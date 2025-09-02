#!/bin/bash

sudo apt install -y python3-tk python3-dev

poetry lock
poetry install

poetry run python -m src.click_helper.main