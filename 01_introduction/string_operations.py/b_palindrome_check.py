name = str(input())
name_rev = name[::-1]
if name==name_rev:
    print("given string is a palindrome")

else:
    print("not a palindrome")