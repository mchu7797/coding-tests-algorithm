n = int(input())
test_case = []

for _ in range(n):
  test_case.append(input())

for string in test_case:
  stack = []
  error = False
  for char in string:
    if char == '(':
      stack.append(char)
    if char == ')':
      if len(stack) != 0:
        stack.pop()
      else:
        error = True
        break
  if len(stack) == 0 and error == False:
    print('YES')
  else:
    print('NO')