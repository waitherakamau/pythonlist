# write a program to check for palidrome
#  a palindrome is a worsd or a number that read s the same forward or backwards
# madam
user=input("Enter the value:")
# introduce slicing
reverse=user[::-1]
if(user==reverse):
    print("yes it is a palindrome")
else:
    print("it is not a palindrome")




str="tot"
start=0
last=len(str)-1
while start < last:
    [start],[last]=[last],[start]
    start+=1
    last-=1
    x=""
    print(x.join(str))
