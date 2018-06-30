def com(n, r):
  if n - r < r:
    return com(n, n - r)
  child = 1
  mother = 1
  for i in range(r):
    child *= n - i
    mother *= r - i
  return child / mother

def calc_from_players(n):
  max = 45
  result = 1
  for i in range(n):
    result *= com(max - (2 * i), 2)
  return result

for j in range(5):
  i = j + 1
  print("other({1}) = {0:d}".format(int(calc_from_players(i)), i))