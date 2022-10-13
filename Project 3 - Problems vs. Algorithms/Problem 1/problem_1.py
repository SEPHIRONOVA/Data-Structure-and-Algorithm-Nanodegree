"""
Finding the Square Root of an Integer
Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))
"""

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    
    if number < 0:
        print("Please enter a positive integer")
        
        return None
 
    if number <= 1:
        return number
    
    test_start = 1
    test_end = number
    
    while test_start <= test_end:
        mid = (test_start + test_end) // 2
        mid_squared = mid * mid
        
        if mid_squared == number:
             return mid
        elif mid_squared < number:
             test_start = mid + 1
             output = mid
        else:
             test_end = mid - 1
              
    return output
    
# Test

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

# Edge Case
print ("Pass" if  (None == sqrt(-1)) else "Fail") # Will also print "Please enter a positive integer
print ("Pass" if  (0 == sqrt(0)) else "Fail")
