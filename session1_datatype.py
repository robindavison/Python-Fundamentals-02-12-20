## integer
x = 1
print("x=",x)

## Decimal
x1 = 1.3
print("x=",x,"x1=",x1)

## String
x2 ="This is some text"
print("x=",x,"x1=",x1, "x2=", x2)

# Boolean
x3=False
x4=True
print("x=",x,"x1=",x1, "x2=", x2, "x3=",x3,"x4=",x4)

# List (arrays) 1st index = 0
l1 = [1,2,3,4,5,6,7,8,9,10]
print(l1)            # whole list
print("l[0]=",l1[0]) # individual item

# Mixed list
l2 =[1,"hello", True, 0, 2]

# length of list
print(len(l2))
# Add to end of list
l2.append("Robin")
print(l2)

#set element
l2[0] = 666
print(l2)

# remove element by value
l2.remove(666)
print(l2)

# remove by index
l2.pop(0)
print(l2)

# remove by index different method
del l2[0]
print(l2)

# dictionary - named array entries
d1={
    "Name": "Dog",
    "Height": 2,
    }
print(d1["Name"],d1["Height"])

# Dictionaries with lists
d2 = {
    "Name": "Dog",
    "Races": ["Pug", "Bulldog", "Spaniel"]
}
print(d2)

# List with dictionaries
l3=[d1,d2,{"Name":"Fred", "Height":5}]
print(l3)

# dictionary within dictionary
d3 = {
    "Name": "Wolf Pack",
    "Wolves": [{"Name":"Huey", "Colour":"Brown"},
               {"Name":"Duey", "Colour":"Grey"}
               ],
    "a":{"b":1,"c":2}
}

print(d3["Wolves"][0])
print(d3["Wolves"][0]["Colour"])

wolves = d3["Wolves"]
wolves_1 = d3["Wolves"][0]
wolves_2 = d3["Wolves"][1]
print("All of wolves",wolves)
print("Wolf 1",wolves_1)
print("Wolf 2",wolves_2)

wolf_1_colour = wolves_1["Colour"]
print(wolf_1_colour)


print(d3["a"]["c"])


# ############## Practice 1
person_name = "Robin"
person_age = 666
person_job = "SI&T Design Engineer"

person_details = {
    "name": person_name,
    "age": person_age,
    "job": person_job
}

print(person_details)
print("Name =", person_details["name"], "Age =",person_details["age"], "Job =",person_details["job"])
