#Author:Yoshiki Hoshinaga
#Date: May 21 2020


# function 0
def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1*x

# put your definitions for the remaining functions below

# function 1
def cube(x):
    """compute the volume of a cube with x"""
    return x**3


# function 2
def convert_to_inches(yard,feet):
    """Compute the converting to inches from yard and feet"""
    if yard<0:
        yard =0
    if feet<0:
        feet =0
    yard = yard * 36
    feet = feet * 12
    return yard + feet


#function 3
def area_sq_inches(height_yds, height_ft, width_yrs, width_ft):
    """Compute the area of square by inches"""
    if height_yds<0:
        height_yds=0
    if height_ft<0:
        height_ft=0
    if width_yrs<0:
        width_yrs=0
    if width_ft<0:
        width_ft=0
    height_yds = height_yds * 36
    height_ft = height_ft * 12
    width_yrs = width_yrs * 36
    width_ft = width_ft *12
    return ((height_yds + height_ft)*(width_yrs + width_ft))


# optional but encouraged: add test calls for your functions, indented below
if __name__ == '__main__':
        
    # sample test call for function 0
    #print('opposite(-8) returns', opposite(-8))
    print('cube(2) is',cube(2))
    print('convert_to_inches(-4,2) is', convert_to_inches(-4,2))
    print('area_sq_inches(1,2,3,1) is',area_sq_inches(1,2,3,1))


