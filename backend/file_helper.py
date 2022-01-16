import os

data_path = "data/"


def create_directory_if_not_exists(full_path):
    paths = full_path.split('/')
    for i_path in range(1, len(paths)):
        path = "/".join(paths[:i_path + 1])
        if not os.path.exists(path):
            os.mkdir(path)


def save_file(file):
    create_directory_if_not_exists(data_path)
    with open(data_path + file.filename, "wb") as buffer:
        buffer.write(file.file.read())


def get_file_name_extended(file_name, extended_part="-encoded"):
    file_name_split = file_name.split(".")
    file_name_without_extension = ".".join(file_name_split[:-1])
    file_name_extension = file_name_split[-1]
    return file_name_without_extension + extended_part + "." + file_name_extension
