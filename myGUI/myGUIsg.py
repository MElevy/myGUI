import PySimpleGUI as sg
sg.theme('SystemDefault1')
sg.SetOptions(element_padding=(1,1))
window_closed=sg.WIN_CLOSED
themes=sg.theme_list()
def theme(theme):
	sg.theme(theme)
def window(title,layout,fin=False,maxed=False):
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
	return sg.T(text, font=font, key=key,visible=visible)
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
def menu(layout,tearoff=False, key=None, visible=True):
	return sg.Menu(layout, tearoff=tearoff, key=key,visible=visible)
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
def slider(range=(1, 100), value=None, visible=True,
					key=None, events=False, orientation='h',s=(None, None)):
	return sg.Slider(range=range,default_value=value, key=key,s=s,
								enable_events=events, orientation=orientation,visible=visible)
def frame(title, layout, s=(None, None),visible=True, key=None, relief='groove'):
	return sg.Frame(title, layout, s=s, visible=visible, key=key, relief=relief)
def popup_gettext(title, text=None):
	return sg.popup_get_text(title, text)