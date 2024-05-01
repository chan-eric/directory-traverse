import os
import fnmatch
import regex as re


file_path = 'c:/Users/EricChan/workspace/nas_master/'
csv = 'c:/Users/EricChan/workspace/tables_202404291350.csv'

def load_table_schema(filename):
    table_names = []
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
        for line in lines:
            #print(line)
            pair = line.split(',')
            table_names.append((pair[0],pair[1]))
        # for item in table_names:
        #     print(item)
    return table_names
def find_in_master(list_of, dir_):
    tables_used = set()
    for root, dir, files in os.walk(dir_):
        for file in fnmatch.filter(files, "*.java"):
            current_file_path = os.path.join(root, file)
            #print("...", current_file_path)
            with open(current_file_path, 'r', encoding='utf8') as current:
                content = current.read()
                # matches = re.findall(table_name_pattern, content)
                # for match in matches:
                #     table_names.add("match: "+match)
                #     print(match)
                for table in list_of:
                    if re.search(table[0], content, re.IGNORECASE):
                        tables_used.add(table[0].rstrip())
    return tables_used


if __name__ == '__main__':
    table_schema_pair = load_table_schema(csv)
    result = find_in_master(table_schema_pair, file_path)