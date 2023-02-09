name = input("what is your name?")
age= input ("how old will you be this year?")
age=int(age)
# an error can occur here. problem is not in the code, it is with its execution. for example, if you put in 'twenty', instead of 20, then it will give error.
birth_year=2023-age
#put age as integer because if no it is a string and you can't subtract a number from 2023
print(name, "you were born in", birth_year)
