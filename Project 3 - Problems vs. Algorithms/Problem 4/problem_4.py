"""
Dutch National Flag Problem
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.
"""

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    # Check if input_list is too short
    if len(input_list) <= 1 or input_list is None:
        return input_list
    
    end_0 = 0
    end_1 = 0
    start_2 = len(input_list) - 1
    
    # Loop through until position of 2 starts equal to end position of 1s
    while end_1 <= start_2:
           if input_list[end_1] == 0:
                  # if the current end location of zero have non-zero value, swap it with end_1 value
                  if input_list[end_0] != 0:
                         input_list[end_0], input_list[end_1] =  input_list[end_1], input_list[end_0]
                  end_0 += 1
                  end_1 += 1
           elif input_list[end_1] == 1:
                  end_1 += 1
           elif input_list[end_1] == 2: 
                  # Swap end_1 position with end_2 position
                  if input_list[start_2] != 2:
                         input_list[end_1], input_list[start_2] =  input_list[start_2], input_list[end_1]
                  # move down 1 index for 
                  start_2 -= 1
           
    return input_list
                  
def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

# Normal Case
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])


# Edge Case
test_function([0,0,0,0,0])
test_function([1,1,1,1,1])
test_function([2,2,2,2,2])
test_function([0])
test_function([])