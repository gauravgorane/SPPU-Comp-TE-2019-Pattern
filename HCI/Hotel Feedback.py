import tkinter as tk
from tkinter import messagebox

class CustomerFeedbackForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Feedback Form")

        # Customer Name
        self.label_name = tk.Label(root, text="Name:")
        self.label_name.pack(pady=10)
        self.entry_name = tk.Entry(root, width=30)
        self.entry_name.pack(pady=10)

        # Feedback Text
        self.label_feedback = tk.Label(root, text="Feedback:")
        self.label_feedback.pack(pady=10)
        self.text_feedback = tk.Text(root, height=5, width=40)
        self.text_feedback.pack(pady=10)

        # Ratings Checkbuttons
        self.label_ratings = tk.Label(root, text="Rate the food:")
        self.label_ratings.pack(pady=10)

        self.quality_var = tk.IntVar()
        self.label_quality = tk.Label(root, text="Quality:")
        self.label_quality.pack()
        self.checkbutton_quality = tk.Checkbutton(root, text="Excellent", variable=self.quality_var, onvalue=5, offvalue=0)
        self.checkbutton_quality.pack()

        self.service_var = tk.IntVar()
        self.label_service = tk.Label(root, text="Service:")
        self.label_service.pack()
        self.checkbutton_service = tk.Checkbutton(root, text="Excellent", variable=self.service_var, onvalue=5, offvalue=0)
        self.checkbutton_service.pack()

        self.cleanliness_var = tk.IntVar()
        self.label_cleanliness = tk.Label(root, text="Cleanliness:")
        self.label_cleanliness.pack()
        self.checkbutton_cleanliness = tk.Checkbutton(root, text="Excellent", variable=self.cleanliness_var, onvalue=5, offvalue=0)
        self.checkbutton_cleanliness.pack()

        # Submit Button
        self.submit_button = tk.Button(root, text="Submit Feedback", command=self.submit_feedback)
        self.submit_button.pack(pady=20)

    def submit_feedback(self):
        # Get values from the form
        name = self.entry_name.get()
        feedback = self.text_feedback.get("1.0", tk.END).strip()
        quality_rating = self.quality_var.get()
        service_rating = self.service_var.get()
        cleanliness_rating = self.cleanliness_var.get()

        # Validate form entries
        if not name or not feedback or quality_rating == 0 or service_rating == 0 or cleanliness_rating == 0:
            messagebox.showerror("Error", "Please fill in all the fields and provide ratings.")
            return

        # You can add additional logic here, such as saving the feedback to a database

        # Display a confirmation message
        message = f"Thank you, {name}!\nYour feedback:\n{feedback}\nRatings:\nQuality: {quality_rating}\nService: {service_rating}\nCleanliness: {cleanliness_rating}"
        messagebox.showinfo("Feedback Submitted", message)

def main():
    root = tk.Tk()
    feedback_form = CustomerFeedbackForm(root)
    root.mainloop()

if __name__ == "__main__":
    main()
