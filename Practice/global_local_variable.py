x=10 #Global
print(x)

def var():
    global x #using this keyword it change the local keyword into global
    x=5 #local
    print(x)

var()
print(x)