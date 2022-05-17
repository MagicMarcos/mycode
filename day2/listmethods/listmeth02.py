#!/usr/bin/env python3
proto = ["ssh", "http", "https"]

protoa = ["ssh", "http", "https"]
print(proto)

proto.append("dns") # this line will add "dns" to the end of our list

protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)

proto2 = [ 22, 80, 443, 53 ] # a list of common ports

#add each individual item in proto2 to list proto
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)

#add proto2 as a list to protoa (a list within a list)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)

#insert a new item inside of list at the second index 
proto.insert(2, "marcos")
print(proto)

#reverse the list 
protoa.reverse()
print(protoa)

#remove a specific item in the list 
proto.remove("marcos")
print(proto)

#remove item at second index in the list 
protoa.pop(2)
print(protoa)

#remove the last item from the list 
proto.pop()
print(proto)
