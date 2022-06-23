from operator import length_hint


course="python programing"
print(len(course))
print(course[0])
print(course[-1])

#slice the string
print(course[0:3])
print(course[0:])
print(course[:3])


chapter="python\nprograming"
print(chapter)

cars="i love Audi.I enjoy driving Audi"
# replace Audi with jeep
new_text=cars.replace("Audi","jeep")
print(new_text)

# /n prints a newline
workers="job \n jobless"
print(workers)

# Given two variables first an last print variable in full
first="Effence"
last="Kamau"
full=first +""+ last
print(full)
# format 
first="Effence"
last="Kamau"
full=f"{first} {last}"
print(full)
# get the length
first="Effence"
last="Kamau"
full=f"{len(first)} {last}"

# slicing
s="cinema"
s[2:5]







string1="childrenareplaying" 
print(string1[0:len(string1)//2]+ string1[len(string1)//2:].upper())

