import PySimpleGUI as sg
sg.theme('SystemDefault1')
window_closed=sg.WIN_CLOSED
def theme(theme):
	sg.theme(theme)
def window(title,layout,fin=True,maxed=True):
	win=sg.Window(title,layout,finalize=fin)
	if fin and maxed:
		win.Maximize()
	return win
def button(text, s=(10,1),key=None,visible=True):
	return sg.B(text, s=s,key=key,visible=visible)
def entry(s=(60,1),key=None,events=False,visible=True, clear=False):
	return sg.In(s=s, key=key,enable_events=events,
						visible=visible, do_not_clear=not clear)
def label(text, font='Helvetica 11',key=None,visible=True):
	return sg.T(text, font=font, key=key,visble=visible)
def multiline(s=(50,10),r_stdout=False, r_stderr=False,
						key=None,events=False,visible=True):
	return sg.Multiline(s=s, reroute_stdout=r_stdout,visible=visible,
									reroute_stderr=r_stderr, key=key, enable_events=events)
def checkbox(text, on=False, key=None, disabled=False,events=False,visible=True):
	return sg.Checkbox(text,default=on,key=key,visible=visible,
									 disabled=disabled,enable_events=False)
def combo(values, key=None, events=None, s=(10,1),visible=True):
	return sg.Combo(values, key=key, enable_events=events, s=s,visible=visible)
def listbox(values, key=None, events=False, s=(50, 5), default=None,visible=True):
	return sg.Listbox(values, key=key, enable_events=events, 
								default_values=default,s=s,visible=visible)
def menu(layout):
	return sg.Menu(layout)
def radio(text, group, on=False, disabled=False,
				key=None,events=False,visible=True):
	return sg.Radio(text, group, default=on, visible=visible,
								disabled=disabled, key=key, enable_events=events)
def getfile(text='Select File', target=None,s=(10,1)):
	return sg.FileBrowse(text, target=target,s=s)
def getfolder(text='Select Folder', target=None,s=(10,1)):
	return sg.FolderBrowse(text, target=target,s=s)
def saveas(text='Save As...', target=None,s=(10,1)):
	return sg.SaveAs(text, target=target,s=s)