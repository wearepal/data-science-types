#!/bin/bash

black -l 100 -t py36 . && flake8 *-stubs && python -m pytest -vv tests/ && python gen_pyi.py && mypy tests
