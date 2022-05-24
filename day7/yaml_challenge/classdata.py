#!/usr/bin.env python3
"""Exploring YAML and JSON load, loads, dump and dumps methods.
    Read from JSON file, add to returned object and create a new YAML file with new information
"""
import yaml
import json

def main(): 
    """ - Open json file
        - Covenrt to dictionary using json.load()
        - Append new student
        - Write as new YAML file
    """
    
    # use with so file doesn't need to be closed, open file for reading
    with open("classdata.json", "r") as classdata:
        #convert json file into python dictionary
        classdata_dict = json.load(classdata)
    
    # create new student 
    new_student = {
        'name' : 'Bagheera',
        'awesome' : True,
        'favorites': {
            'movie' : 'The Jungle Book',
            'ice cream' : 'bacon',
            'color' : 'gray'
        },
        'number' : 4
    }
    
    # append student to class_dict
    classdata_dict.append(new_student)

    # use with so we don't have to close file, write to file
    with open("classdata.yaml", "w") as classdata:
        # use dump to add class_dict to classdata file
        yaml.dump(classdata_dict, classdata)

if __name__ == "__main__":
    main()