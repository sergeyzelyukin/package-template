from setuptools import setup, find_packages
setup(
    name="mypackage1",
    version="0.3.4",
    packages=find_packages("."),
    package_data={"resources": ["data/*.txt"]},
    entry_points = {
        "console_scripts": [
            "mypkg1=src.cli:main"
        ]
    },
    setup_requires = [
        "flake8",
        "pytest-runner"
    ],
)
