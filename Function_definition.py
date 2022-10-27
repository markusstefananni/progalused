import math

# define function
def print_hello():
    print ("hello")

def get_hello():
    return "hello"

def ask_name_and_greet_user():
    name = input("insert you name: ")
    capitalized_name = name.capitalize()
    if capitalized_name == "thanos":
        print("Get out of here, Thanos! Nobody wants to play with you!")
    else:
        print(f"Hi, {capitalized_name}. Would you like to have a Hamburger?")


    print("Hi {capitalized_name}.  Would you like to have a Hamburger?")

def calculate_hypotenuse_length(a, b):
    c = math.sqrt(a ** 2 + b ** 2)
    return c

def calculate_cathetus_length(c, a):
    b = math.sqrt(c ** 2 - a ** 2)
    return b


# use function
# print_hello() # without return

# func_result = get_hello() # whith return
# print(func_result)

# ask_name_and_greet_user()
# func_result = calculate_hypotenuse_length(5, 4)
# print(func_result)

func_results = calculate_cathetus_length(5, 4)
print(func_results)

