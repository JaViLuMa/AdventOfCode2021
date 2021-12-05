for _ in range(int(input())):
  n = int(input())

  if n % 2 == 0:
    print(0)
  else:
    counter = 0

    for x in str(n):
      if int(x) % 2 != 0:
        counter += 1

    if counter == len(str(n)):
      print(-1)
    else:
      if int(str(n)[0]) % 2 == 0:
        print(1)
      else:
        print(2)
