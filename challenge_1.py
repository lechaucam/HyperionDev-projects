#calculations of the area a triangle using the formula in the the assignment
# to use math formulas math needs to be imported
import math

# ask user to enter length of 3 different sides, this can be in decimals so we use floats
side1 = float(input ("Please enter the length of the first side of a triangle: "))
side2 = float(input ("Please enter the length of the second side of a triangle: "))
side3 = float(input ("Please enter the length of the third side of a triangle: "))

# make a list entered data and calculate the sum
triangle_sides = [(side1),(side2),(side3)]
sum_sides = sum(triangle_sides)
print(("The sum of the sides is: ") + str(sum_sides))

# using formula from assignment and make calculations with entered data and print area of triangle
s_triangle = sum_sides/2
area_triangle = math.sqrt(s_triangle*(s_triangle-side1)*(s_triangle-side2)*(s_triangle-side3))
area_triangle =(round(area_triangle,2)) 
print ("The area of the triangle is "+ str(area_triangle))
