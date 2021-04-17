"""
----------------------------------------------------------------------
Name:   problem2.py

Purpose:  Tony is a new DoorDash Driver and is tracking statistics for the first 100km that he's driven for the food delivery service.  Write a program that allows Tony to enter the distance driven for each day until the total distance driven surpasses 100km.  The program will compute and output: the number of days it took to pass 100 km, and average distance driven per day. 
 
Author: Sinclair.K
 
Created:  03/03/2021
----------------------------------------------------------------------
"""

# program header
print ("***** Welcome to the DoorDash Distance Tracker ****** ")

# add spacing and description
print (" ")
print ("** Travel Log **")

# set initial value 
distance_travelled = 0
total_distance = 0
number_of_days = 0

# while loop to get the distance travelled and number of days
while total_distance < 100:
  distance_travelled = int(input("Enter the distance travelled for the day: "))
  total_distance = total_distance + distance_travelled
  number_of_days = number_of_days + 1

# determine the average distance diven per day
average_distance = int(total_distance / number_of_days)

# add spacing and description
print (" ")
print ("** Summary **")

# output number of days taken and average distance 
print ("It took " + str(number_of_days) + " days to surpass 100km driven.")
print ("The average distance driven per day is " + str(average_distance) +"km.")
