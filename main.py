from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import PyPDF2
import pyttsx3

# _____________________________ Application Functionalities _____________________

main_filepath = ""
temp_filepath = ""


def choose_pdf():
    global temp_filepath
    temp_filepath = askopenfile(mode='r', filetypes=[('pdf files', '*pdf')])
    if temp_filepath is not None:
        pass


def convert_pdf():
    global main_filepath
    global temp_filepath
    main_filepath = str(temp_filepath)

    m = main_filepath.split("'")
    main_filepath = m[1]
    pdfReader = PyPDF2.PdfFileReader(main_filepath)

    # the page with which you want to start
    # this will read the page of 25th page.
    from_page = pdfReader.getPage(1)

    # extracting the text from the PDF
    text = from_page.extractText()

    # reading the text
    speak = pyttsx3.init()
    speak.say(text)
    speak.runAndWait()



# __________________________ Window setup _____________________________

window = Tk()
window.title("JoshPyDevOps WaterMark Application")
window.config(padx=50, pady=50, background="white")


# ______________________________ Intro Line setup _____________________________________

label = Label(text='Joshpydevops PDF to AudioBook Converter', padding=10, font=("Arial", 23, "bold"), foreground="#222123",
              background="white")
label.grid(column=0, row=1)


# ______________________________ Upload setup _____________________________________

# file_upload_label = Label(text="Upload Image: ")
# file_upload_label.grid(column=0, row=2, columnspan=1)

choose_button = Button(text="Choose PDF to Convert", command=choose_pdf)
choose_button.grid(column=0, row=2, sticky="ew")

file_upload_button = Button(text="Click to Convert", command=convert_pdf)
file_upload_button.grid(column=0, row=3)

window.mainloop()
