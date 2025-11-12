def factorial():
  number=int(input("enter the number"))
  factorial=1
  for a in range(1,number+1):
    factorial*=a
  return factorial
factorial()
enter the number10
3628800
