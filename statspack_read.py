import re


#Define file path
file = "statspack_example.txt"

#Define string
string_to_search = "SQL ordered by CPU  DB/Inst:"

#Find in a text file the number of the line with "Snapshot" + space + "Snap Id" + space + "Snap Time" + space + "Sessions Curs/Sess Comment"
def find_snap_id(file):
    with open(file, "r") as file:
        for num, line in enumerate(file, 1):
            if string_to_search in line:
                return num

line_number = find_snap_id(file)

#Store the following 50 lines from the line string_to_search in a list (SQL_ordered_by_CPU)
def print_snap_id(file):
    SQL_ordered_by_CPU = []
    with open(file, "r") as file:
        for num, line in enumerate(file, 1):
            if num == line_number:
                for i in range(50):
                    #Each line is stored in a list as a string
                    SQL_ordered_by_CPU.append(file.readline())
                break
    return SQL_ordered_by_CPU
            
#Print the list SQL_ordered_by_CPU
for line in print_snap_id(file):
    print(line)
