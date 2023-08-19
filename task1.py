############################## TO DO LIST ############################################
from  tkinter import * 
import tkinter.messagebox

def mytask():
    
    input_text=""
    def add():
        input_text=entry_task.get(1.0, "end-1c")     
        if input_text=="":
            tkinter.messagebox.showwarning(title="Warning!",message="Please Enter some Text")
        else:
            listbox_task.insert(END,input_text)
            #close the root1 window
            root1.destroy()
    root1=Tk()
    root1.title("Add task")
    entry_task=Text(root1,width=30,height=3.5)
    entry_task.pack()
    button_temp=Button(root1,text="Add a task",command=add)
    button_temp.pack()
    root1.mainloop()
    

#function to facilitate the delete task from the Listbox
def todelete(): 
    selected=listbox_task.curselection()
    listbox_task.delete(selected[0])


def tocomplete():
    marked=listbox_task.curselection()
    temp=marked[0]              #store the text of selected item in a string
    temp_marked=listbox_task.get(marked)        #update it 
    temp_marked=temp_marked+" ✅"
    #delete it then insert it 
    listbox_task.delete(temp)
    listbox_task.insert(temp,temp_marked)

window=Tk()
window.title("My To-Do List")

#frame container having different widgets
frame_task=Frame(window)
frame_task.pack()

#listbox
listbox_task=Listbox(frame_task,bg="white",fg="black",height=7,width=40,font = "Georgia")  
listbox_task.pack(side=tkinter.LEFT)

#Scrolldown
scrollbar_task=Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT,fill=tkinter.Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)   #. The command option is used to associate a function or method that will be called when the scrollbar is moved.
#Button widget 
entry_b=Button(window,text="Add the task",width=30,command=mytask,bg="cyan")
entry_b.pack(pady=2)

delete_b=Button(window,text="Delete selected task",width=30,command=todelete,bg="red")
delete_b.pack(pady=2)

mark_b=Button(window,text="Mark as completed ",width=30,command=tocomplete,bg="green")
mark_b.pack(pady=2)


window.mainloop()
