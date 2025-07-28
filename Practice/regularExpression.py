import re

text = 'Hello world, I am a python progrramming language'
# pattern='o'
#
# #findall() = It display the all value were we want to find
# x=re.findall(pattern,text)
# print(x)
#
# #search() = it display it index value
#
# x=re.search(pattern,text)
# print(x)
# print(x.start())
# print(x.group())
# print(x.start())
# print(x.end())
# print(x.string)
#
# #split() = it split the value we entered value is occurred
#
# x= re.split(pattern,text)
# x= re.split(pattern,text,2)
# print(x)
#
# #sub = substitute or replace the value
#
# x=re.sub(pattern,'*****',text)
# x=re.sub(pattern,'*****',text,2)
# print(x)

# pattern='[a-m]'
pattern='H...o' # it will match 'Hello' and 'Hello'
pattern='H....o' # it will match 'Hello' and 'Hello'
pattern='^Hello' # it will match 'Hello' at the start of the string
pattern='^.ello' # it will match 'Hello' at the start of the string
pattern='^Hi' # it will match 'Hi' at the start of the string
pattern='a..$' # it will match 'a' followed by any two characters at the end of the string
pattern='a.*$' # it will match 'a' followed by any characters at the end of the string
pattern='a.+$' # it will match 'a' followed by at least one character at the end of the string
pattern='e.?$' # it will match 'e' followed by zero or one character at the end of the string
pattern='Hel{2}o' # it will match 'Hello' with exactly two 'l's
pattern='Hel{2,3}o' # it will match 'Hello' with two or three 'l's
pattern='world|universe' # it will match either 'world' or 'universe'
x=re.findall(pattern,text)
print(x)
