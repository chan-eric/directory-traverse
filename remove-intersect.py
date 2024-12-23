


#load from database
csv = 'c:/Users/EricChan/workspace/screen_defn.csv'

unused = 'c:/Users/EricChan/workspace/unused.csv'


def load_table_schema(filename):
    screen_tbl_set = set()
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
        for line in lines:
            #print(line)
            screen_tbl_set.add(line.lower())
        # for item in table_names:
        #     print(item)
    return screen_tbl_set


if __name__ == '__main__':

    #load screen_defn from DB
    table_set = load_table_schema(csv)
    unused_set = load_table_schema(unused)
    # intersect = unused_set.intersection(table_set)
    # for item in intersect:
    #     print(item)
    # print(len(intersect))
    result = unused_set-table_set
    for item in sorted(result):
        print(item)
    print(len(result))



