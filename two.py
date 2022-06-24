# from turtle import left, right





s=["h","e","l","l","0"]
left=0
right=len(s)-1
while left > right:
    hold=s[left]=s[right]
    s=right=hold
    left+=1
    right-=1 

    s="axc"
    t="ahdc"
    spointer=0
    tpointer=0
    while spointer<len(s) and tpointer < len(t):
        if s[spointer] == [tpointer]:
            spointer+=1
            tpointer+=1
            print(spointer)
           
        

a="I am Akirachix"
a.split()
start=0
end=len(a)-1
while start < end:
    a[start],a[end]= a[end],a[start]
    start+=1
    end-=1
    str=""
print(a.join(str))

        


