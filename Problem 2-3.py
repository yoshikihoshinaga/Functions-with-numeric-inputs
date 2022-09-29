# Functions with numeric inputs
#Author:Yoshiki Hoshinaga
#Date: May 21 2020
#

# function 0
def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1*x

# put your definitions for the remaining functions below

#problem 1
def first_and_last(values):
    """put your docstring here"""
    first = values[0]
    last = values[-1]
    return [first, last]

# problem 2
def longer_len(s1, s2):
    """put your docstring here"""
    len1 = len(s1)
    len2 = len(s2)
    if(len1>len2):
        return len1
    else:
        return len2

#problem 3
def move_to_end(a,b):
    if (b>len(a)):
        return a
    else:
        return (a[b:] + a[0:b])




# optional but encouraged: add test calls for your functions, indented below
if __name__ == '__main__':
        
    # sample test call for function 0
    #print('opposite(-8) returns', opposite(-8))

    #print for problem 1
    print('first_and_last([1,2,3,99])',first_and_last([1,2,3,99]))
    print('first_and_last([7])',first_and_last([7]))
    print(first_and_last(['how','are','you']))

    #print for problem 2
    print(longer_len('computer','compute'))
    print(longer_len('hi', 'hello'))
    print(longer_len('begin','on'))

    #print for problem 3
    print(move_to_end('computer',3))
    print(move_to_end('computer',5))
    print(move_to_end('computer',0))
