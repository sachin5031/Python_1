#Pickling

#load() [deserialization] and dump() [Serialization]

# import pickle
#
# result={'a':1,'b':2,'c':3}
# with open('pick.bin','wb') as f:
#     pickle.dump(result,f)
#     f.close()
#
# with open('pick.bin','rb') as f:
#     x = pickle.load(f)
#
# print(x)

# import pickle

# result={'a':1,'b':2,'c':3}
# with open('dict.txt','wb') as f:
#     pickle.dump(result,f)
#     f.close()

# with open('dict.txt','rb') as f:
#     x = pickle.load(f)

# print(x)
# print(type(x))

# tell() = in this method we use before load it tells starting position and after load it tells final position
#seek() = it tells what position to start

# with open('dict.txt','rb') as f:
#     print(f.tell())
#     x = pickle.load(f)
#     print(f.tell())
# print(x)
# print(type(x))

with open('new.txt','r') as f:
    f.seek(5)
    print(f.tell())
    print(f.read())
    print(f.tell())
