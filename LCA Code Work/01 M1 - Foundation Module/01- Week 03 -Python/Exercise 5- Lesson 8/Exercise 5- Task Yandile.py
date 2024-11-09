# Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits
fruits = ["apple","banana","pineapple","tomato"]
# TODO: Add a fruit to the end of the list
fruits.append("pear")
# TODO: Insert a fruit at the beginning of the list
fruits[0] = "grapes"
# TODO: Remove a fruit from the list
fruits.remove("banana")
# TODO: Print the modified list
print(fruits)

#-------------------------------------------------------------------------
# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5
list_of_numbers = [1,2,3,4,5]
# TODO: Create a new list with each number squared
new_list_of_numbers = [1,4,9,16,25]
# TODO: Find the sum and average of the original numbers
total_sum = 16

for value in list_of_numbers:
    total_sum += value
avg= total_sum / len(list_of_numbers) 
# TODO: Print the results
print(avg)

#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries

# TODO: Create a dictionary of countries and their capitals
countrydict = {
    "South Africa":"Pretoria",
    "China":"Beijing",
    "England":"London",
    "Germany":"Berlin"
}
# TODO: Add a new country-capital pair
countrydict["America"]= "Washington,DC"
print(countrydict)
print(countrydict["America"])
# TODO: Update the capital of an existing country
countrydict["South Africa"]="Cape Town"
print(countrydict["South Africa"])
# TODO: Remove a country-capital pair
countrydict.pop("England")
print(countrydict)
# TODO: Print the modified dictionary


#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors
fruit_colorsdict= {
    "banana":"yellow",
    "orange":"orange",
    "blueberry":"blue",
    "cherry":"red"
}
# TODO: Print all the fruits (keys)
keys = fruit_colorsdict.keys()
print(keys)
# TODO: Print all the colors (values)
values = fruit_colorsdict.values()
print(values)
# TODO: Print each fruit and its color
for fruit,color in fruit_colorsdict.items():
    print(f"The color of {fruit} is {color}.")
# TODO: Check if a fruit is in the dictionary and print its color
fruit_check = "banana"

if fruit_check in fruit_colorsdict:
    print(f"{fruit_check} is in the dictionary with color:{fruit_colorsdict[fruit_check]}")
else:
    print(f"{fruit_check} is not in the dictionary.")