import re
import prettytable as pt


#Define file path
file = "statspack_example.txt"

#Define string
string_to_search1 = "SQL ordered by Elapsed time for DB:"
string_to_search2 = "SQL ordered by CPU  DB/Inst:"

#Find line of Elapsed time 
def find_line_elapsed(file):
    with open(file, "r") as file:
        for num, line in enumerate(file, 1):
            if string_to_search1 in line:
                first_condition =  num
                return first_condition

#Find line of CPU time
def find_line_cpu(file):
    with open(file, "r") as file:
        for num, line in enumerate(file, 1):
            if string_to_search2 in line:
                second_condition =  num
                return second_condition


#Store line number
first_condition =  find_line_elapsed(file)
second_condition = find_line_cpu(file)

# Find percentage of Total Elapsed Time
def find_percTotal_Elapsed(file, first_condition):
    with open(file, "r") as file:
        for num, line in enumerate(file, 1):
            if num == first_condition + 7:
                #Store all number in line
                string = file.readline()
                #Find all number in line and append to a list
                result = re.findall(r'[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?', string)
                #Join 7 and 8 number in line
                total_elapsed =  result[2]
            
    return total_elapsed

# Find percentage of Total CPU Time
def find_percTotal_CPU(file, second_condition):
    with open(file, "r") as file:
        for num, line in enumerate(file, 1):
            if num == second_condition + 7:
                #Store all number in line
                string = file.readline()
                #Find all number in line and append to a list
                result = re.findall(r'[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?', string)
                #Join 7 and 8 number in line
                total_cpu =  result[2]
            
    return total_cpu

#%Total Elapsed Time
total_elapsed =  find_percTotal_Elapsed(file, first_condition)
total_cpu = find_percTotal_CPU(file, second_condition)

#Find most expensive SQL (Elapsed Time)
def find_SQLs_Elapsed(file, first_condition):
    with open(file, "r") as file:
        for num, line in enumerate(file, 1):
            if num == first_condition + 8:
                #Store lines in a list  
                module_elapsed = file.readlines()
                #Stop at first empty line
                module_elapsed = module_elapsed[:module_elapsed.index('\n')]   
        return module_elapsed

#Find most expensive SQL (CPU Time)
def find_SQLs_CPU(file, second_condition):
    with open(file, "r") as file:
        for num, line in enumerate(file, 1):
            if num == second_condition + 8:
                #Store lines in a list  
                module_cpu = file.readlines()
                #Stop at first empty line
                module_cpu = module_cpu[:module_cpu.index('\n')]   
        return module_cpu

#Store most expensive SQL
module_elapsed = find_SQLs_Elapsed(file, first_condition)
module_cpu = find_SQLs_CPU(file, second_condition)

# Print table
def print_table(module_elapsed, module_cpu, total_elapsed, total_cpu):
    #Elapsed table
    table_elapsed = pt.PrettyTable()
    #Add column
    table_elapsed.field_names = ["SQL ID","%Total Elapsed Time"]
    #Add rows
    table_elapsed.add_row([module_elapsed, total_elapsed]),
    #Print table
    print(table_elapsed)
    
    #Cpu table
    table_cpu = pt.PrettyTable()
    #Add column
    table_cpu.field_names = ["SQL ID","%Total CPU Time"]
    #Add rows
    table_cpu.add_row([module_cpu, total_cpu]),
    #Print table
    print(table_cpu)    

