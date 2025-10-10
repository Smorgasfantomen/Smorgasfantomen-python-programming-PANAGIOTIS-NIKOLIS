# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import os

# File reader
# We assign the current directory to a variable, which is used to create a variable for the file path

current_dir = os.path.dirname(os.path.abspath(__file__)) #This solution was suggested by Mistral, in order to force it to always read data from the directory the program runs from
filedata = []

def filereader(wantspokemon):
    if wantspokemon:
        csv_path = os.path.join(current_dir, "datapoints.txt")
        with open(csv_path, "r") as file:
            next(file)
            for row in file:
                values = [float(x) for x in row.strip().split(",")[:2]]
                filedata.append(values)
            return filedata
    else:
        csv_path = os.path.join(current_dir, "unlabelled_data.csv")
        with open(csv_path, "r") as file:
            for row in file:
                values = [float(x) for x in row.strip().split(",")]
                filedata.append(values)
            return filedata

# File writer was also a function I was comfortable breaking out of the main file

def filewriter(writedata):
    write_path = os.path.join(current_dir, "labelled_data.csv")
    with open(write_path, "w") as file:
        for row in writedata:
            line = ",".join(map(str, row)) + "\n"
            file.write(line)



# Point classification (takes an array, a coefficient and an offset,
# and returns an array with a third column designating which side
# of the function the coordinates are). The last lab's code sorted it
# into two arrays straight away, but I wanted to break out this function
# into this file. I could probably have made it return two arrays instead.
# May try that in the future.

def point_classifier(input_array, k, m):
    above_div_bool = input_array[:, 1] > k * input_array[:, 0] + m #This & next row were suggested by Mistral
    above_div_binary = above_div_bool.astype(int)
    sorted_array = np.column_stack((input_array, above_div_binary))
    return sorted_array