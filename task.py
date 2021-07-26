# Given a sorted integer array where the range of elements are [lower, upper] inclusive, return its missing ranges.
# For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].

from typing import List

def make_range(left : int,right : int) -> str:
    if left == right:
        return str(right)
    else:
        return str(left) + ' -> ' + str(right)
    

def return_missing_values(array : List,lower : int, upper: int) -> List:
    
    result_list = []
    
    if array:
        prev_num = array[0]
        for value in array:
            if prev_num != value and value - 1 != prev_num:                     
                result_list.append(make_range(prev_num + 1, value - 1))
                prev_num = value                
            else:
                prev_num = value   
                      
        if array[-1] != upper:
                missing = make_range(array[-1] + 1, upper)
                result_list.append(missing)

    else:
        result_list.append(make_range(lower,upper))


    return result_list



print(return_missing_values(array=[0, 1, 3, 50, 75],lower=0,upper=99))