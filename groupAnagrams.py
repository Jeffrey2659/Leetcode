'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.'''



# My Solution( This works)
from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :

        """
        #automatically creates an empty list if the key doesn’t exist.
        my_dict = defaultdict(list)
        arr = []
        n_str =[]
        
        for i in strs:
            n_str.append("".join(sorted(i)))

        for j in range(len(n_str)):
            my_dict[n_str[j]].append(strs[j])

        for values in my_dict.values():
            arr.append(values)


        return arr
    


    #Optimal solution


    from collections import defaultdict

def group_anagrams_sort(strs):
    groups = defaultdict(list)
    for s in strs:
        key = "".join(sorted(s))  # canonical form
        groups[key].append(s)
    return list(groups.values())

