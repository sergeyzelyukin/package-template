from pkg_resources import resource_stream


def load_data_file():
    return resource_stream("resources", "data/file1.txt").read().decode("utf-8")
