#list
#
def list_number():
    list=[2,4,6,8]
    list.pop(2)
    return list
print(list_number())

days=["mon","tue","fri","mon"]
print(days.count("mon"))

def divisible_by_seven():
    for x in range(100,200):
      if x%7==0:
        print(x)
        
divisible_by_seven()
 
num1=int(input("enter number"))
num2=int(input("enter number"))
sum=num1+num2
if sum >10:
    print("greater")
elif sum<10:
    print("less")
else:
    sum==10
    print("equal")

list=[1,2,3,4,5,]
if 4 in list:
    print(True)
else:
    print(False)

def list_fruits():
    list=["apples","grapes","pinneaple",]
    list.pop(2)
    return list
print(list_fruits())

cars=["ford","volvo","Bmw"]
cars.sort()
print(cars)

list=[4,5,2,6,1,7]
list.remove(min(list))
print(list)

def smallest():
    list[3,4,8,6,5,1,9]
    small=list[0]
    for x in list:
        if x<small:
            samll=x
            print(x)
smallest()
    







