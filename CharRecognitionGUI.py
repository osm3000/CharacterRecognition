#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.5
# In conjunction with Tcl version 8.6
#    Nov 21, 2015 03:29:17 PM
import sys
import os
import numpy
import matplotlib.pyplot as plt

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import CharRecognitionGUI_support
from FreemanEncoder import FreemanEncoder
from PIL import Image, ImageDraw
import KNN
import HMM

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    root.title("Digit Recognizer")
    geom = "848x493+374+90"
    root.geometry(geom)
    CharRecognitionGUI_support.set_Tk_var()
    w = New_Toplevel_1 (root)
    CharRecognitionGUI_support.init(root, w)
    root.mainloop()

w = None
def create_New_Toplevel_1(root, param=None):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    w.title('New_Toplevel_1')
    geom = "848x493+374+90"
    w.geometry(geom)
    CharRecognitionGUI_support.set_Tk_var()
    w_win = New_Toplevel_1 (w)
    CharRecognitionGUI_support.init(w, w_win, param)
    return w_win

def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None


class New_Toplevel_1:
    def __init__(self, master=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])
        master.configure(background="#d9d9d9")
        master.configure(highlightbackground="#d9d9d9")
        master.configure(highlightcolor="black")
        
        #user defined variables
        self.thumbnails = self.load_thumbnails(CharRecognitionGUI_support.thumbnails_path)
        self.PIL_image = Image.new("1", (300, 300), "white")
        self.hidden_canvas = ImageDraw.Draw(self.PIL_image)
        self.x = None
        self.y = None
        
        self.knn = KNN.KNN()
        self.fenc = FreemanEncoder()


        self.Clear = Button(master)
        self.Clear.place(relx=0.44, rely=0.14, height=24, width=78)
        self.Clear.configure(activebackground="#d9d9d9")
        self.Clear.configure(activeforeground="#000000")
        self.Clear.configure(background=_bgcolor)
        self.Clear.configure(disabledforeground="#a3a3a3")
        self.Clear.configure(foreground="#000000")
        self.Clear.configure(highlightbackground="#d9d9d9")
        self.Clear.configure(highlightcolor="black")
        self.Clear.configure(pady="0")
        self.Clear.configure(text='''Clear''')
        self.Clear.bind("<Button-1>",self.clear)

        self.Canvas1 = Canvas(master)
        self.Canvas1.place(relx=0.01, rely=0.02, relheight=0.61, relwidth=0.35)
        self.Canvas1.configure(background="white")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="black")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief=RIDGE)
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(width=378)
        self.Canvas1.bind("<B1-Motion>",self.drag)
        self.Canvas1.bind("<ButtonRelease-1>",self.drag_end)

        self.Save = Button(master)
        self.Save.place(relx=0.5, rely=0.04, height=24, width=77)
        self.Save.configure(activebackground="#d9d9d9")
        self.Save.configure(activeforeground="#000000")
        self.Save.configure(background=_bgcolor)
        self.Save.configure(disabledforeground="#a3a3a3")
        self.Save.configure(foreground="#000000")
        self.Save.configure(highlightbackground="#d9d9d9")
        self.Save.configure(highlightcolor="black")
        self.Save.configure(pady="0")
        self.Save.configure(text='''Save''')
        self.Save.bind("<Button-1>",self.save)

        self.Quit = Button(master)
        self.Quit.place(relx=0.44, rely=0.24, height=24, width=77)
        self.Quit.configure(activebackground="#d9d9d9")
        self.Quit.configure(activeforeground="#000000")
        self.Quit.configure(background=_bgcolor)
        self.Quit.configure(disabledforeground="#a3a3a3")
        self.Quit.configure(foreground="#000000")
        self.Quit.configure(highlightbackground="#d9d9d9")
        self.Quit.configure(highlightcolor="black")
        self.Quit.configure(pady="0")
        self.Quit.configure(text='''Quit''')
        self.Quit.bind("<Button-1>",self.quit)

        self.Frame1 = Frame(master)
        self.Frame1.place(relx=0.61, rely=0.02, relheight=0.6, relwidth=0.36)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background=_bgcolor)
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=305)

        self.Label1 = Label(master, wraplength=500, justify=LEFT)
        self.Label1.place(relx=0.01, rely=0.69, height=131, width=514)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background=_bgcolor)
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")

        self.TCombobox1 = ttk.Combobox(master)
        self.TCombobox1.place(relx=0.41, rely=0.39, relheight=0.06
                , relwidth=0.16)
        self.value_list = ['kNN','HMM','RandomForest',]
        self.TCombobox1.configure(values=self.value_list)
        self.TCombobox1.configure(textvariable=CharRecognitionGUI_support.combobox)
        self.TCombobox1.configure(takefocus="")
        
        self.TCombobox2 = ttk.Combobox(master)
        self.TCombobox2.place(relx=0.4, rely=0.04, height=24, width=77)
        self.value_list = ['0','1','2','3','4','5','6','7','8','9',]
        self.TCombobox2.configure(values=self.value_list)
        self.TCombobox2.configure(textvariable=CharRecognitionGUI_support.combobox2)
        self.TCombobox2.configure(takefocus="")
        self.TCombobox2.current(0)
        
        self.Frame2 = Frame(master)
        self.Frame2.place(relx=0.74, rely=0.71, relheight=0.24, relwidth=0.14)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background=_bgcolor)
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(width=150, height=150)

        self.Thumbnail = Label(master)
        self.Thumbnail.place(relx=0.75, rely=0.73, height=100, width=100)
        self.Thumbnail.configure(background=_bgcolor)
        self.Thumbnail.configure(disabledforeground="#a3a3a3")
        self.Thumbnail.configure(foreground="#000000")
        self._img1 = PhotoImage(file='./thumbnails/blank.gif')
        self.Thumbnail.configure(image=self._img1)
        self.Thumbnail.configure(text='''Label''')
        self.Thumbnail.configure(width=94)

        self.Recognize = Button(master)
        self.Recognize.place(relx=0.44, rely=0.53, height=24, width=87)
        self.Recognize.configure(activebackground="#d9d9d9")
        self.Recognize.configure(activeforeground="#000000")
        self.Recognize.configure(background=_bgcolor)
        self.Recognize.configure(disabledforeground="#a3a3a3")
        self.Recognize.configure(foreground="#000000")
        self.Recognize.configure(highlightbackground="#d9d9d9")
        self.Recognize.configure(highlightcolor="black")
        self.Recognize.configure(pady="0")
        self.Recognize.configure(text='''Recognize''')
        self.Recognize.bind("<Button-1>",self.recognize)

    def load_thumbnails(self, thumbnails_path):
        images = {}
        for thumb in os.listdir(thumbnails_path):
            thumb_name = os.path.splitext(thumb)[0]
            images[thumb_name] = thumbnails_path + '/' + thumb
        
        return images
    
    def quit(self, event):
        '''
        Event function to quit the drawer window
        '''
        sys.exit()
       
    def clear(self, event):
        '''
        Event function to clear the drawing canvas (draw white fill)
        '''
        self.Canvas1.delete("all")
        self.PIL_image = Image.new("1", (300, 300), "white")
        self.hidden_canvas = ImageDraw.Draw(self.PIL_image)
    
    def drag(self, event):
        '''
        Event function to start drawing on canvas when left mouse drag happens
        '''
        newx,newy=event.x,event.y
        if self.x is None:
            self.x,self.y=newx,newy
            return
        self.Canvas1.create_line((self.x,self.y,newx,newy), width=5, smooth=True)
        self.hidden_canvas.line((self.x,self.y,newx,newy), width=12)
        self.x,self.y=newx,newy
    
    def drag_end(self, event):
        '''
        Event function to stop drawing on canvas when mouse drag stops
        '''
        self.x,self.y=None,None
       
    def save(self, event):
        '''
        Event function to save the current canvas image in JPG format
        '''
        image_cnt = 1
        if not os.path.exists(CharRecognitionGUI_support.save_dir):
            os.makedirs(CharRecognitionGUI_support.save_dir)
        file_name = CharRecognitionGUI_support.save_dir + self.TCombobox2.get() + '_' + str(image_cnt) + ".jpg"
        
        while os.path.isfile(file_name):
            image_cnt += 1
            file_name = CharRecognitionGUI_support.save_dir + self.TCombobox2.get() + '_' + str(image_cnt) + ".jpg"
        
        self.PIL_image.save(file_name)
        self.Label1['text'] = 'SAVED!'

    def recognize(self, event):
        image = ~numpy.array(self.PIL_image.convert('L'))
        try:
            code = self.fenc.encode_freeman(image)
        except ValueError:
            self.Label1['text'] = 'Please redraw the image'
        self.Label1['text'] = str(code)
        
        if self.TCombobox1.get() == 'kNN':
            self.knn.knn_train('I:/eclipse_workspace/CharacterRecognition/teams_dataset', 1.0)
            pred = self.knn.knn_predict_one(code, 3)
            pred_thumb = self.thumbnails[pred[0]]
            self._image = PhotoImage(file=pred_thumb)
            self.Thumbnail.configure(image=self._image)
            
        else:
            self.Label1['text'] = 'Not Implemented yet'


if __name__ == '__main__':
    vp_start_gui()



