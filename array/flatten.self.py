"""
Implement Flatten Arrays.
Given an array that may contain nested arrays,
give a single resultant array.

function flatten(input){
}

Example:

Input: var input = [2, 1, [3, [4, 5], 6], 7, [8]];
flatten(input);
Output: [2, 1, 3, 4, 5, 6, 7, 8]
"""

def list_flatten(arr, init_arr=None):
  result = list(init_arr) if isinstance(init_arr, (tuple, list)) else []

  for el in arr:
    if isinstance(el, (tuple, list)):
      result = list_flatten(el, result)
    else:
      result.append(el)

  return result

result = list_flatten([2, 1, [3, [4, 5], 6], 7, [8]])
print(result)
