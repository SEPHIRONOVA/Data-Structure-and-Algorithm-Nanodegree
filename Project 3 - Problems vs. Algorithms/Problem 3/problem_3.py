"""
Rearrange Array Elements
Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

"""

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    
    # Trasverse
    while left_index < len(left) and right_index < len(right):
        # If right's item is larger, append right's item and increment index
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        # Otherwise, append left's item and increment
        else:
            merged.append(left[left_index])
            left_index += 1
     
    # Append the rest
    merged += left[left_index:]
    merged += right[right_index:]
        
    # return the ordered, merged list
    return merged
       
def mergesort(items):

    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left, right)

       
def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) <= 1:
           print("The length of list is too small to sort")
           return
    
    first_num = ""
    second_num = ""
    
    # Sort the array first
    sorted_list = mergesort(input_list)
    
    
    for i in range(0, len(sorted_list), 2):
          first_num += str(sorted_list[i])
          
    for j in range(1, len(sorted_list), 2):
          second_num += str(sorted_list[j])
          
    return [int(first_num), int(second_num)]
           

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    print(output)
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_case_1 = [[1, 2, 3, 4, 5], [542, 31]]
test_function(test_case_1)
test_case_2 = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case_2)

# Edge Case
edge_case_1 = []
rearrange_digits(edge_case_1)
# The length of list is too small to sort

edge_case_2 = [1]
rearrange_digits(edge_case_2)
# The length of list is too small to sort