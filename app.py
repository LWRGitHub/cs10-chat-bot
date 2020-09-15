import random

# Function that response to what you say
def get_bot_response(user_response):
    res = user_response.upper()

    good_res = [f"I'm so glad you are {user_response}", f"I makes me feel {user_response} you are {user_response}!", f"{user_response} to hear your {user_response}!"]
    bad_res = ["Well at least your above the ground!", f"I'm sorry to here your feeling {user_response} I hope your end to the day is better!", "Well be sure & do something for you self today!"]

    if res == 'HAPPY' or res == 'GOOD' or res == "NICE":
        return random.choice(good_res)
    elif res == 'SAD' or res == 'BAD' or res == "MISERABLE":
        return random.choice(bad_res)
    else:
        return "As the wise man once said the camle with the biges hump is the wealthiest."

#Greeting
print("Hey there! Wecome welcome, come and tell me how you are feeling?")

user_response = ""

#keep asking how they feel tell user says Good bye
while user_response != 'Good bye':
    user_response = input('type "Good bye" when you nologer want to talk, but pleas do tell me how you are felling?')

    print(get_bot_response(user_response))