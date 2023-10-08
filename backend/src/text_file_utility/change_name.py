import os


def rename_file(old_filename, new_filename):
    """
    Rename a file.

    Parameters:
    - old_filename (str): The current path and name of the file.
    - new_filename (str): The new path and name for the file.

    Example:
    ```python
    rename_file("path/to/oldfile.txt", "path/to/newfile.txt")
    ```

    :param old_filename: The current path and name of the file.
    :type old_filename: str
    :param new_filename: The new path and name for the file.
    :type new_filename: str
    """
    try:
        # Attempt to rename the file
        os.rename(old_filename, new_filename)
        print(f"File renamed successfully: {old_filename} -> {new_filename}")
    except FileNotFoundError:
        print(f"File not found: {old_filename}")
    except FileExistsError:
        print(f"A file with the name {new_filename} already exists.")

# Uncomment the following line to test the function
# rename_file("backend/src/text-file-utility/test.doc", "backend/src/text-file-utility/test1.docx")
