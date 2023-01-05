#!/bin/sh

set -o errexit
set -o nounset

PY=${PY:-python}

# Top-level submodules
git submodule update --init

cd pelican-plugins
# Submodules for specific plugins in pelican-plugins
git submodule update --init pelican-open_graph
cd ..

$PY -m pip install --user pipenv
$PY -m pipenv install
$PY -m pipenv run pelican-themes -s $PWD/pelican-themes/pelican-bootstrap3
