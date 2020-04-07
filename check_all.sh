#!/bin/bash

black -l 100 -t py36 . && python -m pytest -vv tests/ && mypy tests
