from mypackage1.mymodules1.mymodule1 import loader


def main():
    print("main func started")
    print("reading data file: '{}'".format(loader()))
