import os


def is_text_file(file_path: str) -> bool:
    """
    Check if a file is a valid text file based on its extension.

    Parameters:
    - file_path (str): The path to the file.

    Returns:
    - bool: True if the file is a valid text file, False otherwise.

    Example:
    ```python
    is_text = is_text_file("path/to/textfile.txt")
    print(is_text)
    ```

    :param file_path: The path to the file.
    :type file_path: str
    :return: True if the file is a valid text file, False otherwise.
    :rtype: bool
    """
    # Check if the file exists
    if not os.path.exists(file_path):
        return False

    # Check if the file is a regular file
    if not os.path.isfile(file_path):
        return False

    # Check if the file extension corresponds to a valid text format
    file_extension = file_path[-4:].lower()  # Consider case-insensitive check
    valid_extensions = ['.doc', '.txt', '.docx']

    if file_extension in valid_extensions:
        return True

    print(f"Unsupported file format: {file_extension}")
    return False

# Uncomment the following line to test the function
# is_text = is_text_file("backend/src/text-file-utility/test.txt")
# print(is_text)
