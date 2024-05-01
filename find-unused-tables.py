#directory to search
file_path = 'c:/Users/EricChan/workspace/nas_master/'

#where the input file is located
csv = 'c:/Users/EricChan/workspace/tables_202404291350.csv'

result = 'c:/Users/EricChan/workspace/result2.csv'

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

def load_result(filename):
    table_names = []
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
        for line in lines:
            table_names.append(line)
        # for item in table_names:
        #     print(item)
    return table_names



if __name__ == '__main__':
    table_schema_pair = load_table_schema(csv)

    res_list = load_result(result)
    for item in table_schema_pair:
        if item not in res_list:
            print(item)

