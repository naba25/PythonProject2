import tkinter as tk
from tkinter import scrolledtext
import threading

from brain import get_response
from voice import speak

def update_chat(text):
    chat_box.insert(tk.END, text + "\n")
    chat_box.see(tk.END)

def process(query):
    answer = get_response(query)

    root.after(
        0,
        update_chat,
        "PyChat: " + answer
    )

    threading.Thread(
        target=speak,
        args=(answer,),
        daemon=True
    ).start()

def ask():
    query = entry.get().strip()

    if not query:
        return

    update_chat("You: " + query)

    entry.delete(0, tk.END)

    threading.Thread(
        target=process,
        args=(query,),
        daemon=True
    ).start()

root = tk.Tk()
root.title("PyChat")
root.geometry("750x550")

chat_box = scrolledtext.ScrolledText(
    root,
    font=("Arial", 11)
)
chat_box.pack(fill=tk.BOTH, expand=True)

entry = tk.Entry(
    root,
    font=("Arial", 14)
)
entry.pack(fill=tk.X)

button = tk.Button(
    root,
    text="Ask PyChat",
    command=ask
)
button.pack()

entry.bind("<Return>", lambda e: ask())

update_chat("PyChat: Ready 🚀")

root.mainloop()
