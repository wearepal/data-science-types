#!/bin/bash

echo "Begin check..." \
&& black -l 100 -t py36 . \
&& python gen_pyi.py \
&& black -l 100 -t py36 --pyi --fast matplotlib-stubs/pyplot.pyi.in \
&& flake8 *-stubs \
&& python -m pytest -vv tests/ \
&& mypy tests \
&& echo "Check all complete!"
