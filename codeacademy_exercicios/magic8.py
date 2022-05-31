import time
import random

answers = ['Yes - definitely.', 'It is decidedly so.', 'Without a doubt.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.']

name = input("Tell us your name, please: ")
print("Good")
question = input("So, what's your question?: ")
print(name + " asks: " + question)
print("Just a moment...")
time.sleep(5)

print("Magic 8-Ball’s answer: " + random.choice(answers))




