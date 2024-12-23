import os
import fnmatch
import regex as re


file_path = 'c:/Users/EricChan/workspace/nas_master/'
ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
excluded_extensions = ['.idx', '.pack', '.rev', '.zip', '.gen', '.tree', '.jar', '.pdf', '.jpg', '.png']
accepted_extensions = ['.java', '.properties', '.xml']

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
def find_in_master(dir_):
    for root, dir, files in os.walk(dir_):
        for file in fnmatch.filter(files, "*.*"):
            current_file_path = os.path.join(root, file)
            #print("...", current_file_path)
            try:
                if any(file.endswith(ext) for ext in accepted_extensions):
                    with open(current_file_path, 'r', encoding='utf8') as current:
                        content = current.read()
                        ip_matches = ip_pattern.findall(content)
                        if ip_matches:
                            print(f"IP addresses found in {current_file_path}: {ip_matches}")

                        # matches = re.findall(table_name_pattern, content)
                        # for match in matches:
                        #     table_names.add("match: "+match)
                        #     print(match)
                      #  for table in list_of:
                      #      if re.search(table[0], content, re.IGNORECASE):
                      #          tables_used.add(table[0].rstrip())
            except:
                print("")
    return ""


if __name__ == '__main__':
    result = find_in_master(file_path)