def func1():
    print("Hello world")


for x in range(1):
    func1()


def sausage_maker(pig):
    return "sausages of " + pig


sausage = sausage_maker("frog")

print(sausage)
print(sausage_maker("elephant"))


def print_add(x1, y):
    print("Sum =", x1 + y)


print_add(2, 3)


def add(x2, y):
    return x2 + y


print(add(3, 7))

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [23, 34, 7567, 35, 124, 1]


def operation_by_2(input_list, operator):
    return_list = []
    for process_list in input_list:
        if operator == "*":
            return_list.append(process_list * 2)
        else:
            return_list.append(process_list / 2)
    return return_list


print('List multiplied by 2 = ', operation_by_2(l1, "*"))
print('List divided by 2 = ', operation_by_2(l1, "/"))
print('List multiplied by 2 = ', operation_by_2(l2, "*"))
print('List divided by 2 = ', operation_by_2(l2, "/"))

marco = {
    "name": "Marco",
    "age": 30,
    "gender": "male"
}
sofia = {
    "name": "Sofia",
    "age": 10,
    "gender": "Female"
}


def is_male(person):
    if person["gender"] == "male":
        return True
    else:
        return False


def is_female(person):
    if person["gender"] == "Female":
        return True
    else:
        return False


print(marco["name"], "male = ", is_male(marco))
print(sofia["name"], "male = ", is_male(sofia))
print(marco["name"], "female = ", is_female(marco))
print(sofia["name"], "female = ", is_female(sofia))


def age_more_than_30(person):
    if person["age"] > 30:
        return True
    else:
        return False


print(marco["name"], "age more than 30 =", age_more_than_30(marco))
print(sofia["name"], "age more than 30 =", age_more_than_30(sofia))

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def div_by_2(input_list):
    return_list = []
    for process_list in input_list:
        if process_list % 2 == 0:
            return_list.append(process_list)
    return return_list


print("List divisible by 2", div_by_2(l1))

people = [
    marco,
    sofia,
    {
        "name": "Lucas",
        "age": 40,
        "gender": "male"
    }
]


def male_people_over_30(list_of_people):
    new_list = []
    for values in list_of_people:
        if age_more_than_30(values) and is_male(values):
            new_list.append(values)
    return new_list


print("Male people over 30 =", male_people_over_30(people))
