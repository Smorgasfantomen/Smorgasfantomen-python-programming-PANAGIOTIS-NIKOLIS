# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from Functions import filereader, filewriter, point_classifier

# Jag skriver alla kommentarer på engelska pga att jag tycker bara att det låter konstigt
# när jag blandar svenska och engelsk programmeringsterminologi

# File reader
# I got a little eager around the (d) task and interpreted it as if I should read the testdata from lab 2 into this alogrithm
# therefore I'm leaving this section  as an easter egg where you get to choose between loading the data csv or the lab 2 datapoints.txt

while True:
    data_choice = input("Do you want to read the (p)okemon datapoints.txt or the (u)nlabelled data.csv?")
    if data_choice == "p":
        value_array = np.array(filereader(True))
        break
    elif data_choice == "u":
        value_array = np.array(filereader(False))
        break
    else:
        print(f"{data_choice} is not a valid command.")


# I felt that the most intuitive divider line would be a line that:
# 1: Intersects the mean point of the coordinates,
# 2: Is perpendicular to the mean line of the coordinates
 
# Sort data into lists

x_values = value_array[:, 0]
y_values = value_array[:, 1]

# Use these to find the mean point coordinates

mean_x = np.mean(x_values)
mean_y = np.mean(y_values)

# Create a mean line through the two clusters
# I searched for and found a function to create a mean line,
# but later found polyfit, which I replaced it with

mean_k, mean_m = np.polyfit(x_values, y_values, 1)

meanline_x = np.array([min(x_values), max(x_values)])
meanline_y = mean_k * meanline_x + mean_m

# Create the mean-based divider equation:
div_k = (-1 / mean_k)
div_m = (mean_y - div_k * mean_x)
divline_y = div_k * meanline_x + div_m

# Write i-task equations & limit plot display area:
plot_size = 6

x = np.linspace(-plot_size, plot_size, 2)

f = -0.489 * x
g = -2 * x + 0.16
h = 800 * x - 120

# Ask the user which equation should be used for sorting
# (bypass & use default if using pokemon data or standard mean divider):
# I realize (quite late) I could have put this into Functions.py as well,
# but I don't have the time to rewrite and test it

sorted_array = point_classifier(value_array, div_k, div_m)

while data_choice == "u":
    sorting_choice = input("Which equation do you want to use for classification?\n(m)ean based equation\n(f)x = -0.489x\n(g)x = -2x + 0,16\n(h)x = 800x -120")
    if sorting_choice == "m":
        break
    elif sorting_choice == "f":
        sorted_array = point_classifier(value_array, -0.489, 0)
        break
    elif sorting_choice == "g":
        sorted_array = point_classifier(value_array, -2, 0.16)
        break
    elif sorting_choice == "h":
        sorted_array = point_classifier(value_array, 800, -120)
        break
    else:
        print(f"{sorting_choice} is not a valid command.")

# Sort coordinates into arrays:

filewriter(sorted_array)

# Split array based on third column binary
above_div = sorted_array[sorted_array[:, 2] == 1]
below_div = sorted_array[sorted_array[:, 2] == 0]

# Main plot code
plt.figure(figsize=(8, 8), dpi=100)
plt.scatter(mean_x, mean_y, color = "black", marker = "x", label="Mean point", s=200)
plt.plot(meanline_x, meanline_y, color="purple", linestyle="-", label="Mean Line")
plt.plot(meanline_x, divline_y, color="red", linestyle="-", label="Mean-perpendicular division Line")
plt.scatter(above_div[:, 0], above_div[:, 1], color = "blue", marker = "o", label="Above division line")
plt.scatter(below_div[:, 0], below_div[:, 1], color = "red", marker = "o", label="Below division line")

# Make sure the graph shows relevant area depending on which data is read,
# as the h(x) function stretches quite far beyond the points
if data_choice == "p":
    plt.axis("equal")
elif data_choice == "u":
    plt.axis([-plot_size, plot_size, -plot_size, plot_size])
    # i-task plots:
    plt.plot(x, f, label="f(x)")
    plt.plot(x, g, label="g(x)")
    plt.plot(x, h, label="h(x)")

# Final plot parameters

plt.title("Coordinates")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid(True)
plt.legend()
plt.show()