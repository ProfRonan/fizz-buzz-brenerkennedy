inteiro = int(input("digite um valor inteiro"))
if(inteiro%3 == 0 and inteiro%5 != 0):
    print("Fizz")
elif(inteiro%3 != 0 and inteiro%5 == 0):
    print("Buzz")
elif(inteiro%3 == 0 and inteiro %5 == 0):
    print("FizzBuzz")
else:
    print(inteiro)
