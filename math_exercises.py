
import math

"""set of different math expressions and exe"""

num_a = 5
num_b = 2

# 1. sum and difference

sum = num_a + num_b
print (f"{num_a} + {num_b} = {sum}")
print ("----------")

difference = num_a - num_b
print (f"{num_a} - {num_b} = {difference}")
print ("-----------")

#2. Float division

division = num_a / num_b
print (f"{num_a} / {num_b}  = {division}")
print ("------------")

#3. Integer division

division = num_a // num_b
print (f"{num_a} // {num_b}  = {division}")
print ("------------")

#4. Powerful operations

multiply_numbers = num_a * num_b
print (f"{num_a} * {num_b} = {multiply_numbers}")
print ("------------")

#5. Find average

average = (num_a + num_b) / 2
print (f"({num_a} + {num_b}) / 2= {average}")

#6. Area of a circle

radius = 10
print ("Pi:", math.pi)
print (10 ** 2 * math.pi)
print ("---------")

#7. Area of an equilateral triangle

side_length = 5
triangle_area = (math.sqrt(3) /4) * side_length ** 2
print(triangle_area)
triangle_area = round(triangle_area)
print(triangle_area)
print(f"Triangle area is {triangle_area} if side length is {side_length}")
print ("---------")

#8. Calculate discriminant

a = 1
b = 5
c = 6
discriminant = b ** 2 - 4 * a * c
print (discriminant)
print (f"Numbers {a} and {b} and {c} discriminant is {discriminant}")
print ("---------")

#9. Calculate hypotenuse length

num_c = math.sqrt(num_a ** 2 + num_b ** 2)
print(f"{num_c}")
print ("--------")

#10. Calculate cathetus length

num_c = 10
num_a = 6
num_b = math.sqrt(num_c ** 2 - num_a ** 2)
print(f"{num_b}")
print("--------")

#11. Time converter

second = 4612
minutes = second // 60
print(minutes)
hours = minutes // 60
minutes = minutes % 60
second = second % 60
print(hours)
print(minutes)
print(second)
print("--------")

#12. Student helper

angle = 35
sine = math.sin(angle)
cosine = math.cos(angle)

sine = round (sine, 1)
cosine = round(cosine, 1)

print(sine)
print(cosine)

print(f"Angle {angle} sin is {sine}")
print(f"Angle {angle} cosine is {cosine}")
print("--------")

#13. Greetings

n = 4
lots_of_keys = "hey" * 4
print(lots_of_keys)
print("-----------")

#14. Adding numbers

num_a = "6"
num_b = "2"
string_numbers = (num_a + num_b)
print(string_numbers)
print("---------")
