#!/bin/sh

set -o errexit
set -o nounset

PY=${PY:-python}

$PY -m pipenv run make rsync_upload
