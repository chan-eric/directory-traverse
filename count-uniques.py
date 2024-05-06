tables_found = 'c:/Users/EricChan/workspace/found.txt'

find_unique = set()


def count_lines(filename):
    with open(filename, 'r', encoding='UTF-8') as file:
        while line := file.readline():
            find_unique.add(line.rstrip())
        print('Number of tables found in NAS App:', len(find_unique))


if __name__ == '__main__':
    count_lines(tables_found)
