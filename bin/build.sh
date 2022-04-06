#!/bin/bash
set -e

cd $( dirname "$0" )
echo "Running tests..."
python functional_test_runner.py
echo "Running lint..."
PYTHONPATH=.. python -m pylint ../trailing_commas.py
