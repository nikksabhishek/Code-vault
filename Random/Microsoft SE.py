"""
Given an array of integers, arrange the array according to descending order of repetition of elements.



For example, if the input array is {2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12}, then modify the array to {3, 3, 3, 3, 2, 2, 2, 12, 12, 4, 5}.



If frequencies of two elements are same, print them in increasing order.



Write the program for above statement along with unit test cases for 100% Branch and Statement Coverage

"""
from collections import defaultdict
import coverage

# def string_check(input_array):
#     try:
#         for element in input_array:
#             if element.isalpha():
#                 return True
#         return False
#     except Exception as e:
#         print (" Error in string_check : "+str(e))

def arrange_elements(input_array):
    try:
        # if string_check(input_array):
        #     return 'Expected input : Integers'
        if input_array:
            freq_dict = {}
            for element in input_array:
                if element not in freq_dict.keys():
                    freq_dict[element] = 1
                else:
                    freq_dict[element] += 1

            res = defaultdict(list)
            for key, val in sorted(freq_dict.items()):
                res[val].append(key)

            output_array = []    
            while res:
                key = max(res, key=int)
                if len(res[key]) > 1: 
                    for item in res[key]:
                        output_array.extend([item]*key)
                else:
                    output_array.extend(res[key]*key)
                res.pop(key)
            return output_array
        else:
            return 'Empty input array'
    except Exception as e:
        print ("Exception in arrange_elements function : "+str(e))

import unittest

class TestStringMethods(unittest.TestCase):

    def test_arrange_default(self):
        self.assertEqual(arrange_elements([2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12]), [3, 3, 3, 3, 2, 2, 2, 12, 12, 4, 5])

    def test_arrange_pattern1(self):
        self.assertEqual(arrange_elements([2, 2, 2, 4, 5, 12, 2, 3, 3, 3, 12]), [2, 2, 2, 2, 3, 3, 3, 12, 12, 4, 5])

    def test_arrange_pattern2(self):
        self.assertEqual(arrange_elements([2, 2, 2, 3, 3, 3, 12]), [2, 2, 2, 3, 3, 3, 12])

    def test_arrange_sortedList_ascendingOrder(self):
        self.assertEqual(arrange_elements([1, 2, 3, 4, 5, 6, 7]), [1, 2, 3, 4, 5, 6, 7])

    def test_arrange_sortedList_descendingOrder(self):
        self.assertEqual(arrange_elements([7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7])
    
    def test_arrange_null(self):
        self.assertEqual(arrange_elements([]), 'Empty input array')

if __name__ == '__main__':
    unittest.main()