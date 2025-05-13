from tkinter import *
from expression import Expression
from str_tokenizer import stringTokenizer

root = Tk()
root.title("Calculator")
screen_width = root.winfo_screenwidth()  
screen_height =root.winfo_screenheight()
width = 950
height = 500
x = (screen_width//2) - (width//2)
y = (screen_height//2) - (height//2)
root.geometry(f"{width}x{height}+{x}+{y}")
root.configure(background='alice blue')

def postfix():
    e = infix_entry.get()
    exp = stringTokenizer(e)
    expression = Expression(exp)
    postfix_label.config(text=expression.get_postfix())

def prefix():
    e = stringTokenizer(infix_entry.get())
    exp = Expression(e)
    expression = exp.get_postfix()
    prefix_label.config(text=exp.get_prefix(expression))

def evaluate():
    e = stringTokenizer(infix_entry.get())
    exp = Expression(e)
    expression = exp.get_postfix()
    evaluate_label.config(text=exp.get_evaluate(expression))

infix_label = Label(
    root, 
    text="Infix Exp:", 
    font=("Arial", 25), 
    width=10, 
    bg='steelblue', 
    fg='white', 
    bd=5, 
    relief="ridge"
)
infix_label.place(x=20, y=40)

infix_entry = Entry(
    root, 
    font=("Arial", 25), 
    width=37, 
    bg='white', 
    bd=5
)
infix_entry.place(x=250, y=41)

postfix_btn = Button(
    root, 
    text="Postfix Exp: ", 
    font=("Arial", 25), 
    width=10, 
    bg='steelblue', 
    fg='white', 
    bd=5,
    cursor='hand2', 
    relief="ridge",
    command= lambda:postfix()
)
postfix_btn.place(x=20, y=160)

postfix_label = Label(
    root, 
    font=("Arial", 25), 
    width=35, 
    bg='white', 
    bd=5, 
    anchor=W
)
postfix_label.place(x=250, y=168)

prefix_btn = Button(
    root, 
    text="Prefix Exp: ", 
    font=("Arial", 25), 
    width=10, 
    bg='steelblue', 
    fg='white', 
    bd=5,
    cursor='hand2', 
    relief="ridge",
    command= lambda:prefix()
)
prefix_btn.place(x=20, y=280)

prefix_label = Label(
    root, 
    font=("Arial", 25), 
    width=35, 
    bg='white', 
    bd=5, 
    anchor=W
)
prefix_label.place(x=250, y=287)

evaluate_btn = Button(
    root, 
    text='Evaluate', 
    font=("Arial", 25), 
    width=10, 
    bg='green',
    bd=5, 
    cursor='hand2',
    relief="ridge", 
    command= lambda:evaluate()
)
evaluate_btn.place(x=20, y=400)

evaluate_label = Label(
    root, 
    font=("Arial", 25), 
    width=35, 
    bg='white', 
    bd=5, 
    anchor=W
)
evaluate_label.place(x=250, y=407)

root.mainloop()


