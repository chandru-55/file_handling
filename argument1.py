from sys import argv

script, user_name = argv
prompt = '> '

print("Hi %s from %s, I'm the %s script." % (user_name, city, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % user_name)
likes = input(prompt)

print("What's the whether like today in %s?" % city)
weather = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright, so you said %r about liking me.
The weather in your city is %s.
But I can't feel it because I'm a robot.
And you have a %r computer.  Nice.
""" % (likes, weather, computer))
