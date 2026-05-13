import os


def create_folder(folder_path):
    """
    Creates a folder if it does not already exist.
    """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def file_exists(file_path):
    """
    Checks whether a file exists.
    """
    return os.path.isfile(file_path)


def get_file_name(file_path):
    """
    Returns the file name from a file path.
    """
    return os.path.basename(file_path)


def clear_console():
    """
    Clears the console output.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
