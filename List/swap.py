List = [23, 65, 19, 90]
pos1,pos2 = 1,3
def swap_position(my_list,pos1,pos2):
    my_list[pos1], my_list[pos2] = my_list[pos2],my_list[pos1]
    return my_list
    
print(swap_position(List,pos1-1,pos2-1))