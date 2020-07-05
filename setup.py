from setuptools import setup

# read the contents of your README file
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    install_requires=[
        "dill==0.3.2",
        "multiprocess==0.70.10",
        "parse==1.15.0",
        "pathos==0.2.6",
        "pox==0.2.8",
        "ppft==1.6.6.2",
        "six==1.15.0",
    ],
    name="powsolver",
    version="0.1.2",
    description="Proof of Work solver mainly for CTF challenges",
    url="http://github.com/apogiatzis/powsolver",
    author="Antreas Pogiatzis",
    author_email="pogiatzis.c.a@gmail.com",
    license="MIT",
    packages=["powsolver"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    zip_safe=False,
)
