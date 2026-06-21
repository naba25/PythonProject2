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
