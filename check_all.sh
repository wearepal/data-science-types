#!/bin/bash

python gen_pyi.py && black -S -l 100 -t py36 . && flake8 *-stubs && python -m pytest -vv tests/ && mypy tests && echo "Check all complete!"
