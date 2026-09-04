from Unit_converter2  import cm_to_inches,inches_to_cm,mm_to_inches,inches_to_mm
direction=input("Enter conversion (cm_to_inches or inches_to_cm or mm_to_inches or inches_to_mm):")
value=float(input("enter measurement: "))

if direction == "cm_to_inches":
    result= cm_to_inches(value)
    print("Converted value:",result,"inches")
   

elif direction == "inches_to_cm":
    result= inches_to_cm(value)
    print("Converted value:",result,"cm")


elif direction == "mm_to_inches":
    result= mm_to_inches(value)
    print("Converted value:",result,"inches")


elif direction == "inches_to_mm":
    result= inches_to_mm(value)
    print("Converted value:",result,"mm")




else:
    print("invalid conversion option")

print(mm_to_inches.__doc__)
print(inches_to_mm.__doc__)
print(cm_to_inches.__doc__)
print(inches_to_cm.__doc__)




