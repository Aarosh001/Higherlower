from art import logo, vs
import random
from data import data
score = 0
print(logo)
first = random.choice(data)
second = random.choice(data)
print(f"Compare A: {first['name']}, a {first['description']} from {first['country']}")
print(vs)
print(f"Against B: {second['name']}, a {second['description']} from {second['country']}")
option = input("Which has higher followers? A or B : ")
if first['follower_count'] >= second['follower_count']:
    answer = 'A'
else:
    answer = 'B'
if option == answer:
    score = score + 1
    print(f"Youre Right! \nScore = {score}")
else:
    print(f"Youre Wrong! \nFinal Score = {score}")
while option == answer:
    if answer != 'A':
        first = second
    second = random.choice(data)
    print(f"Compare A: {first['name']}, a {first['description']} from {first['country']}")
    print(vs)
    print(f"Against B: {second['name']}, a {second['description']} from {second['country']}")
    option = input("Which has higher followers? A or B : ")
    if first['follower_count'] >= second['follower_count']:
        answer = 'A'
    else:
        answer = 'B'
    if option == answer:
        score = score + 1
        print(f"Youre Right! \nScore = {score}")
    else:
        print(f"Youre Wrong! \nFinal Score = {score}")





