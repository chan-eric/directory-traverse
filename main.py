# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import fnmatch
import regex as re

#directory to search
file_path = 'c:/Users/EricChan/workspace/nas_master/src/com/nas/db/'

#where the input file is located
list_of_tables = 'c:/Users/EricChan/workspace/tables.csv'

table_name_pattern = r'\b(?:SELECT|DELETE)\s+([a-zA-Z_][a-zA-Z0-9_]*)(?=\s*[;)\s])'
    #r'\b(?:table|from)\s+([a-zA-Z_][a-zA-Z0-9_]*)(?=\s*[;)\s])'


def extract_table_names(directory):
    # Use a breakpoint in the code line below to debug your script.
    # with open(dir, 'r') as file:  # r means read, w for write
    #     print(file.read())

    count = 0

    table_names = set()
    for root, dir, files in os.walk(directory):
        table_names = load_list(list_of_tables)
        print(root)
        print("")
        for file in fnmatch.filter(files, "*.java"):
            
            current_file_path = os.path.join(root, file)
            print("..." + current_file_path)
            with open(current_file_path, 'r', encoding='utf8') as current:
                content = current.read()
                # matches = re.findall(table_name_pattern, content)
                # for match in matches:
                #     table_names.add("match: "+match)
                #     print(match)
                if (content.find('java.sql.PreparedStatement') != -1):
                    for table in table_names:
                        if(table.find('_')!= -1 and re.search(table, content, re.IGNORECASE)):
                            print('appraisal.'+table)
            count = count + 1
        print()
        #with open(filename, "r"):
    print('total number of files: ', count)

    # print("Table Names:")
    # for table_name in table_names:
    #     print(table_name)


def load_list(filename):
    table_names = set()
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
        for line in lines:
            #print(line)
            table_names.add(line)
    return table_names

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #load_list(list_of_tables)
    extract_table_names(file_path)
