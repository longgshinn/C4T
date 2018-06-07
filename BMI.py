height=float(input("Height?(cm)"))/100
weight=float(input("Weight?(kg)"))
BMI=weight/(height**2)
print("BMI:",BMI)
if BMI<16:
    print("Severely underweight")
elif BMI<18.5:
    print("Underweight")
elif BMI<25:
    print("Normal")
elif BMI<30:
    print("Overweight")
else:
    print("Obese")
