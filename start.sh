#/bin/bash

sudo apt install -y python3-tk python3-dev

poetry install

poetry run python src/click_helper/scripts/click_helper.py