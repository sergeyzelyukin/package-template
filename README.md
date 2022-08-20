# package-template

## Structure
```
.
├── LICENSE
├── README.md
├── resources
│   ├── __init__.py
│   └── data
│       └── file1.txt
├── setup.cfg
├── setup.py
├── src
│   ├── __init__.py
│   ├── cli.py
│   └── mymodules1
│       ├── __init__.py
│       ├── mymodule1.py
│       └── mymodule2.py
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
...
================================================= test session starts ==================================================
tests/test_mymodule1.py ....                                                                                     [ 80%]
tests/test_mymodule2.py .                                                                                        [100%]
================================================== 5 passed in 0.44s ===================================================
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

## To uninstall
```
$ pip uninstall mypackage1
```
