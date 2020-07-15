import random
from textblob import TextBlob

# Name and nickname
name = input("What is your name human?  ")
nicknameQ = input(f"Do you have a nickname {name}? ")

if "y" in nicknameQ.lower():
    nickname = input("What is your nickname? ")
    print(f"Nice to meet you {nickname}!")
elif "n" in nicknameQ.lower():
    nickname = name + name[-1] + "y"
    print(f"I will call you {nickname}")

# Greeting selection
greetings = [
    f"How are you feeling today {nickname}?  ",
    f"Howdy {nickname}! How you doin'?  ",
    f"What's up {nickname}?  ",
    f"How are things going {nickname}?  "
]

print(random.choice(greetings))

greetingA = input()
blob = TextBlob(greetingA)

if blob.polarity > 0:
    print("Glad you are doing well.")
else:
    print("Sorry to hear that.")

# Opinions on topics
topics = [
    "Fortnite",
    "football",
    "Donald Trump",
    "coding",
    "debates",
    "video games"
]

questions = [
    "What is your take on ",
    "What do you think about ",
    "What do you reckon about ",
    "I would like your opinion on "
]

for i in range(0, random.randint(3, 4)):
    q = random.choice(questions)
    t = random.choice(topics)

    questions.remove(q)
    topics.remove(t)

    question = q + t + "?"
    print(question)

    topicA = input()
    blob = TextBlob(topicA)

    if blob.polarity > 0.5:
        print(f"You think very highly of {t}. Quite biased.")
    elif blob.polarity > 0.1:
        print(f"It's clear that you do like {t}.")
    elif blob.polarity < -0.5:
        print(f"Whoa! You hate {t}.")
    elif blob.polarity < -0.1:
        print(f"You don't like {t}. ")
    else:
        print(f"Quite neutral towrads {t}.")

# Random bye
byes = [
    f"Good bye {nickname}!",
    f"Alright {nickname}, gotta bounce. Peace out.",
    f"GTG {nickname}. See you later",
    f"See you later {nickname}!",
    f"Good by American pie!"
]

print(random.choice(byes))