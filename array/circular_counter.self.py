"""
There are people sitting in a circular fashion,
print every third member while removing them,
the next counter starts immediately after the member is removed.
Print till all the members are exhausted.

For example:
Input: consider 123456789 members sitting in a circular fashion,
Output: 369485271
"""

def pickByGutter(int_list, gutter):
  gutter = gutter - 1
  index = 0

  while len(int_list) > 0:
    index = (index + gutter)%len(int_list)
    print(int_list.pop(index))

lists = [i for i in range(1,10)]
print(lists)
pickByGutter(lists, 3)
