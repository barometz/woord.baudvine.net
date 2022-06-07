Quickstart:
- git submodule update --init
- pipenv install
- pipenv run pelican content
- pipenv run pelican --listen

Publish:
- pipenv run make rsync_upload (or ssh_upload if rsync is not available)
