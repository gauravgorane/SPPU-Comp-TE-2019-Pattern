import tkinter as tk

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        # Entry fields for two numbers
        self.entry_num1 = tk.Entry(root, width=10, font=('Arial', 12))
        self.entry_num1.grid(row=0, column=0, padx=5, pady=10)

        self.entry_num2 = tk.Entry(root, width=10, font=('Arial', 12))
        self.entry_num2.grid(row=0, column=1, padx=5, pady=10)

        # Label to display the result
        self.result_label = tk.Label(root, text="Result: ")
        self.result_label.grid(row=1, column=0, columnspan=2, pady=10)

        # Buttons for operations
        operations = ['Addition', 'Subtraction', 'Multiplication', 'Division']
        
        row_val = 2
        col_val = 0

        for operation in operations:
            tk.Button(root, text=operation, width=15, height=2, command=lambda op=operation: self.calculate(op)).grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 1:
                col_val = 0
                row_val += 1

    def calculate(self, operation):
        try:
            num1 = float(self.entry_num1.get())
            num2 = float(self.entry_num2.get())

            if operation == 'Addition':
                result = num1 + num2
            elif operation == 'Subtraction':
                result = num1 - num2
            elif operation == 'Multiplication':
                result = num1 * num2
            elif operation == 'Division':
                result = num1 / num2

            self.result_label.config(text=f"Result: {result}")
        except Exception as e:
            self.result_label.config(text="Error")

def main():
    root = tk.Tk()
    calculator = SimpleCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
