
# display a descriptive message about the program 
print("----------------------Welcome To Statistical Analysis Program---------------------- ")

print("This program will analyze the numbers you provide and compute useful statistics.")
# prompt to enter numbers 
print("--- Enter the numbers you want to analyze. Enter -1 when you are finished. ---")
# creating empty list to later store numbers in 
number_list = [] 
# entering numbers in list 
# using try / except to provide correctness in input values
while True:
    try:
       number= int(input('Enter a number '))
       if number == -1 :
           break 
       number_list.append(number)    
    except ValueError  :
        print("Invalid Input : please enter a valid  integer  ") 
# creating  dictionary to compute frequency of numbers 
number_dictionary = {}
# using the get method to increment the value of the dictionary number 
for number in number_list:
    if number not in number_dictionary:
        number_dictionary[number] = 1
    else:
        number_dictionary[number] = number_dictionary.get(number) +1 

# displaying numbers and its frequency 
print("The numbers you entered : "  , number_list)
print("Frequency of each number: "  , number_dictionary)

# display statistical report 
# 
print('### Statistical Report ###')
# display a note for empty list 
# display statistical report for nonempty list 
if not  number_list:
    print("No numbers were entered. Unable to generate a statistical report.")
else:    
    print('Maximum number : ' , max(number_list))
    print('Minimum number : ' , min(number_list))
    print(' Total Sum :' , sum(number_list))
    print('Average : ' , sum(number_list) / len(number_list))


