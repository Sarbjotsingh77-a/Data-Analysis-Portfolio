import os

def create_directory(path):

    if not os.path.exists(path):
        os.makedirs(path)

def save_text_report(filename, text):

    with open(filename, "w") as file:
        file.write(text)
