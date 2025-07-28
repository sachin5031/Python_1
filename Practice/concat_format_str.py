#Concatenate String
# a="Hello"
# b="World"
# print(a+" "+b)

# a="My age is"
# b=21
# print(a+" "+str(b))

#Format : Using this argument we use {} placeholder were we want to place the values

age=21
clg="Agni college"
txt="I am {} years old.I am studying at {}"
print(txt.format(age,clg))

txt2="I am {} years old.I am studying at {}".format(age,clg)
print(txt2)

txt3=f"I am {age} years old.I am studying at {clg}"
print(txt3)