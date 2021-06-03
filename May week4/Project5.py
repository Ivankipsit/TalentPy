"""
Create three functions as follows -
    1. def remove_vowels(string) - which will remove all vowels from the given
string. For example if the string given is “aeiru”, then the return value should
be ‘r’
    2. def remove_consonants(string) - which will remove all consonants from
given string. For example, if the string given is “aeri”, then the return value
should be ‘aei’.
    3. def caller -> This function should 2 parameters
        1. Function to call
        2. String argument
        This caller function should call the function passed as a parameter, by
passing second parameter as the input for the function. Example: caller(remove_vowles,
“aeiru”) should call remove_vowels function and should return ‘r’ as the output.
"""

def remove_vowels(string):
    vowels_list = list("aeiou")
    string_list = list(string[0]) #aeri
    return_list = [string_list[i] for i in range(len(string_list)) if (string_list[i] in vowels_list) == False]
    return return_list
    
def remove_consonants(string):
    consonants_list = list("qwrtyplkjhgfdszxcvbnm")
    string_list = list(string[0])
    return_list = [string_list[i] for i in range(len(string_list)) if (string_list[i] in consonants_list) == False]
    return return_list

string1 = input("Enter string: ")
string = []
string.append(string1)
print(string)
print("remove_vowels or remove_consonants")
choice = input("Enter your choice: ")
if choice == "remove_vowels":
    print("".join(map(remove_vowels,string1)))
else:
    print("".join(map(remove_consonants,string1)))


