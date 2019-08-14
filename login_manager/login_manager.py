from tkinter import Tk, Label, Button, Entry, StringVar
from db import create_db_table, create_user_db, find_user_db, get_user_detail
from helper import raise_above_all, popup_message


class LoginBox:
    """ Login Manager GUI Box Class """

    def __init__(self, master):
        """ Class init Method"""
        self.master = master
        master.title("Login Manger")
        master.geometry("300x430+500+100")
        master.resizable(0, 0)
        raise_above_all(master)

        # state variable
        self.screen_state = 'init'

        # home screen objects
        self.greeting_label = Label(master, text="Welcome to the Login Manger")
        self.login_button = Button(master, command=self.login_click, text="Login", bg='Green', fg='Black')
        self.login_new_user = Button(master, command=self.create_new_user_click, text="Create New User", fg='Black')
        self.exit_button = Button(master, command=master.destroy, text="Exit", fg='Black')

        self.home()

        # Build database table
        create_db_table()

        # login screen objects
        self.login_greeting_label = Label(master, text="Please enter login details")
        self.username_label = Label(text="Username:")
        self.password_label = Label(text="Password:")
        self.username_entry = Entry()
        self.password_entry = Entry(show="*")

        # create new user screen objects
        self.new_greeting_label = Label(master, text="Please enter your details")
        self.new_first_name_label = Label(text="First Name")
        self.new_last_name_label = Label(text="Last name")
        self.new_username_label = Label(text="Username:")
        self.new_email_label = Label(text="Email Address")
        self.new_phone_number_label = Label(text="Phone Number")
        self.new_password_label = Label(text="Password:")
        self.new_password_confirm_label = Label(text="Re-enter Password")
        self.new_first_name_entry = Entry()
        self.new_last_name_entry = Entry()
        self.new_username_entry = Entry()
        self.new_email_entry = Entry()
        self.new_phone_number_entry = Entry()
        self.new_password_entry = Entry(show="*")
        self.new_password_confirm_entry = Entry(show="*")

        # special labels
        self.login_failure_label = Label(master, text="--Dumbass--\nAuthentication unsuccessful.\n")
        self.create_failure_label = Label(master, text="--Dumbass--\nUser could not be created.\n")
        self.login_success_label = Label(master, text="User successfully authenticated!")
        self.new_success_label = Label(master, text="User successfully created!")
        self.done_button = Button(master, command=self.done_click, text="Done")

        self.back_button = Button(master, command=self.back_click, text="Back")
        self.submit_button = Button(master, command=self.submit_click, text="Submit")

        self.welcome_label_text = StringVar()
        self.reject_label_text = StringVar()

        self.welcome_label = Label(master, textvariable=self.welcome_label_text)
        self.reject_label = Label(master, textvariable=self.reject_label_text)

        self.current_user_db_password = None
        self.fields = ['first_name', 'last_name', 'username', 'email', 'phone_number', 'password']
        self.new_user_dictionary = {}
        self.current_user_data_dictionary = {}
        self.login_user_dictionary = {}
        self.new_user_bad_fields = []

    def home(self):
        """ Pack the home screen objects"""
        self.screen_state = 'home'
        self.greeting_label.pack()
        self.login_button.pack()
        self.login_new_user.pack()
        self.exit_button.pack(side='bottom')

    def remove_home_pack(self):
        """ Remove the home screen objects"""
        self.greeting_label.pack_forget()
        self.login_button.pack_forget()
        self.login_new_user.pack_forget()
        self.exit_button.pack_forget()

    def clear_login_data(self):
        """ Clear the dict data for login and login user data"""
        self.login_user_dictionary = {}
        self.current_user_data_dictionary = {}

    def clear_new_user_data(self):
        """ Clea the dict data for new user"""
        self.new_user_dictionary = {}

    def login_click(self):
        """ Login button clicked """
        self.clear_login_data()
        self.remove_home_pack()
        self.build_login()

    def build_login(self):
        """ Build/Pack Login screen objects"""
        self.screen_state = 'login'
        self.login_greeting_label.pack()
        self.username_label.pack()
        self.username_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.back_button.pack(side='bottom')
        self.submit_button.pack(side='bottom')

    def back_login(self):
        self.remove_login()
        self.home()

    def back_create_user(self):
        self.remove_create_user()
        self.home()

    def submit_login(self):
        self.retrieve_login()
        self.remove_login()

        success = self.verify_login()
        if success:
            self.get_additional_data()
            self.successful_login()
        else:
            self.failed_login()

    def submit_create_user(self):
        self.retrieve_create_user()
        success = self.verify_new_user()

        if success:
            self.remove_create_user()
            self.successful_create_user()
        else:
            self.failed_create_user()

    def back_click(self):
        """ Back button clicked """
        switcher = {
            "init": None,
            "home": self.remove_home_pack,
            "login": self.back_login,
            'create': self.back_create_user,
        }
        func = switcher.get(self.screen_state)
        func()

    def submit_click(self):
        """ Submit button clicked """
        switcher = {
            "login": self.submit_login,
            'create': self.submit_create_user,
        }
        func = switcher.get(self.screen_state)
        func()

    def done_click(self):
        """ Done Button clicked"""
        switcher = {
            "login": self.done_login,
            'create': self.done_create_user,
        }
        func = switcher.get(self.screen_state)
        func()

    def retrieve_login(self):
        self.login_user_dictionary = {"username": self.username_entry.get(),
                                      "password": self.password_entry.get()}
        self.remove_login()

        if self.login_user_dictionary["password"] == '' or None:
            pass

        else:
            self.current_user_db_password = find_user_db(self.login_user_dictionary["username"])

    def verify_login(self):
        """ Verify login details provided. Assume not matching until proved otherwise """
        success = False

        if self.current_user_db_password == self.login_user_dictionary["password"]:
            success = True

        return success

    def verify_new_user(self):
        """ Verify new user details provided. """
        success = True
        if '' in self.new_user_dictionary.values():  # nothing contained in the entry boxes
            success = False

            key_list = []

            self.new_user_bad_fields = []
            for key, value in self.new_user_dictionary.items():
                key_list.append(key)
                if value == '':
                    self.new_user_bad_fields.append(key)

            white_list = list(set(key_list) - set(self.new_user_bad_fields))
            for i in range(len(white_list)):
                code_string = "self.new_" + white_list[i] + "_entry.config(background='white')"
                exec(code_string)

            for i in range(len(self.new_user_bad_fields)):
                code_string = "self.new_" + self.new_user_bad_fields[i] + "_entry.config(background='red')"
                exec(code_string)
                # print(code_string)

        return success

    def remove_login(self):
        """ Removes the login elements """
        self.login_greeting_label.pack_forget()
        self.username_label.pack_forget()
        self.username_entry.pack_forget()
        self.password_label.pack_forget()
        self.password_entry.pack_forget()
        self.back_button.pack_forget()
        self.submit_button.pack_forget()
        self.username_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')

    def create_new_user_click(self):
        """New User button clicked """
        self.remove_home_pack()
        self.build_create_user()

    def build_create_user(self):
        """ Build/Pack Create new user screen """
        self.screen_state = 'create'
        self.new_greeting_label.pack()
        self.new_first_name_label.pack()
        self.new_first_name_entry.pack()
        self.new_last_name_label.pack()
        self.new_last_name_entry.pack()
        self.new_username_label.pack()
        self.new_username_entry.pack()
        self.new_email_label.pack()
        self.new_email_entry.pack()
        self.new_phone_number_label.pack()
        self.new_phone_number_entry.pack()
        self.new_password_label.pack()
        self.new_password_entry.pack()
        self.new_password_confirm_label.pack()
        self.new_password_confirm_entry.pack()
        self.back_button.pack(side='bottom')
        self.submit_button.pack(side='bottom')

    def remove_create_user(self):
        """ Removes the create new user elements"""
        self.new_greeting_label.pack_forget()
        self.new_first_name_label.pack_forget()
        self.new_first_name_entry.pack_forget()
        self.new_last_name_label.pack_forget()
        self.new_last_name_entry.pack_forget()
        self.new_username_label.pack_forget()
        self.new_username_entry.pack_forget()
        self.new_email_label.pack_forget()
        self.new_email_entry.pack_forget()
        self.new_phone_number_label.pack_forget()
        self.new_phone_number_entry.pack_forget()
        self.new_password_label.pack_forget()
        self.new_password_entry.pack_forget()
        self.new_password_confirm_label.pack_forget()
        self.new_password_confirm_entry.pack_forget()
        self.back_button.pack_forget()
        self.submit_button.pack_forget()
        self.new_first_name_entry.delete(0, 'end')
        self.new_last_name_entry.delete(0, 'end')
        self.new_username_entry.delete(0, 'end')
        self.new_email_entry.delete(0, 'end')
        self.new_phone_number_entry.delete(0, 'end')
        self.new_password_entry.delete(0, 'end')
        self.new_password_confirm_entry.delete(0, 'end')

    def get_additional_data(self):
        data = get_user_detail(self.login_user_dictionary["username"])
        self.current_user_data_dictionary = dict(zip(self.fields, data))

    def retrieve_create_user(self):
        """ Retrieves the create new user data"""
        # db interaction now.
        self.new_user_dictionary = {"first_name": self.new_first_name_entry.get(),
                                    "last_name": self.new_last_name_entry.get(),
                                    "username": self.new_username_entry.get(),
                                    "email": self.new_email_entry.get(),
                                    "phone_number": self.new_phone_number_entry.get(),
                                    "password": self.new_password_entry.get()}

        self.verify_new_user()
        # there should be verifications and checking to make sure there isn't garbage being entered into the db.
        create_user_db(self.new_user_dictionary)

    def successful_login(self):
        """ Forward Successful login """
        self.welcome_label_text.set("Welcome"
                                    + " " + self.current_user_data_dictionary["first_name"]
                                    + " " + self.current_user_data_dictionary["last_name"])

        self.login_success_label.pack()
        self.welcome_label.pack()
        self.done_button.pack()

    def failed_login(self):
        """ Forward Failed login """
        self.reject_label_text.set("There is no such user registered,\n perhaps you got confused \nbecause there "
                                   "were too many options?")
        self.login_failure_label.pack()
        self.reject_label.pack()
        self.done_button.pack()

    def successful_create_user(self):
        """ Forward Successful create user """
        self.new_success_label.pack()
        self.welcome_label_text.set("Welcome"
                                    + " " + self.new_user_dictionary["first_name"]
                                    + " " + self.new_user_dictionary["last_name"])
        self.welcome_label.pack()
        self.done_button.pack()

    def failed_create_user(self):
        """ Forward Failed create user """
        # popup window
        popup_message()

        # TODO: also a bug where we go, back after this, fix it for future.
        # self.reject_label_text.set("You have not populated\n all the required data fields.\n Did you got confused?")
        # self.create_failure_label.pack()
        # self.reject_label.pack()
        # self.done_button.pack()
        # failures can be due to:
        # 1. More data needed.
        # 2. Username taken

    def done_login(self):
        """ Done button pressed after login and greeting - reset"""
        self.login_success_label.pack_forget()
        self.login_failure_label.pack_forget()
        self.welcome_label.pack_forget()
        self.reject_label.pack_forget()
        self.done_button.pack_forget()
        self.home()

    def done_create_user(self):
        """ Done button pressed after new user created and added to db - reset"""
        self.new_success_label.pack_forget()
        self.create_failure_label.pack_forget()
        self.welcome_label.pack_forget()
        self.reject_label.pack_forget()
        self.done_button.pack_forget()
        self.home()


def main():
    root = Tk()
    login_box = LoginBox(root)
    root.mainloop()


if __name__ == '__main__':
    main()
