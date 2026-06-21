import webbrowser
import urllib.parse
import wikipedia

def smart_search(query):
    q = urllib.parse.quote(query)

    wiki_url = f"https://en.wikipedia.org/wiki/Special:Search?search={q}"
    google_url = f"https://www.google.com/search?q={q}"
    youtube_url = f"https://www.youtube.com/results?search_query={q}"

    webbrowser.open(wiki_url)
    webbrowser.open(google_url)
    webbrowser.open(youtube_url)

    return "I searched Wikipedia, Google and YouTube."

def wiki_answer(query):
    try:
        return wikipedia.summary(query, sentences=2)
    except:
        return None
