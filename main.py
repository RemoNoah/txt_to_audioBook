import pyttsx3

path = input("Enter the path to the txt file:  ")
filename = input("Enter the output file name: ") + ".mp3"

with open(path) as book:
    bookText = book.readlines()

engine = pyttsx3.init()

engine.save_to_file(bookText, filename=filename)
for i in bookText:
    engine.say(i)
    engine.runAndWait()
