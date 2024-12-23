tables_found = 'c:/Users/EricChan/workspace/found.txt'




def count_lines(filename):
    find_unique = set()
    with open(filename, 'r', encoding='UTF-8') as file:
        while line := file.readline():
            if line.startswith('appraisal.'):
                find_unique.add(line.rstrip())
        print('Number of unique tables found in NAS App:', len(find_unique))


if __name__ == '__main__':
    count_lines(tables_found)
