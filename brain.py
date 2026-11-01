import datetime
import random
import re

from search import smart_search, wiki_answer

jokes = [
    "Why do programmers hate nature? Too many bugs.",
    "I told my computer I needed a break, and it said no problem."
]

facts = [
    "Python was created in 1991.",
    "The human brain has billions of neurons."
]

def safe_math(expr):
    if re.fullmatch(r"[0-9\+\-\*/\.\(\) ]+", expr):
        try:
            return str(eval(expr))
        except:
            return "Invalid math expression"
    return None


def get_response(query):

    q = query.lower().strip()

    
    if q in ["hi", "hello", "hey"]:
        return "Hello! I am PyChat."

    
    elif "how are you" in q:
        return "I am doing well. Thanks for asking."

    elif "who are you" in q:
        return "I am PyChat, your smart assistant."

    elif "who made you" in q:
        return "I was created as the PyChat project."

    elif "what are you doing" in q:
        return "I am waiting for your next question."

    elif "what can you do" in q:
        return (
            "I can answer questions, solve math, "
            "tell jokes, give facts, search Wikipedia "
            "and search the web."
        )

    elif "thank you" in q or "thanks" in q:
        return "You're welcome."

    elif "good morning" in q:
        return "Good morning! Have a wonderful day."

    elif "good afternoon" in q:
        return "Good afternoon!"

    elif "good evening" in q:
        return "Good evening!"

    elif "good night" in q:
        return "Good night. Take care."

    
    elif "time" in q:
        return "Current time: " + datetime.datetime.now().strftime("%H:%M:%S")

    
    elif "date" in q:
        return "Today's date: " + datetime.datetime.now().strftime("%Y-%m-%d")

    
    math_result = safe_math(q)

    if math_result:
        return math_result

    
    elif "joke" in q:
        return random.choice(jokes)

    
    elif "fact" in q:
        return random.choice(facts)

    
    wiki = wiki_answer(query)

    if wiki:
        return "Wikipedia:\n" + wiki

    
    return smart_search(query) 
