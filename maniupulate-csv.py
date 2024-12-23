import csv

csvfile = 'c:/temp4/ACCPAC_AR_EXPORT_00000_TB_L.csv'
output = 'c:/temp4/output.csv'

def process_csv(filename, out):
    result = []
    with open(filename) as file, open(out, "w", newline='') as outfile:

        writer = csv.writer(outfile)

        reader = csv.reader(file)
        header = next(reader) # Skip headers
        #result.append(header)
        writer.writerow(header)
        line = 1
        for row in reader:
            row[10] = line
            line = line + 1
            print(row)
            new_row1 = row.copy()  # Duplicate the row
            new_row1[14] = '40017'
            new_row1[13] = '10'
            new_row1[10] = line
            line = line +1
            for i in range(10):  # Clear columns 0 to 9
                if i < len(new_row1):
                    new_row1[i] = ""
            print(new_row1)
            new_row2 = row.copy()  # Duplicate the row
            new_row2[14] = '40018'
            new_row2[13] = '13'
            new_row2[10] = line
            line = line + 1
            for i in range(10):  # Clear columns 0 to 9
                if i < len(new_row2):
                    new_row2[i] = ""
            print(new_row2)
            new_row3 = row.copy()  # Duplicate the row
            new_row3[15] = '40019'
            new_row3[13] = '15'
            new_row3[10] = line
            line = line + 1
            for i in range(10):  # Clear columns 0 to 9
                if i < len(new_row3):
                    new_row3[i] = ""
            print(new_row3)
            writer.writerow(row)
            writer.writerow(new_row1)
            writer.writerow(new_row2)
            writer.writerow(new_row3)
    return result

if __name__ == '__main__':
    result = process_csv(csvfile, output)



