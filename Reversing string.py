# define the function
def reverse_string(string):
    reversed_str=""
    #A loop to go through the characters from the end index to the start index
    for i in range (len(string)-1,-1,-1):
        reversed_str+=string[i]#Add the characters to the empty string
    return reversed_str
print(reverse_string("Nicole"))