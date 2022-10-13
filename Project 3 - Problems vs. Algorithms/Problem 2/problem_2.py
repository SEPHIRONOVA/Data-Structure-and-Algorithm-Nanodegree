"""
Search in a Rotated Sorted Array
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4
"""

def array_search_recursive(array, target, start, end):
    """
    Recursively find the target value

    Args:
       input_list(array), number(int), start, end: Input array to search, the target, start index and end index
    Returns:
       int: Index or -1
    """
    if start > end:
           return -1
    
    mid_index = (start + end) // 2
    mid_num = array[mid_index]
    
    if target == mid_num:
           return mid_index
    
    left_result = array_search_recursive(array, target, start, mid_index - 1)
    right_result = array_search_recursive(array, target, mid_index + 1, end)
    
    # Use max function to find out true result if there is one(The other one will be -1 or both -1 means didn't find it)
    return max(left_result, right_result)
    
    
def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    start = 0
    end = len(input_list) - 1
    
    return array_search_recursive(input_list, number, start, end)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

# Test

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# Edge Case
test_function([[], -1])
test_function([[-5,-6], 0])
