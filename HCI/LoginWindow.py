import tkinter as tk
from tkinter import messagebox

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Window")

        self.label_username = tk.Label(root, text="Username:")
        self.label_username.pack(pady=10)
        self.entry_username = tk.Entry(root)
        self.entry_username.pack(pady=10)

        self.label_password = tk.Label(root, text="Password:")
        self.label_password.pack(pady=10)
        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.pack(pady=10)

        self.button_login = tk.Button(root, text="Login", command=self.login)
        self.button_login.pack(pady=20)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Replace this with your actual authentication logic
        if username == "admin" and password == "password":
            messagebox.showinfo("Login Successful", "Welcome, {}".format(username))
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

def main():
    root = tk.Tk()
    login_window = LoginWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
