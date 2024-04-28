# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import fnmatch
import regex as re

file_path = 'c:/Users/EricChan/workspace/nas_master/src/com/nas/db/'

table_name_pattern = r'\b(?:SELECT|DELETE)\s+([a-zA-Z_][a-zA-Z0-9_]*)(?=\s*[;)\s])'
    #r'\b(?:table|from)\s+([a-zA-Z_][a-zA-Z0-9_]*)(?=\s*[;)\s])'


def extract_table_names(directory):
    # Use a breakpoint in the code line below to debug your script.
    # with open(dir, 'r') as file:  # r means read, w for write
    #     print(file.read())

    count = 0

    table_names = set()
    for root, dir, files in os.walk(directory):
        print(root)
        print("")
        for file in fnmatch.filter(files, "*.java"):
            print("..." + root+file)
            current_file_path = os.path.join(root, file)
            with open(current_file_path, 'r', encoding='utif8') as current:
                content = current.read()
                matches = re.findall(table_name_pattern, content)
                for match in matches:
                    table_names.add("match: "+match)
                    print(match)
            count = count + 1
        print()
        #with open(filename, "r"):
    print('total number of files: ', count)

    print("Table Names:")
    for table_name in table_names:
        print(table_name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    extract_table_names(file_path)
