# dictt={
#     "name":"Sachin",
#     "age":21,
#     "vehicle":"bmw",
#     "fruits":["apple","oranges","grapes"],
#     "vehicle":"bike"
# }
dictt={
    "name":"Sachin",
    "age":21,
    "vehicle":"bmw",
    "fruits":["apple","oranges","grapes"]
}
# print(len(dictt))
# print(type(dictt))
# x = dictt["vehicle"]
# print(x)
# x =dictt.get("fruits")
# print(x)
# dictt.update({"name":"Bharath"})
# print(dictt)
# dictt.pop("vehicle")
# print(dictt)
# dictt["color"]="black"
# print(dictt)

l1=[('a',1),('b',2),('c',3)]
d1=dict(l1)
print(d1)

key=['a','b','c']
value=[1,2,3]
d2=list(zip(key,value))
print(d2)
d3=dict(zip(key,value))
print(d3)