import random

user_response = ""

# Function that response to what you say
def get_bot_response(user_response):

    for word in user_response:
        res = word.upper()

        if res == 'HAPPY' or res == 'GOOD' or res == "NICE" or res == 'SAD' or res == 'BAD' or res == "MISERABLE":

            good_res = [f"I'm so glad you are {word}", f"I makes me feel {word} you are {word}!", f"{word} to hear your {word}!"]
            bad_res = ["Well at least your above the ground!", f"I'm sorry to here your feeling {word} I hope your end to the day is better!", "Well be sure & do something for you self today!"]

            
            if res == 'HAPPY' or res == 'GOOD' or res == "NICE":
                return random.choice(good_res)
            elif res == 'SAD' or res == 'BAD' or res == "MISERABLE":
                return random.choice(bad_res)
        
    return "As the wise man once said the camle with the biges hump is the wealthiest."

#Greeting
print("Hey there! Wecome welcome, come and tell me how you are feeling?")



#keep asking how they feel tell user says done
while user_response != ['done']:
    user_response = input('type "done" when you nologer want to talk, but pleas do tell me how you are felling?').split()


    print(get_bot_response(user_response))