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
        weight_class = "Under Weight"
    elif bmi <= 25.0:
        weight_class = "Normal Weight"
    else:
        weight_class = "Over weight"
    print("The user is", weight_class)

    return 0



calculate_bmi(height=1.73,weight=57)