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

#Print the line
print(find_snap_id(file))