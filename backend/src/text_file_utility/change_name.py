import os


def rename_file(old_filename, new_filename):
    try:
        os.rename(old_filename, new_filename)
        print(f"File renamed successfully: {old_filename} -> {new_filename}")
    except FileNotFoundError:
        print(f"File not found: {old_filename}")
    except FileExistsError:
        print(f"A file with the name {new_filename} already exists.")


# rename_file("backend/src/text-file-utility/test.doc",
#             "backend/src/text-file-utility/test1.docx")
