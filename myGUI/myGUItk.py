from tkinter import *
class window():
	def __init__(self,title):
		self.tk=Tk()
		self.tk.title(title)
		self._last_child_ids=None
		self._w='.'
		self.children={}
	def show(self):
		self.tk.mainloop()
	def label(self,text,x,y,key=None):
		txt=Label(self.tk,text=text)
		txt.grid(row=y,column=x)
		return txt
		if key is not None:
			self.children[key]=txt
	def button(self,text,x,y,onpress=None,key=None):
		btn=Button(self.tk,text=text,command=onpress)
		btn.grid(row=y,column=x)
		if key is not None:
			self.children[key]=btn
		return btn
	def textinput(self,x,y,key=None):
		ent=Entry(self.tk)
		if key is not None:
			self.children[key]=ent
		ent.grid(row=y,column=x)
		return ent
	def get(self,entry):
		self.entry=self.children[entry]
		return self.entry.get()
	def title(self,title):
		self.tk.title(title)
	def textbox(self,x,y,key=None):
		pass