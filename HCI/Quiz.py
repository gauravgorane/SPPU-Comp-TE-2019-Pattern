import tkinter as tk
from tkinter import messagebox

class OnlineQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Online Quiz")

        # Quiz Questions and Options
        self.questions = [
            {"question": "What is the capital of France?", "options": ["Berlin", "Madrid", "Paris", "Rome"], "correct": "Paris"},
            {"question": "Which planet is known as the Red Planet?", "options": ["Venus", "Mars", "Jupiter", "Saturn"], "correct": "Mars"},
            {"question": "What is the largest mammal?", "options": ["Elephant", "Blue Whale", "Giraffe", "Lion"], "correct": "Blue Whale"}
        ]

        # Initialize variables
        self.current_question_index = 0
        self.selected_option = tk.StringVar()

        # Create and place widgets in the window
        self.label_question = tk.Label(root, text="")
        self.label_question.pack(pady=10)

        self.option_buttons = []
        for i in range(4):
            button = tk.Radiobutton(root, text="", variable=self.selected_option, value="", command=self.update_selected_option)
            button.pack(pady=5)
            self.option_buttons.append(button)

        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.pack(pady=20)

        # Display the first question
        self.display_question()

    def display_question(self):
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.label_question.config(text=question_data["question"])

            for i in range(4):
                self.option_buttons[i].config(text=question_data["options"][i], value=question_data["options"][i])

            self.selected_option.set(None)
        else:
            self.show_results()

    def update_selected_option(self):
        pass  # You can add additional logic here if needed

    def next_question(self):
        if self.selected_option.get() is None:
            messagebox.showwarning("Warning", "Please select an option.")
        else:
            # Check the answer (you can add more sophisticated scoring logic)
            question_data = self.questions[self.current_question_index]
            if self.selected_option.get() == question_data["correct"]:
                messagebox.showinfo("Correct", "Your answer is correct!")
            else:
                messagebox.showinfo("Incorrect", "Your answer is incorrect. The correct answer is: {}".format(question_data["correct"]))

            # Move to the next question
            self.current_question_index += 1
            self.display_question()

    def show_results(self):
        messagebox.showinfo("Quiz Completed", "Congratulations! You have completed the quiz.")

def main():
    root = tk.Tk()
    quiz = OnlineQuiz(root)
    root.mainloop()

if __name__ == "__main__":
    main()
