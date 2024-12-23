


pparams = 'c:/Users/EricChan/workspace/path-params.csv'


def load_table_schema(filename):
    screen_tbl_set = set()
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
        for line in lines:
            #print(line)
            if line.startswith('/'):
                screen_tbl_set.add(line.lower())
        # for item in table_names:
        #     print(item)
    return screen_tbl_set


if __name__ == '__main__':

    #load screen_defn from DB
    result = load_table_schema(pparams)
    # for item in sorted(result):
    #     print('ls '+item+'10491688_20240524125738_6840.pdf;')
    # print(len(result))
    #
    # for item in sorted(result):
    #     print('ls '+item+'10490001-10500000/10491688_20240524125738_6840.pdf;')
    # print(len(result))

    for item in sorted(result):
        print('ls '+item+'10405540_20230604212832_1577.pdf;')
    print(len(result))

    for item in sorted(result):
        print('ls '+item+'10400001-10410000/10405540_20230604212832_1577.pdf;')
    print(len(result))


