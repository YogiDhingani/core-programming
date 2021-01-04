array_of_string = []
string = input("Enter your numbers in COMMA SEPARATED FORMAT : ")

def largest(array_of_string):

    array_of_numbers = []

    array_of_string.append(string)

    for i in range(0,len(array_of_string)):
        for n in array_of_string[i].split(","):
            array_of_numbers.append(int(n))

    max = array_of_numbers[0]

    for i in range(0,len(array_of_numbers)):
        if array_of_numbers[i] > max:
            max = array_of_numbers[i]
    
    return max

print("Largest number is:",largest(array_of_string))




