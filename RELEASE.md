To release a new version of python-lsp-black:

1. git fetch upstream && git checkout upstream/master
1. Close milestone on GitHub
1. git clean -xfdi
1. Update CHANGELOG.md with loghub: `loghub python-lsp/python-lsp-black  --milestone vX.X.X`
1. git add -A && git commit -m "Update Changelog"
1. Update release version in `setup.cfg` (set release version, remove '.dev0')
1. git add -A && git commit -m "Release vX.X.X"
1. python setup.py sdist
1. python setup.py bdist_wheel
1. twine check dist/\*
1. twine upload dist/\*
1. git tag -a vX.X.X -m "Release vX.X.X"
1. Update development version in `setup.cfg` (add '.dev0' and increment minor)
1. git add -A && git commit -m "Back to work"
1. git push upstream master
1. git push upstream --tags
1. Draft a new release in GitHub using the new tag.
