from tkinter import *

logged_in = False
button_color_off = "#eeeeee"


class MainWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.config(bg="#222831")
        self.wm_geometry("300x250")
        self.title("Account Login")
        self.page_container = Frame(self, bg="#222831")
        self.page_container.pack(side="top", fill="both", expand=True)

        # create a Form label
        self.page_label = Label(self.page_container, text="Choose Login Or Register", fg="#eeeeee", bg="#222831",
                                width="300", height="2", font=("Colfax", 8, "bold"))
        self.page_label.pack(side="top", fill="both", expand=True)

        # create frame to hold buttons
        self.button_frame = Frame(self.page_container, bg="#222831")
        self.button_frame.pack(side="bottom", fill="both", expand=True)

        # create Login Button
        self.login_button = Button(self.button_frame, bg=button_color_off, text="Login", height="2", width="30",
                                   font=("Colfax", 8, "bold"), command=self.login_page)
        self.login_button.grid(row=1, column=2, pady=5, padx=40)

        # create a register button
        self.register_button = Button(self.button_frame, bg=button_color_off, text="Register", height="2", width="30",
                                      font=("Colfax", 8, "bold"), command=self.register_page)
        self.register_button.grid(row=2, column=2, pady=5, padx=40)

    def login_page(self):
        self.page_label.config(text="Login page", fg="#eeeeee", bg="#222831", width="300", height="2",
                               font=("Colfax", 12, "bold"))
        self.wm_geometry("600x500")
        # hide the button frame
        self.button_frame.pack_forget()
        # hide the register frame if we came from it
        try:
            self.register_frame.pack_forget()
        except AttributeError:
            # an error will occur if user open the registration page without not from the login page
            pass

        # create log in frame
        self.login_frame = Frame(self.page_container, bg="#222831")
        self.login_frame.pack(side="bottom", fill="both", expand=True)

        # log in form

        # create username label and entry
        self.username_label = Label(self.login_frame, fg="#00adb5", bg="#222831", text="Username * ",
                                    font=("Colfax", 12, "bold"))
        self.username_label.grid(row=0, column=2, sticky="w", pady=10, padx=250)
        self.username_entry = Entry(self.login_frame, width=50)
        self.username_entry.grid(row=1, column=2, columnspan=3, sticky="w", pady=10, padx=140)

        # create password label and entry
        self.space = Label(self.login_frame, bg="#222831", text="")
        self.space.grid(row=2, column=2, sticky="w", pady=5, padx=5)
        self.password_label = Label(self.login_frame, fg="#00adb5", bg="#222831", text="Password * ",
                                    font=("Colfax", 12, "bold"))
        self.password_label.grid(row=3, column=2, sticky="w", pady=10, padx=250)
        self.password_entry = Entry(self.login_frame, show='*', width=50)
        self.password_entry.grid(row=4, column=2, columnspan=3, sticky="w", pady=10, padx=140)

        # create form submit button
        self.space2 = Label(self.login_frame, bg="#222831", text="")
        self.space2.grid(row=5, column=2, sticky="w", pady=5, padx=5)
        self.submit_button = Button(self.login_frame, text="Login", width=30, height=1, command=self.verify_user)
        self.submit_button.grid(row=6, column=2, sticky="w", pady=10, padx=180)
        self.register_button = Button(self.login_frame, text="Register", width=30, height=1, command=self.register_page)
        self.register_button.grid(row=7, column=2, sticky="w", pady=5, padx=180)

    def register_page(self):
        self.page_label.config(text="Register page", fg="#eeeeee", bg="#222831", width="300", height="1",
                               font=("Colfax", 12, "bold"))
        self.wm_geometry("600x500")
        # hide the button frame
        self.button_frame.pack_forget()
        # hide the login frame if we came from it
        try:
            self.login_frame.pack_forget()
        except AttributeError:
            # an error will occur if user open the registration page without not from the login page
            pass

        # create register frame
        self.register_frame = Frame(self.page_container, bg="#222831")
        self.register_frame.pack(side="bottom", fill="both", expand=True)

        # register form

        # create username label and entry
        self.username_label = Label(self.register_frame, fg="#00adb5", bg="#222831", text="Username * ",
                                    font=("Colfax", 12, "bold"))
        self.username_label.grid(row=0, column=2, sticky="w", pady=5, padx=250)
        self.username_entry = Entry(self.register_frame, width=50)
        self.username_entry.grid(row=1, column=2, columnspan=3, sticky="w", pady=5, padx=140)

        # create email label and entry
        self.email_label = Label(self.register_frame, fg="#00adb5", bg="#222831", text="Email * ",
                                 font=("Colfax", 12, "bold"))
        self.email_label.grid(row=2, column=2, sticky="w", pady=5, padx=270)
        self.email_entry = Entry(self.register_frame, width=50)
        self.email_entry.grid(row=3, column=2, columnspan=3, sticky="w", pady=5, padx=140)

        # create password label and entry
        self.password_label = Label(self.register_frame, fg="#00adb5", bg="#222831", text="Password * ",
                                    font=("Colfax", 12, "bold"))
        self.password_label.grid(row=4, column=2, sticky="w", pady=5, padx=250)
        self.password_entry = Entry(self.register_frame, show='*', width=50)
        self.password_entry.grid(row=5, column=2, columnspan=3, sticky="w", pady=5, padx=140)

        # create confirm password label and entry
        self.confirm_password_label = Label(self.register_frame, fg="#00adb5", bg="#222831", text="Confirm Password * ",
                                    font=("Colfax", 12, "bold"))
        self.confirm_password_label.grid(row=6, column=2, sticky="w", pady=5, padx=220)
        self.confirm_password_entry = Entry(self.register_frame, show='*', width=50)
        self.confirm_password_entry.grid(row=7, column=2, columnspan=3, sticky="w", pady=5, padx=140)

        # create form submit button
        self.space2 = Label(self.register_frame, bg="#222831", text="")
        self.space2.grid(row=8, column=2, sticky="w", pady=5, padx=5)
        self.submit_button = Button(self.register_frame, text="Register", width=30, height=1, command=self.register_user)
        self.submit_button.grid(row=9, column=2, sticky="w", pady=10, padx=180)
        self.login_button = Button(self.register_frame, text="Login", width=30, height=1, command=self.login_page)
        self.login_button.grid(row=10, column=2, sticky="w", pady=5, padx=180)


    def verify_user(self):
        # define the log in global variables
        global username_verify, password_verify
        username_verify = self.username_entry.get()
        password_verify = self.password_entry.get()
        print(username_verify)
        print(password_verify)

    def register_user(self):
        # define the log in global variables
        global username, password, email, confirm_password
        username = self.username_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()
        confirm_password = self.confirm_password_entry.get()
        print(username)
        print(password)
        print(email)
        print(confirm_password)

