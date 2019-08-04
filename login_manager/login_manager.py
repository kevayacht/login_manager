from tkinter import Tk, Label, Button, Entry


class LoginBox:
    def __init__(self, master):
        self.master = master
        master.title("Login Manger")
        master.geometry("300x300+500+100")
        master.resizable(0, 0)

        self.greeting_label = Label(master, text="Welcome to the Login Manger")
        self.login_button = Button(master, command=self.login_click, text="Login", bg='Green', fg='Black')
        self.login_new_user = Button(master, command=self.create_new_user_click, text="Create New User", fg='Black')

        self.home()

        self.username_label = Label(text="Username:")
        self.password_label = Label(text="Password:")
        self.username_entry = Entry()
        self.password_entry = Entry()

    def home(self):
        self.greeting_label.pack()
        self.login_button.pack()
        self.login_new_user.pack()

    def remove_home_pack(self):
        self.greeting_label.pack_forget()
        self.login_button.pack_forget()
        self.login_new_user.pack_forget()

    def login_click(self):
        self.remove_home_pack()

    def build_login(self):
        pass

    def remove_login(self):
        pass

    def create_new_user_click(self):
        self.remove_home_pack()

    def build_create_user(self):
        pass

    def verify_login(self):
        pass


def main():
    root = Tk()
    login_box = LoginBox(root)
    root.mainloop()


if __name__ == '__main__':
    main()