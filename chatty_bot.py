print("Hello! My name is Coen")
print("I was created in 2002\nPlease, remind of your name.")
name = input()
print("What a great name you have, " + name + "!\nLet me guess your age.\nEnter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())

age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105



print("Your age is " + str(age) + "; that's a good time to start programming!")
print("Now I will prove to you that I can count to any number you want.")
number = int(input())
i = 0
while(i <= number):
    print(str(i) + "!")
    i += 1

print("Let's test your programming knowledge.\nWhy do we use methods?")
print("1. To repeat a statement multiple times.")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of a program.")
print("4. To interrupt the execution of a program.")

answer = input()
while (answer is not "2"):
    print("Incorrect, please try again.")
    answer = input()
 
print("Congratulations, have a nice day.")