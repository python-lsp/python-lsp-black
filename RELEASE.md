To release a new version of python-lsp-black:
1. git fetch upstream && git checkout upstream/master
2. Close milestone on GitHub
3. git clean -xfdi
4. Update CHANGELOG.md with loghub: `loghub python-lsp/python-lsp-black  --milestone vX.X.X`
5. git add -A && git commit -m "Update Changelog"
6. Update release version in ``setup.cfg`` (set release version, remove '.dev0')
7. git add -A && git commit -m "Release vX.X.X"
8. python setup.py sdist
9. python setup.py bdist_wheel
10. twine check dist/*
11. twine upload dist/*
12. git tag -a vX.X.X -m "Release vX.X.X"
13. Update development version in ``setup.cfg`` (add '.dev0' and increment minor)
14. git add -A && git commit -m "Back to work"
15. git push upstream master
16. git push upstream --tags
17. Draft a new release in GitHub using the new tag.
