from tkinter import Tk, Label, Button


def raise_above_all(master):
    master.attributes('-topmost', True)
    master.focus_force()


def popup_message():
    popup = Tk()
    popup.wm_title("Error")
    popup.geometry("250x150+525+150")
    raise_above_all(popup)

    message_lable = Label(popup, text="--Dumbass--\n\nYou have not populated\n all the required data fields.\n "
                                      "Did you get confused?\n")
    message_lable.pack(side='top')

    ok_button = Button(popup, text="Yes, I Apologise", command=popup.destroy)
    ok_button.pack()
    popup.mainloop()
