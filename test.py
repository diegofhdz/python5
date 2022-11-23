import re


with open("name.txt", 'r') as f:
    all_lines = f.readlines()


find_name = re.compile(r"^[A-Z][a-zA-Z]+, [A-Z][a-zA-Z]+")
find_handle = re.compile(r"@[a-z]+$")

names = []
handles = []



for line in all_lines:
    found_name = find_name.search(line)
    found_handle = find_handle.search(line)
    if found_handle:
        name_start =found_name.span()[0]
        name_end = found_name.span()[1]
        names.append(line[name_start : name_end])
        handle_start = found_handle.span()[0]
        handle_end = found_handle.span()[1]
        handles.append(line[handle_start : handle_end])


def print_all(names_list, handles_list):

    print("=================")
    print("Full Name/Twitter")
    print("=================")
    
    for i in range(len(names_list)):
        print(names_list[i], "/", handles_list[i], end="\n")


print_all(names, handles)