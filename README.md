# package-template

## Structure
```
.
├── LICENSE
├── README.md
├── mypackage1
│   ├── __init__.py
│   ├── cli.py
│   ├── data
│   │   └── file1.txt
│   └── mymodules1
│       ├── __init__.py
│       ├── mymodule1.py
│       └── mymodule2.py
├── setup.cfg
├── setup.py
└── tests
    ├── conftest.py
    ├── test_mymodule1.py
    └── test_mymodule2.py
```

## To install dependencies
```
$ pip install -r requirements.txt
```

## To test
```
$ python setup.py test
========================================================================== test session starts ==========================================================================
...
tests/test_mymodule1.py::test_loader1 PASSED                                                                                                                      [ 20%]
tests/test_mymodule1.py::test_loader2 PASSED                                                                                                                      [ 40%]
tests/test_mymodule1.py::test_loader3 PASSED                                                                                                                      [ 60%]
tests/test_mymodule1.py::test_loader4 PASSED                                                                                                                      [ 80%]
tests/test_mymodule2.py::test_load_data_file PASSED                                                                                                               [100%]
=========================================================================== 5 passed in 0.36s ===========================================================================
```

## To check formatting
```
$ python setup.py flake8
running flake8
WARNING: flake8 setuptools integration is deprecated and scheduled for removal in 4.x.  For more information, see https://gitlab.com/pycqa/flake8/issues/544
```

## To install
```
$ pip install .
...
Successfully built mypackage1
Installing collected packages: mypackage1
Successfully installed mypackage1-0.3.4
```

## To run
```
$ mypkg1
main func started
reading data file: '12345'
```

## To import
```
>>> from mypackage1.mymodules1.mymodule2 import load_data_file
>>> data = load_data_file()
>>> print(data)
12345
```

## To uninstall
```
$ pip uninstall mypackage1
```
