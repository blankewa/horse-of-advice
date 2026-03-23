#ui functions

#import tkinter libs + pil
import tkinter
from PIL import Image

#create windwo parent
window = tkinter.Tk()

#load image to tk form
def load_image(path):
    image = Image.open(path)
    return tkinter.PhotoImage(image)

#create main window in func
def create_window():
    #set basics of window
    window.title("Wise Horse of Financial Wisdom")
    window.geometry("400x400")
    window.mainloop()


#load image to window
def display_image(image):
    picLabel = tkinter.Label(window, image=image)
    picLabel.pack()

    



