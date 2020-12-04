
name1 = "Bill"
name2 = "Ben"

if name1 == name2:
    print("name1 equals")
else:
    print("name1 not equal")

if name1 != name2:
    print("name1 not equal")
else:
    print("name1 equals")

x1 = 2

if x1 == 1:
    print("=1")
elif x1 >= 2:
    print("x1 greater than or equals 2")
elif x1 > 1:
    print("x1 greater than 1")
else:
    print("Something else")

# For loops
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in l1:
    print(item, " * 2 = ", item * 2)

for i, item in enumerate(l1):
    print(i, "->", l1[i], " * 2 =", l1[i] * 2)

# Practice 3
practice_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []
for item in practice_list:
    new_list.append(item * 2)
print("New List =", new_list)

names1 = ["Marco", "George", "Kieran", "Robin"]
names2 = []
for item in names1:
    names2.append(item)
print("Names2=", names2)

ages2 = [10, 20, 40, 30, 10, 57]
ages3 = []
for item in ages2:
    if item < 30:
        ages3.append(item)
print("Ages3 =", ages3)

people1 = [
    {
        "name": "Marco",
        "age": 30
    },
    {
        "name": "Kieran",
        "age": 20
    },
    {
        "name": "Robin",
        "age": 10
    },
    {
        "name": "George",
        "age": 40
    }
]
people_over_30 = []
people_below_30 = []
people_equals_30 = []
for item in people1:
    if item["age"] > 30:
        people_over_30.append(item)
    elif item["age"] < 30:
        people_below_30.append(item)
    else:
        people_equals_30.append(item)
print("People_over_30=", people_over_30)
print("People_below_30=", people_below_30)
print("People_equals_30=", people_equals_30)

people_over_30 = [p for p in people1 if p["age"] > 30]
print("People_over_30=", people_over_30)
