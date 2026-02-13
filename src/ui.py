import tkinter as tk
from logic import on_button_click, append_value, pretty_value_to_eval

def create_ui():
    root = tk.Tk()

    root.title("Calculator")
    root.geometry("400x600")

    # Configure rows and columns to be resizable (weight 1)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.columnconfigure(3, weight=1)
    root.columnconfigure(4, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)
    root.rowconfigure(4, weight=1)
    root.rowconfigure(5, weight=1)
    root.rowconfigure(6, weight=1)
    root.rowconfigure(7, weight=1)

    display_var = tk.StringVar()

    screen = tk.Entry(
        root,
        textvariable=display_var,
        font=("Arial", 18),
        bd=5,
        relief="ridge",
        justify="right"
    )

    screen.grid(row=0, column=0, columnspan=5, rowspan=2, padx=10, pady=10)

    button1 = tk.Button(root, text="1", command=lambda: on_button_click(1, display_var))
    button2 = tk.Button(root, text="2", command=lambda: on_button_click(2, display_var))
    button3 = tk.Button(root, text="3", command=lambda: on_button_click(3, display_var))
    button4 = tk.Button(root, text="4", command=lambda: on_button_click(4, display_var))
    button5 = tk.Button(root, text="5", command=lambda: on_button_click(5, display_var))
    button6 = tk.Button(root, text="6", command=lambda: on_button_click(6, display_var))
    button7 = tk.Button(root, text="7", command=lambda: on_button_click(7, display_var))
    button8 = tk.Button(root, text="8", command=lambda: on_button_click(8, display_var))
    button9 = tk.Button(root, text="9", command=lambda: on_button_click(9, display_var))
    button0 = tk.Button(root, text="0", command=lambda: on_button_click(0, display_var))
    button_dot = tk.Button(root, text=".", command=lambda: on_button_click('.', display_var))
    button_equal = tk.Button(root, text="=", command=lambda: on_button_click('=', display_var))
    button_plus = tk.Button(root, text="+", command=lambda: on_button_click('+', display_var))
    button_minus = tk.Button(root, text="-", command=lambda: on_button_click('-', display_var))
    button_multiply = tk.Button(root, text="*", command=lambda: on_button_click('*', display_var))
    button_divide = tk.Button(root, text="/", command=lambda: on_button_click('/', display_var))
    button_exp = tk.Button(root, text="EXP", command=lambda: on_button_click('EXP', display_var))
    button_clear = tk.Button(root, text="C", command=lambda: on_button_click('C', display_var))
    button_answer = tk.Button(root, text="Ans", command=lambda: on_button_click('Ans', display_var))
    button_delete = tk.Button(root, text="Del", command=lambda: on_button_click('Del', display_var))
    button_smart_parentheses = tk.Button(root, text="(x)", command=lambda: on_button_click('(x)', display_var))
    button_open_paren = tk.Button(root, text="(", command=lambda: on_button_click('(', display_var))
    button_close_paren = tk.Button(root, text=")", command=lambda: on_button_click(')', display_var))
    button_raise = tk.Button(root, text="x^y", command=lambda: on_button_click('x^y', display_var))

    # Place widgets using grid()
    # Use sticky="nsew" to make them expand with the cell
    button_smart_parentheses.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
    button_open_paren.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
    button_close_paren.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")
    button_raise.grid(row=2, column=3, padx=10, pady=10, sticky="nsew")
    button7.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
    button8.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")
    button9.grid(row=3, column=2, padx=10, pady=10, sticky="nsew")
    button4.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")
    button5.grid(row=4, column=1, padx=10, pady=10, sticky="nsew")
    button6.grid(row=4, column=2, padx=10, pady=10, sticky="nsew")
    button1.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")
    button2.grid(row=5, column=1, padx=10, pady=10, sticky="nsew")
    button3.grid(row=5, column=2, padx=10, pady=10, sticky="nsew")
    button0.grid(row=6, column=0, padx=10, pady=10, sticky="nsew")
    button_equal.grid(row=5, column=4, rowspan=2, padx=10, pady=10, sticky="nsew")
    button_dot.grid(row=6, column=1, padx=10, pady=10, sticky="nsew")
    button_exp.grid(row=6, column=2, padx=10, pady=10, sticky="nsew")
    button_plus.grid(row=6, column=3, padx=10, pady=10, sticky="nsew")
    button_minus.grid(row=5, column=3, padx=10, pady=10, sticky="nsew")
    button_multiply.grid(row=4, column=3, padx=10, pady=10, sticky="nsew")
    button_divide.grid(row=3, column=3, padx=10, pady=10, sticky="nsew")
    button_clear.grid(row=2, column=4, padx=10, pady=10, sticky="nsew")
    button_delete.grid(row=3, column=4, padx=10, pady=10, sticky="nsew")
    button_answer.grid(row=4, column=4, padx=10, pady=10, sticky="nsew")


    root.mainloop()
