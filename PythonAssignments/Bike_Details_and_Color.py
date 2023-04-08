# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 13:28:29 2023

@author: haryi
"""

# Initial Bike details
bike_list = [
    {
        "Name Of The Bike": "Bajaj Pulsar",
        "Model": "Bajaj Pulsar 220 F",
        "Milage Of The Bike": "40kmpl"
    },
    {
        "Name Of The Bike": "Tvs Apache",
        "Model": "Tvs Apache Rtr 160",
        "Milage Of The Bike": "50kmpl"
    },
    {
        "Name Of The Bike": "Yamaha",
        "Model": "Yamaha Yzf R15 Ver 3.0",
        "Milage Of The Bike": "45kmpl"
    }
]

# a. Get N number of Bike details in nested list.
n = int(input("Enter the number of bikes to add: "))
for i in range(n):
    name = input("Enter bike name: ")
    model = input("Enter bike model: ")
    mileage = input("Enter bike mileage: ")
    bike_list.append({
        "Name Of The Bike": name,
        "Model": model,
        "Milage Of The Bike": mileage
    })

# b. Insert "Color" at index 3 of every list.
for bike in bike_list:
    bike.insert(3, "Color")

# c. Add "Yamaha" bike details with different color.
bike_list.append({
    "Name Of The Bike": "Yamaha",
    "Model": "Yamaha Yzf R15 Ver 3.0",
    "Milage Of The Bike": "45kmpl",
    "Color": "Blue"
})

# d. Add 1 more new Bike details using extend().
bike_list.extend([{
    "Name Of The Bike": "Honda",
    "Model": "Honda CB Shine",
    "Milage Of The Bike": "55kmpl",
    "Color": "Red"
}])

# e. Sort the list based on Mileage of the bike.
sorted_bike_list = sorted(bike_list, key=lambda x: x["Milage Of The Bike"])

# f. Print the original and sorted list.
print("Original Bike List:")
for bike in bike_list:
    print(bike)
print("\nSorted Bike List:")
for bike in sorted_bike_list:
    print(bike)

# g. Insert "S.No" at index 0 of every list.
for i, bike in enumerate(bike_list):
    bike.insert(0, f"S.No.{i+1}")

# h. Print the unique bike details.
unique_bikes = set(tuple(bike.items()) for bike in bike_list)
print("\nUnique Bike Details:")
for bike in unique_bikes:
    print(dict(bike))
