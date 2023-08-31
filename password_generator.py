import tkinter
import string
import random
class Window():

    MAX_CHARS = 15
    MIN_CHARS = 3
    CHARS_OPTIONS = ["Alphanumric",
                     "Numric",
                     "Alpha"]
    GRID_PADY = (18,18)
    def __init__(self):
        self.initUI()

    def initUI(self):
        self.master = tkinter.Tk()
        self.master.title("Password Generator")
        self.master.geometry("450x450")

        self.ptype = tkinter.StringVar(self.master,
                                       value= Window.CHARS_OPTIONS[0])
        self.n_chars = tkinter.IntVar(self.master,
                                      value=Window.MIN_CHARS)
        
        self.lable_chars = tkinter.Label(self.master,
                text="CHOOSE THE PASSWORD STYLE: ",font = ("arial",10,'bold'),bd=10,fg="yellow",big="black")
        self.option_menu_chars = tkinter.OptionMenu(self.master, self.ptype *Window.CHARS_OPTIONS)



        self.frame_n_chars = tkinter.Frame(self.master)
        self.label_num_chars = tkinter.Label(self.master, text="Password Lenght:" ,font=("arial",10,'bold'),bd= 10,fg="yellow",bg="black")
        self.option_menu_chars= tkinter.OptionMenu(self.master, self.n_chars, *range(Window.MIN_CHARS, Window.MAX_CHARS+1))

        self.text_passwird_out = tkinter.Text(self.master, border=2, height=2, width=30)

        self.frame_buttons = tkinter.Frame()
        self.button_generate = tkinter.Button(self.frame_buttons, text = "Generate", width=8,font=("Algerian",10,'bold'),bd=10,fg="RED",bg="BLACK",command=lambda:self.__setattr__)
        self.option.close = tkinter.Button(self.frame_buttons, text="close", command=self.master.quit,width=8,font=("Algerian",10,;'bold'),bd=10,fg="RED",bg="BLACK")


        self.label_chars_grid(row=0, column=0, pady=Window.GRID_PADY)
        self.option_menu_chars.grid(row=0, column=1)

        self.label_num_chars.grid(row=1, column=0, pady=Window.GRID_PADY)
        self.option_menu_chars.grid(row=1, column=1)

        self.text_password_out.grid(row=2, column=0, pady=Window.GRID_PADY)


        self.button_generate.pack(side=tkinter.LEFT)
        self.button_close.pack(side=tkinter.LEFT, pady=Window.GRID_PADY)
        self.frame_buttons.grid(row=3, column=1, columnspan=2)

        self.master.mainloop()
        def set_password(self):
            chars = ""
            ptype = self.pytpe.get().lower()
            if ptype == "numeric":
                chars = string.digits

            elif ptype == "alpha":
                chars = string.ascii_letters
            else:
                chars = string.digits + string.ascii_letters
            password = "".join(random.choices(chars, k=self.n_chars.get()))

            self.text_password_out.delete("1,0", tkinter.END)
            self.text_password_out.insert("1,0, paasword")

    def new_method(self):
        self.option_menu_chars.grid(row = 0, column=1)

    if __name__ == "__main":
        Window()

