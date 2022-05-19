while True:
  string = input()
  bracket = []
  error_flag = False

  if string == '.':
    break
  
  for char in string:
    if char == '[' or char == '(':
      bracket.append(char)
    if char == ')':
      if len(bracket) > 0 and bracket[-1] == '(':
        bracket.pop()
      else:
        error_flag = True
        break
    if char == ']':
      if len(bracket) > 0 and bracket[-1] == '[':
        bracket.pop()
      else:
        error_flag = True
        break
  if len(bracket) == 0 and error_flag == False:
    print('yes')
  else:
    print('no')