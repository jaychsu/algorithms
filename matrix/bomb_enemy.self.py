# Given a 2D grid, each cell is either a wall 'W',
# an enemy 'E' or empty '0' (the number zero),
# return the maximum enemies you can kill using one bomb.
# The bomb kills all the enemies in the same row and column from
# the planted point until it hits the wall since the wall is too strong
# to be destroyed.
# Note that you can only put the bomb at an empty cell.

# Example:
# For the given grid

# 0 E 0 0
# E 0 W E
# 0 E 0 0

# return 3. (Placing a bomb at (1,1) kills 3 enemies)

def kill_max_enemies(grid):
  if not grid: return 0

  result = {
    'planted_point': (0, 0),
    'killed_enemies': 0,
  }

  m, n = len(grid), len(grid[0])

  for i in range(m):
    for j in range(n):
      print(grid[i][j])

  return result

# def kill_in_row(grid, i, j):

# def kill_in_col(grid, i, j):

m = [
  ['0', 'E', '0', '0'],
  ['E', '0', 'W', 'E'],
  ['0', 'E', '0', '0'],
]
result = kill_max_enemies(m)
msg = 'Placing a bomb at {a} kills {b} enemies'.format(a=result['planted_point'], b=result['killed_enemies'])
print(msg)
