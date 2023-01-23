import random

upper_cases = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_cases = upper_cases.lower()
digits = "123456789"
symbols = "@#/.,*-&<>"

length = int(input("How long you want your password to be (Enter Number of Characters): "))
ans = upper_cases + lower_cases + digits + symbols

password = "".join(random.sample(ans, length))

print("Your Password is Generated: " + password)