string  = "IMPORTANT"

def reverse_alternate(string,d):

    new_string = ""
    string_arr = []

    for i in range(0,len(string),d):
        string_arr.append(string[i:i+d])

    for i in range(len(string_arr)):
        new_string += string_arr[i][::-1]

    return new_string

print(string+ " -> " +reverse_alternate(string,2))
