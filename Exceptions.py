name = input("what is your name?")
age = input("how old will you be this year?")
try:
    age=int(age)
except ValueError:
    print("sorry, that was not a valid number")
    exit (-1)
    birth_year=2023-age
    print(name, "you were born in", birth_year)

