from setuptools import setup, find_packages
setup(
    name="mypackage1",
    version="0.3.5",
    packages=find_packages("."),
    package_data={"mypackage1": ["data/*.txt"]},
    scripts=["bin/auxiliary1.sh"],
    entry_points = {
        "console_scripts": [
            "mypkg1=mypackage1.cli:main"
        ]
    },
    setup_requires = [
        "flake8<4.0.0",
        "pytest-runner"
    ],
    python_requires = ">=3.7",
    install_requires = [
        "click>=8.0.0",
    ],
    tests_require = [
        "pytest"
    ],
)
