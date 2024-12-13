string = input("enter the string")
string1=string.lower()
if string1[::-1]==string:
    print("yes your string is a palindrome ")
else:
    print("sorry")