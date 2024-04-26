# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import glob

file_path = 'c:/Users/EricChan/workspace/nas_master/src/com/nas/'


def extract_table_names(dir):
    # Use a breakpoint in the code line below to debug your script.
    # with open(dir, 'r') as file:  # r means read, w for write
    #     print(file.read())

    count = 0
    for filename in glob.iglob(dir + '**/*DAOMySQL.java', recursive=True):
        print(filename)
        #with open(filename, "r"):

        count = count + 1
    print('total number of files: ', count)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    extract_table_names(file_path)
