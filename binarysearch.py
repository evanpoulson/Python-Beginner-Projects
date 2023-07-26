from random import randint
#script which runs a binary search on a list of numbers from least to greatest
def binary_search(lst, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(lst) - 1
    if high < low:
        return -1
    
    midpoint_index = (low + high) //2

    if lst[midpoint_index] == target:
        return midpoint_index
    elif target < lst[midpoint_index]:
        return binary_search(lst, target, low, midpoint_index - 1)
    elif target > lst[midpoint_index]:
        return binary_search(lst, target, midpoint_index + 1, high)
    
#build a random list
length = 100000
sorted_list = set()
while len(sorted_list) < length:
    sorted_list.add(randint(-5*length, 5*length))
sorted_list = sorted(list(sorted_list))

print(binary_search(sorted_list, 5))