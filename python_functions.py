#create a basic function
#syntax is def name():

#first iteration
# def greetings():
#     return("Welcome to Cyber Security!") # return is what the function gives to something if assigned
#
# print(greetings())

#second iteration:

def greeting_user(name):
    return(f"Welcome to Cyber Security, {name}")

print(greeting_user("Kai"))

#take user name as input() and display back to user with greeting
#third iteration

def greeting_user():
    user_name = input("Hi, what is your name? ")
    return(f"Welcome to Cyber Security, {user_name}")

print(greeting_user())