
# Functions with numeric inputs
#Author:Yoshiki Hoshinaga
#Date: May 21 2020
#Title: Problem Set2, Part 4
#

#problem 1
def mirror(s):
    return s + s[::-1]

#probelm 2
def is_mirror(s):
    if(s==s[::-1]):
        return True
    else:
        return False
#problem 3

def replace_end(values, new_end_values):
    new_values=  values[:len(values)-len(new_end_values)]
    return new_values + new_end_values

#problem 4
           
def repeat_elem(values, index, num_times):
    new_values = values[:index]
    new_lists = [values[index]]* num_times + values[index+1:]
    return new_values + new_lists


    
#print for problem 1
print(mirror('bacon'))
print(mirror('XYZ'))

#print for problem 2
print(is_mirror('baconnocab'))
print(is_mirror('baconnoca'))

#print for problem 3
print(replace_end([1,2,3,4,5],[7,8,9]))
print(replace_end([1,2,3,4,5],[10,11]))
print(replace_end([1,2,3,4,5],[12]))
print(replace_end([0,2,4,6],[4,3,2,1]))


#print for problem 4
print(repeat_elem([10,11,12,13],2,4))
print(repeat_elem([10,11,12,13],2,6))
print(repeat_elem([5,6,7],1,3))
