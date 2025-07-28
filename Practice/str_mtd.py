#String Method

a="hello world"
b="hElLoWoRlD"
e="Hello this is python"
c="   Hello World   "
d="---Hello World---"
f=['A','B','C','D']
print(a.capitalize()) 
print(a.upper())
print(a.lower())
print(b.swapcase())
print(b.casefold())
print(a.title())
print(b.title())
print(a.isalnum())
print(b.isalpha())
print(a.isupper())
print(b.islower())
print(a.isdigit())
print(c.istitle())
print(a.replace("o","***"))
print(c.strip())
print(c.lstrip())
print(c.rstrip())
print(d.rstrip("-"))
print(d.lstrip("-"))
print(e.startswith("Hello"))
print(e.startswith(("Hello","is","python")))
print(e.endswith(("Hello","is","python")))
print(e.endswith("python"))
print(e.split())
print(e.split('o'))
print(e.split('is'))
print(e.split(' ',2))
print(e.rsplit(' ',2))
print(" ".join(f))
print("***".join(f))
print(a.find('o'))
print(a.rfind('o'))
print(a.index('o'))
print(a.rindex('o'))