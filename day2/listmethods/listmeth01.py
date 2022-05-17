#!/usr/bin/env python3

#create a list containing 3 items
proto = ["ssh", "http", "https"]

#print list
print(proto)

#print second item in list 
print(proto[1])

proto.extend("dns") # this line will add d, n, and s
print(proto)
