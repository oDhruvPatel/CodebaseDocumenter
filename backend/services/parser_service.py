import os

ex = "C:\\Users\\dhruv\\OneDrive\\Desktop\\Sites\\codebasedocumentor\\backend\\repositories\\speercheck"
IGNORE_DIR = []
IGNORE_FILES = []
def parsing_files(repository_path):
    result_files = []
    result_structure = []

    for root, dirs, files in os.walk(repository_path):

        # dir filter
        dirs[:] = [d for d in dirs if d not in IGNORE_DIR]

        folder_structure = {
            "path": root,
            "files": files
        }

        # file loop MUST be inside os.walk
        for file in files:
            if file in IGNORE_FILES:
                continue

            file_data = {
                "path": os.path.join(root, file),
                "name": file
            }

            result_files.append(file_data)
        result_structure.append(folder_structure)

    return result_structure

print(parsing_files(ex))