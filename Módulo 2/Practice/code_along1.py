#Write code that finds the minimum value of a list of numbers 5, 3, 8, -1, -2.2, 0
# - Dont use the built-in min() function
# - Instantiate a 'numbers' list variable containing the proper values (above)
# - Iterate over that list and find the min value
# - Print the minimum value in the format:"... is the min number"


list = [5, 3 ,8, -1, -2.2, 0]

min = list[0]


for number in list:
    if number < min:
        min = number

print(min, "is the min number")