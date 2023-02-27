num_list = [-99,56,7,-54,-4,87,39]
num_lists = [-99,56,7,-54,-4,87,39]
sortAscending = []
sortDescending = []

while num_list:
    minimum = num_list[0]
    for x in num_list:
        if x < minimum:
            minimum = x
    sortAscending.append(minimum)
    num_list.remove(minimum)
    
while num_lists:
    maximum = num_lists[0]
    for j in num_lists:
        if j > maximum:
            maximum = j
    sortDescending.append(maximum)
    num_lists.remove(maximum)
    
print( "Ascending order", sortAscending)
print( "Decending order", sortDescending)
