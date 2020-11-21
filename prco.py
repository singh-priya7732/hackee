from tkinter import *
from tkinter import filedialog
from pygame import mixer
from fpdf import FPDF
from gtts import gTTS
import PyPDF2
from PIL import Image, ImageTk
import speech_recognition as sr
import pyaudio

root = Tk()
root.title("Book Byte")
root.minsize(width=400, height=400)
root.geometry("450x321+500+100")
bg = Image.open("book.png")
r = ImageTk.PhotoImage(bg)
img = Label(root, image=r)
img.place(x=0, y=25)

hf1 = Frame(root, bg="#FFBB00", bd=5)
hf1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
hl = Label(hf1, text=" Welcome to \nBook Byte", bg='black', fg='white', font=('Courier', 15))
hl.place(relx=0, rely=0, relwidth=1, relheight=1)


def text_to_speech():
    book = filedialog.askopenfilename(title="Select a PDF")
    pdfreader = PyPDF2.PdfFileReader(book)
    pages = pdfreader.numPages

    for num in range(0, pages):
        page = pdfreader.getPage(num)
        txt = page.extractText()
        tts = gTTS(text=txt, lang='en')
        tts.save("convtxt.mp3")
        mixer.init()
        mixer.music.load("convtxt.mp3")
        mixer.music.play()
        while True:

            print("Press 'p' to pause, 'r' to resume")
            print("Press 'e' to exit the program")
            query = input("  ")

            if query == 'p':
                mixer.music.pause()
            elif query == 'r':
                mixer.music.unpause()
            elif query == 'e':
                mixer.music.stop()
                break
    pass


b1 = Button(root, text="Listen to PDF", bg='black', fg='white', command=text_to_speech)
b1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)


def speech_to_text():

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)

    rs = sr.Recognizer()
    with sr.Microphone() as source:
        rs.adjust_for_ambient_noise(source)

        while True:
            print("Please speak")
            audio = rs.listen(source)
            abc=1

            try:
                text = rs.recognize_google(audio)
                pdf.cell(200, 10, txt=text, ln=abc, align='L')

            except Exception as e:
                print("Error : " +str(e))

            i= input("to continue press 1/ to exit press 0 \n")
            i = int(i)
            if i==0:
                print("you have written : \n ")
                pdf.output("Notes.pdf")
                break
            else:
                abc+=1
    pass


b2 = Button(root, text="Speak Notes", bg='black', fg='white', command=speech_to_text)
b2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

root.mainloop()
