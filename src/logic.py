import re
from parser import ExpressionParser

parser = ExpressionParser()
result = "0"

def append_value(value):
    """non digits get surrounded by spaces"""
    pattern = r'[0-9]' # Matches any single digit
    return str(value) if re.match(pattern, str(value)) else " " + str(value) + " "
def pretty_value_to_eval(display_var):
    display_var.set(display_var.get().replace('^', '**'))
    display_var.set(display_var.get().replace(' ', ''))
    display_var.set(display_var.get().replace('ANS', result))
    return display_var
def on_button_click(value, display_var):
    if (display_var.get() == "error"):
        display_var.set("")
    match value:
        case 'x^y':
            display_var.set(display_var.get() + append_value('^'))
        case 'EXP':
            display_var.set(display_var.get() + append_value('e'))
        case '(x)':
            display_var.set('(' + display_var.get() + ')')
        case 'C':
            display_var.set("")
        case 'Del':
            current = display_var.get()
            display_var.set(current[:-1])
        case 'Ans':
            display_var.set(display_var.get() + append_value('ANS'))
        case '=':
            try:
                global result
                parsed_value = pretty_value_to_eval(display_var)
                result = str(parser.parse_and_evaluate(parsed_value.get()))
                display_var.set(result)
            except Exception as e:
                display_var.set("Error")
        case _:
            display_var.set(display_var.get() + append_value(value))
