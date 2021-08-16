from tkinter.messagebox import *
def info(title, message):
	return showinfo(title, message)
def error(title, message):
	return showerror(title, message)
def warning(title, message):
	return showwarning(title, message)
def question(title, message):
	return askquestion(title, message)