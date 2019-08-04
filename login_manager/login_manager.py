from tkinter import Tk, Label, Button, Entry


class LoginBox:
    def __init__(self, master):
        self.master = master
        master.title("Login Manger")
        master.geometry("300x400+500+100")
        master.resizable(0, 0)

        self.greeting_label = Label(master, text="Welcome to the Login Manger")
        self.login_button = Button(master, command=self.login_click, text="Login", bg='Green', fg='Black')
        self.login_new_user = Button(master, command=self.create_new_user_click, text="Create New User", fg='Black')

        self.home()

        self.username_label = Label(text="Username:")
        self.password_label = Label(text="Password:")
        self.username_entry = Entry()
        self.password_entry = Entry()

        self.new_name_label = Label(text="Name")
        self.new_last_name_label = Label(text="Last name")
        self.new_username_label = Label(text="Username:")
        self.new_email_label = Label(text="Email Address")
        self.new_phone_num_label = Label(text="Phone Number")
        self.new_password_label = Label(text="Password:")
        self.new_password_confirm_label = Label(text="Re-enter Password")

        self.new_name_entry = Entry()
        self.new_last_name_entry = Entry()
        self.new_username_entry = Entry()
        self.new_email_entry = Entry()
        self.new_phone_num_entry = Entry()
        self.new_password_entry = Entry()
        self.new_password_confirm_entry = Entry()

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
        self.build_login()

    def build_login(self):
        self.username_label.pack()
        self.username_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()

        # find a way to hash ou the input of the password box, allow a tick box to turn that off/on

    def retrieve_login(self):
        pass

    def verify_login(self):
        pass

    def remove_login(self):
        pass

    def create_new_user_click(self):
        self.remove_home_pack()
        self.build_create_user()

    def build_create_user(self):
        self.new_name_label.pack()
        self.new_name_entry.pack()

        self.new_last_name_label.pack()
        self.new_last_name_entry.pack()

        self.new_username_label.pack()
        self.new_username_entry.pack()

        self.new_email_label.pack()
        self.new_email_entry.pack()

        self.new_phone_num_label.pack()
        self.new_phone_num_entry.pack()

        self.new_password_label.pack()
        self.new_password_entry.pack()

        self.new_password_confirm_label.pack()
        self.new_password_confirm_entry.pack()

    def verify_login(self):
        # no boxes may be empty.
        # check that there are no funny chars, handle spaces in strange places.
        # python analysis on the entries.
        # save that stuff in the db.
        pass

    def successful_login(self):
        pass

    def failed_login(self):
        pass


def main():
    root = Tk()
    login_box = LoginBox(root)
    root.mainloop()


if __name__ == '__main__':
    main()