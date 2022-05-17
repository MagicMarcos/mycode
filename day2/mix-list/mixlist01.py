#!/usr/bin/env python3

# create a list containing 3 items
my_list = [ "192.168.0.5", 5060, "UP" ]

#print first element in list
print("The first item in the list (IP): " + my_list[0] )

#print second element in list
print("The second item in the list (port): " + str(my_list[1]) )

#print last element in list
print("The last item in the list (state): " + my_list[-1] )

#create a list containing 6 elements
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
firstIp = iplist[3]
secondIp = iplist[4]
print(f"The following are the only IP addresses in our list {firstIp} and {secondIp}")
