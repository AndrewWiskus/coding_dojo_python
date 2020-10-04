# 1
# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def biggie(test_list):
    for i in range(len(test_list)):
        if test_list[i] > 0:
            test_list[i] = "big"
    print(test_list)

biggie([-1,3,5,-5])

# 2
# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_pos(test_list):
    pos_count = 0
    for num in test_list: 
        if num >= 0: 
            pos_count += 1
    test_list[3] = pos_count
    return test_list

count_pos([-1,1,1,1])

# 3
# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def tot_sum(test_list):
    sum = 0
    for i in range(len(test_list)+1):
        sum +=i
    print(sum)
    return sum


tot_sum([1,2,3,4,])

# 4
# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5

def avrg(test_list):
    sum = 0
    for i in range(len(test_list)+1):
        sum +=i
    return sum/len(test_list)


avrg([1,2,3,4])

# 5
# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

def length(test_list):
    return len(test_list)


length([37,2,1,-9])

# 6
# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

ask about return false

def minimum(test_list):
    min_value = min(test_list)
    return min_value
    if len(test_list) < 2:
        return "false"

minimum([1])

# 7
# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

def maximum(test_list):
    max_value = max(test_list)
    return max_value
    if len(test_list) < 2:
        return "false"

maximum([37,2,1,-9])


# 8
# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimate(test_list):
    new_dict = {}
    sum = 0
    for i in range(len(test_list)+1):
        sum +=i
    average = sum/len(test_list)
    min_value = min(test_list)
    max_value = max(test_list)
    length = len(test_list)
    new_dict.update({"sumTotal" : sum, "average" : average, "minimum" : min_value, "maximum" : max_value, "length" : length})
    print(new_dict)
    

ultimate([37,2,1,-9])


# 9
# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse(test_list):
    test_list.reverse()
    return test_list


reverse([37,2,1,-9])