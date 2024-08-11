import tkinter as tk
from tkinter import messagebox

class SignUpWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign Up")

        # Set the window size
        self.root.geometry("400x300")

        # User Name
        self.label_name = tk.Label(root, text="Name:")
        self.label_name.pack(pady=10)
        self.entry_name = tk.Entry(root, width=30)
        self.entry_name.pack(pady=10)

        # User Email
        self.label_email = tk.Label(root, text="Email:")
        self.label_email.pack(pady=10)
        self.entry_email = tk.Entry(root, width=30)
        self.entry_email.pack(pady=10)

        # User Password
        self.label_password = tk.Label(root, text="Password:")
        self.label_password.pack(pady=10)
        self.entry_password = tk.Entry(root, show="*", width=30)  # Mask the password
        self.entry_password.pack(pady=10)

        # Submit Button
        self.submit_button = tk.Button(root, text="Sign Up", command=self.sign_up, width=20)
        self.submit_button.pack(pady=20)

    def sign_up(self):
        # Get values from the form
        name = self.entry_name.get()
        email = self.entry_email.get()
        password = self.entry_password.get()

        # Validate form entries
        if not name or not email or not password:
            messagebox.showerror("Error", "Please fill in all the fields.")
            return

        # You can add additional logic here, such as saving the user information to a database

        # Display a confirmation message
        message = f"Sign Up Successful!\nName: {name}\nEmail: {email}"
        messagebox.showinfo("Success", message)

def main():
    root = tk.Tk()
    signup_window = SignUpWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
