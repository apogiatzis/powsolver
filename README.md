# PoWSolver (WIP)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)



A proof of work puzzle solver mainly for CTF challenges and whatnot.


## Getting Started

You can get started using `powsolver` by installing it through pip.

```
pip install powsolver
```

## Usage

The main component of the powsolver package is the `PoWSolver` class which encapsulates the main functionality.

Here is a basic usage example of the powsolver:

```python
from powsovler import PoWSolver

solver = PoWSolver()
solver.parse(
    "Please submit a printable string X, such that {alg}(X)[{start:d}:] = {target} and len(X) = {len}",
    "Please submit a printable string X, such that sha256(X)[-6:] = 86d113 and len(X) = 11"
)
sol = solver.sol()
```

Exampled of more elaborated usage can be found in the [examples](./examples/)  folder.

## Running the tests

### :TODO:

## Contributing

Any PRs are welcome!

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/apogiatzis/powsolver/tags). 

## Authors

* **Antreas Pogiatzis** - *Initial work* 

See also the list of [contributors](https://github.com/apogiatzis/powsolver/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


