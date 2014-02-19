Some Notes Regarding Debian
===========================

Create Debian Package from PyPI
-------------------------------

Note: `sudo` must be installed and configured correctly
(maybe also fakeroot and python-all?).

```
apt-get update
apt-get install python-stdeb python-all-dev
pypi-install name-of-package
```

Replace `name-of-package` with the actual name of the PyPI package.

Create Debian Package with setuptools
-------------------------------------

Create binary package:
```
python setup.py --command-packages=stdeb.command bdist_deb
```

Create source package (and later a binary package):
```
python setup.py --command-packages=stdeb.command sdist_dsc
dpkg-buildpackage -rfakeroot -uc -us
```
