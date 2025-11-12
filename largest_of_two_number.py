def largest_of_two_number():
  number1=int(input("enter the number"))
  number2=int(input("enter the number"))
  if number1>number2 and number2<number1:
    print("number1 is greater")
    print(number1)
  else:
    print("smaller")
  return number1,number2
largest_of_two_number()
enter the number50
enter the number25
number1 is greater
50
(50, 25)
