

#find from NAS source cde
tables_found = 'c:/Users/EricChan/workspace/found.txt'


#queried from database
csv = 'c:/Users/EricChan/workspace/tables_202404291350.csv'

def count_lines(filename):
    find_unique = set()
    with open(filename, 'r', encoding='UTF-8') as file:
        while line := file.readline():
            if (line.startswith('appraisal.')):
                find_unique.add(line[10:-1])
        print('Number of tables found in NAS App:', len(find_unique))
    return find_unique


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

def convert_to_set(pair_values):
    set_result = set()
    for item in pair_values:
        if (item[1] == 'appraisal'):
            set_result.add(item[0].rstrip())
    return set_result

def find_unused(set_one, set_two):
    result_list = list()
    intersect = set_two.intersection(set_one)
    for item in intersect:
        set_two.remove(item)
    for unused in set_two:
        result_list.append(unused)
    result_list.sort()
    print((result_list))
    print(len(result_list))



if __name__ == '__main__':
    #from NAS app
    set1 = count_lines(tables_found)
    #loaded all table - schema pairs from DB
    table_schema_pair = load_table_schema(csv)
    #pick up all tables from appraisal schema
    set2 = convert_to_set(table_schema_pair)
    find_unused(set1, set2)
