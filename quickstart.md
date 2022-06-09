Quickstart:
- git submodule update --init
- pushd pelican-plugins, git submodule update --init pelican-open_graph, popd
- pipenv install
- pipenv run pelican content
- pipenv run pelican --listen

Publish:
- pipenv run make rsync_upload (or ssh_upload if rsync is not available)
