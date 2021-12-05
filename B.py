S1 = input()
S2 = input()

SS = S1 + S2

if SS.count('#') >= 3 or SS.count('#') == 1:
  print('Yes')
else:
  S1 = list(S1)
  S2 = list(S2)

  if S1[0] == S2[1] or S1[1] == S2[0]:
    print('No')
  else:
    print('Yes')
