# Daniel Kantor
# February 14, 2026
# P2LAB1
# This code will calculate thew diamter, circumference and area of a circle


PI = 3.141592653
radius = float(input("What is the radius of the circle? "))
diameter = float(2 * radius)
circumference = 2 * PI * radius
area = PI * (radius ** 2)

print(f"The diameter of the circle is {diameter:.1f}")
print(f"The circumference of the circle is {circumference:.2f}")
print(f"The area of the circle is {area:.3f}")