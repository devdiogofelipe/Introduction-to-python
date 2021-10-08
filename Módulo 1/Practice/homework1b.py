import traceback

def calculator():
    
    # Get dog age
    age = input("Input dog years: ")

    try:
        # Cast to float
        dog_age = float(age)

        # If user enters negative number, print message
        # Otherwise, calculate dog's age in human years
        if dog_age <0:
            print("You have put an invalid age.")
        else:
            if dog_age == 1:
                human_age = dog_age * 15
            elif dog_age == 2:
                human_age = dog_age * 12
            elif dog_age == 3:
                human_age = dog_age * 9.3
            elif dog_age == 4:
                human_age = dog_age * 8
            elif dog_age == 5:
                human_age = dog_age * 7.2
            else:
                human_age = ((dog_age - 5)* 7) + 36

        human_age = round(human_age, 2)
        sentence = ("The given dog age {} is {} in human years.").format(dog_age, human_age)
        print(sentence)


        # your code here
        

    except:
        print(age, "is an invalid age.")
        print(traceback.format_exc())
    
calculator() # This line calls the calculator function