import re


#Define file path
file = "statspack_example.txt"

#Define string
string_to_search = "SQL ordered by Elapsed time for DB:"

#Find in a text file the number of the line with "Snapshot" + space + "Snap Id" + space + "Snap Time" + space + "Sessions Curs/Sess Comment"
def find_snap_id(file):
    with open(file, "r") as file:
        for num, line in enumerate(file, 1):
            if string_to_search in line:
                return num

line_number = find_snap_id(file)


# Find the third number in the 15th line of the list SQL_ordered_by_CPU
def find_number(file):
    with open(file, "r") as file:
        for num, line in enumerate(file, 1):
            if num == line_number + 7:
                #Store all number in line
                string = file.readline()
                #Find all number in line
                result = re.findall(r'[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?', string)
                #Join 7 and 8 number in line
                return result[3]

#Print the result
SQL_usage = find_number(file)
print(SQL_usage)

#Store the strings beneath line_number + 7 until the next empty line
def find_string(file):
    with open(file, "r") as file:
        for num, line in enumerate(file, 1):
            if num == line_number + 8:
                #Store lines in a list  
                module = file.readlines()
                #Stop at first empty line
                module = module[:module.index('\n')]
                
                return module

#Print all lines
module = find_string(file)
print(module)


