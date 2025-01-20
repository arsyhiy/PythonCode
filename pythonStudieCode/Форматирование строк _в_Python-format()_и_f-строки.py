#старый способ форматирования:
"This is a string %s" % "string value goes here"

print("Hi, my name is %s" % "Jessica")
# Запустив такую строчку кода, получим следующий результат:
# вывод: Hi, my name is Jessica


#   str.Format:
#   "template string {}".format(arguments)

print("Hello, my name is {}. I am a {} turned {}.".format("Jessica", "musician", "programmer"))
# И наш желаемый результат:
#Hello, my name is Jessica. I am a musician turned programmer.


print("Steve plays {0} and {1}.".format("trumpet", "drums"))

# Steve plays trumpet and drums.

print("Steve plays {1} and {0}.".format("trumpet", "drums"))

# Результат:
#Steve plays drums and trumpet.


print("{organization} is {adjective}!".format(organization="Pythonist", adjective="awesome"))
# Output:
# Pythonist is awesome!



name = "Sam"
adjective = "amazing"
number = 200
disney_ride = "Space Mountain"
print("I went to {0} with {name}.\nIt was {adjective}.\nWe waited for {hours} hours to ride {ride}."
      .format("Disneyland", name=name, adjective=adjective, hours=number, ride=disney_ride))

name = "Jessica"
print(f"Maria and {name} have been friends since grade school.")

name = "Jessica"
print(F"Maria and {name} have been friends since grade school.")


rankings = {"Gonzaga": 31, "Baylor": 28, "Michigan": 25, "Illinois": 24, "Houston": 21}
for team, score in rankings.items():
    print(f"{team:10} ==> {score:10d}")


from string import Template
print(Template("I love to learn with $name!").substitute(name="Pythonist"))
# Результат:
# I love to learn with Pythonist!
