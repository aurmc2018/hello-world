

height = float(input("Enter your Height ?"))

weight = float(input("Enter your Weight ?"))

body_mass_index = weight /(height * height)


#18,22,28, 30
if body_mass_index < 18.5:
    print(f"Your bmi is {body_mass_index}, Under Weight")
elif body_mass_index < 25:
    print(f"Your bmi is {body_mass_index},Normal Weight")
elif body_mass_index < 30:
    print(f"Your bmi is {body_mass_index}, Over Weight")
elif body_mass_index < 35:
    print(f"Your bmi is {body_mass_index}, Obese")
else:
    print(f"Your bmi is {body_mass_index}, Clinically Obese")