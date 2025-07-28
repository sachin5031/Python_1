import simplejson

# person={"name":"sachin","age":"21","language":{"Tamil","English"}}

# per_dict=simplejson.loads(person)
with open('data.json') as f:
    data=simplejson.loads(f)
print(data) 