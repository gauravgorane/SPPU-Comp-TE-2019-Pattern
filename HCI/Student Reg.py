import tkinter as tk
from tkinter import messagebox

class StudentRegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Registration Form")

        # Student Name
        self.label_name = tk.Label(root, text="Name:")
        self.label_name.pack(pady=10)
        self.entry_name = tk.Entry(root)
        self.entry_name.pack(pady=10)

        # Student Email
        self.label_email = tk.Label(root, text="Email:")
        self.label_email.pack(pady=10)
        self.entry_email = tk.Entry(root)
        self.entry_email.pack(pady=10)

        # Course Selection (using Listbox)
        self.label_course = tk.Label(root, text="Select Course:")
        self.label_course.pack(pady=10)
        self.courses = ["Math", "Science", "English", "History"]
        self.selected_course = tk.StringVar()
        self.course_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=len(self.courses), exportselection=False)
        for course in self.courses:
            self.course_listbox.insert(tk.END, course)
        self.course_listbox.pack(pady=10)

        # Gender Selection (using Checkbuttons)
        self.label_gender = tk.Label(root, text="Select Gender:")
        self.label_gender.pack(pady=10)
        self.gender_var = tk.StringVar()
        self.checkbutton_male = tk.Checkbutton(root, text="Male", variable=self.gender_var, onvalue="Male")
        self.checkbutton_female = tk.Checkbutton(root, text="Female", variable=self.gender_var, onvalue="Female")
        self.checkbutton_male.pack()
        self.checkbutton_female.pack()

        # Submit Button
        self.submit_button = tk.Button(root, text="Submit", command=self.submit_form)
        self.submit_button.pack(pady=20)

    def submit_form(self):
        # Get values from the form
        name = self.entry_name.get()
        email = self.entry_email.get()
        selected_course_index = self.course_listbox.curselection()
        selected_gender = self.gender_var.get()

        # Validate form entries
        if not name or not email or not selected_course_index or not selected_gender:
            messagebox.showerror("Error", "Please fill in all the fields.")
            return

        selected_course = self.courses[selected_course_index[0]]

        # Display a summary message
        message = f"Registration Successful!\nName: {name}\nEmail: {email}\nCourse: {selected_course}\nGender: {selected_gender}"
        messagebox.showinfo("Success", message)

def main():
    root = tk.Tk()
    registration_form = StudentRegistrationForm(root)
    root.mainloop()

if __name__ == "__main__":
    main()
