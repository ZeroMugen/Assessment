num_list = [-99,56,7,-54,-4,87,39] 
num_lists = [-99,56,7,-54,-4,87,39] 
sortAscending = [] 
sortDescending = []
#made two different varibles with the same array for acension and decension and declared the functions for output. To avoid using builtin function, utilized while loop.


#while loop reads the numbers in the num_list array. The way the computer reads the program is that it will start with the first number in the array and compare it with the next and will check which number is less than the other. If the number compared is less it will be replaced with the lesser number with the append call. And then number would be remove from the num_list to avoid duplication. then repeats until there is nothing to compare.  
while num_list:
    minimum = num_list[0]
    for x in num_list:
        if x < minimum:
            minimum = x
    sortAscending.append(minimum)
    num_list.remove(minimum)
    


#while loop for the decension order. Process is the same as above except the direction is reversed.
while num_lists:
    maximum = num_lists[0]
    for j in num_lists:
        if j > maximum:
            maximum = j
    sortDescending.append(maximum)
    num_lists.remove(maximum)
    



#outputs the order arranged after the while loop 
print( "Ascending order", sortAscending)
print( "Decending order", sortDescending)

