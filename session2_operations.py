print("1+1=", 1+1)

x1=1
x2=2
print("x1+x2=",x1+x2)
print("x1-x2=",x1-x2)
print("x1*x2=",x1*x2)
print("x1/x2=",x1/x2)
print("x1%x2=",x1%x2) # Mod
print("xz1+x2*x3=",(x1+x2)*x2)

s1="Hello"
s2="World"
s3= s1 + " " + s2
print(s3)

s4 = s1 + str(x1) # convert int to string
s5 = int("6")      #convert str to int
print("s4=",s4, "s5=",s5)

have_hair=True
have_mustache=False
hair_and_mustache = have_hair and have_mustache
hair_or_mustache = have_hair or have_mustache
print("And=",hair_and_mustache, "Or=",hair_or_mustache)

have_not_hair_and_mustache = not (have_hair and have_mustache)
print(have_not_hair_and_mustache)

b1 = x1 == x2
print(b1)
