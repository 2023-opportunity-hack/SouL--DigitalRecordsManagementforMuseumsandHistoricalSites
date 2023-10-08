import os


def is_image_file(file_path: str) -> bool:
    # Check if the file exists
    if not os.path.exists(file_path):
        return False

    # Check if the file is a regular file
    if not os.path.isfile(file_path):
        return False

    # Check if the file extension corresponds to a valid text format
    file_extension = file_path[len(file_path) - 4:]
    valid_extensions = ['.doc', '.txt', 'docx']

    if file_extension in valid_extensions:
        return True

    print(f"Unsupported file format: {file_extension}")
    return False
