"""
Max and Min in a Unsorted Array
In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. 
Do not use Python's inbuilt functions to find min and max.
"""

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    
    # Check for emptiness
    if len(ints) == 0:
           return (None, None)
    
    minimum, maximum = ints[0], ints[-1]
    
    for number in ints:
           if number < minimum:
                  minimum = number
           
           if number > maximum:
                  maximum = number
                  
    return (minimum, maximum)
    
## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

print ("Pass" if ((-2, 90) == get_min_max([-2,3,90])) else "Fail")

# Edge Case
# Empty
print ("Pass" if ((None, None) == get_min_max([])) else "Fail")
# Only 1 item that min = max
print ("Pass" if ((1, 1) == get_min_max([1])) else "Fail")