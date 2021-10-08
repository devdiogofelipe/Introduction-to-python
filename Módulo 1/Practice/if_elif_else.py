def num_to_letter_grade(grade):

    if grade >= 90:
        print ("YAAAAY DID U GET AN A!!!!!")
    elif grade >= 80:
        print("WOW DID U GET AN B!!!")
    elif grade >= 70:
        print("WELL DONE MATE, U GET A C!!")
    elif grade >= 60:
        print("WELL DONE MATE, AN D CAN MAKE U PASS THROUGH")
    else :
        print("HELL NO THIS TEACHER ARE A WAAY OUT OF HIS MIND")

grade = input("Enter your numeric grade: ")
grade = int(grade)
num_to_letter_grade(grade)