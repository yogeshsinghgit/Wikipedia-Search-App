# Github : yogeshsinghgit 
# ->Make Sure to Follow<-
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import wikipedia as wiki
import threading
 
# function ...
def search():
    search_data = ent.get()
    # insert data
    search_lbl['text'] = "Searching result for: {}".format(search_data.capitalize())
    try:
        data = wiki.summary(search_data, sentences=8)
    except Exception as e:
        data = e
    # delete current data ..
    ent.set('')
    text.delete(0.0,END)
    text.insert(0.0,data)
 
def call_search(*args):
    x = threading.Thread(target=search)
    x.start()
 
 
 
root = Tk()
root.title('Search Application')
root.geometry('320x480')
root.resizable(0,0)
root.configure(bg='white')
 
# test variable
ent = StringVar()
search_entry = Entry(root,width=30,font=("Sitka Small",12),bd=2,relief=RIDGE,textvariable=ent,justify=CENTER)
# Bind Entry Box with Enter Key
search_entry.bind('<Return>',call_search)
search_entry.place(x=15,y=20)
 
search_lbl = Label(root,text='Searching result for :',font=('arial',12,'bold'),bg='white')
search_lbl.place(x=15,y=70)
 
text = ScrolledText(root,font=('times',12),bd=4,relief=SUNKEN,wrap =WORD)
 
text.place(x=15,y=100,height=300,width=300)
 
search_btn = Button(root,text='Search',font=('arial',12,'bold'),width=10,command=call_search)
search_btn.place(x=10,y=420)
 
clear_btn = Button(root,text='Clear',font=('arial',12,'bold'),width=10,
                   command=lambda :text.delete(0.0,END))
clear_btn.place(x=105,y=420)
 
exit_btn = Button(root,text='Exit',font=('arial',12,'bold'),width=10,command=root.quit)
exit_btn.place(x=200,y=420)
 
 
root.mainloop()
