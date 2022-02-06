from setuptools import setup, find_packages  # noqa: H301

NAME = "equibles_websockets"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["signalrcore >= 0.9.2"]

setup(
    name=NAME,
    version=VERSION,
    description="Equibles websockets for live quotes",
    author_email="equibles@gmail.com",
    url="https://www.equibles.com/",
    keywords=["Swagger", "Stocks"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description=""
)