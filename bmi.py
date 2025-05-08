def calculate_bmi(height,weight):
    #Prints out the height and weight beforehand
    print("Height = " + str(weight))
    print("Weight = " +  str(height))
    # Calculates BMI and displays it
    bmi = weight / (height * height)
    print("Body Mass Index (BMI): ", round(bmi,2))

    # Determines the user's weight classification 
    weight_class = "..."
    if bmi < 18.5:
        weight_class = "-1"
    elif bmi <= 25.0:
        weight_class = "0"
    else:
        weight_class = "1"
    print("The user is", weight_class)

    return round(bmi,2), weight_class


calculate_bmi(height=1.73,weight=57)