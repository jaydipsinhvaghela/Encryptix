import tkinter
from tkinter import *
import tkinter as tk

                                

root=Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False,False)

task_list=[]

def deleteTask():
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w') as taskfie:
            for task in task_list:
                taskfie.write(task+"\n")
        listbox.delete(ANCHOR)
        

def fetchTaskForUpdate():
    try:
        task_index = listbox.curselection()[0]  
        task = listbox.get(task_index)
        task_entry.delete(0, END)
        task_entry.insert(0, task)
        update_button.config(command=lambda: saveUpdatedTask(task_index))
    except IndexError:
        pass

def saveUpdatedTask(task_index):
    new_task = task_entry.get()
    if new_task:
        task_list[task_index] = new_task + '\n'
        with open("tasklist.txt", 'w') as taskfile:
            for task in task_list:
                taskfile.write(task)
        listbox.delete(task_index)
        listbox.insert(task_index, new_task)            
        task_entry.delete(0, END)
        update_button.config(command=fetchTaskForUpdate)
    
def addTask():
    task=task_entry.get()
    task_entry.delete(0,END)
    
    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task)

def openTaskFile():
    try:
        with open("tasklist.txt","r") as taskfile:
            tasks=taskfile.readlines()
        for task in tasks:
            if task !='\n':
                task_list.append(task)
                listbox.insert(END,task)
    except:
        file=open('tasklist.txt','w')
        file.close()        

Image_Icon=PhotoImage(file="Images/task.png")
root.iconphoto(False,Image_Icon)

TOpImage=PhotoImage(file="Images/topbar.png")
Label(root,image=TOpImage)

dockimage=PhotoImage(file="Images/dock.png")
Label(root,image=dockimage,bg="#32405b").place(x=30,y=25)

noteimage=PhotoImage(file="Images/task.png")
Label(root,image=noteimage,bg="#32405b").place(x=340,y=25)

heading=Label(root,text="All List ",font="arial 20 bold",fg="white",bg="#32405b")
heading.place(x=130,y=20)

frame=Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=180)

task=StringVar()
task_entry=Entry(frame,width=18,font="arial 20",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

button=Button(frame,text="ADD",font="arial 20 bold",width=6,bg="#5a95ff",fg="#fff",bd=0,command=addTask)
button.place(x=300,y=0)

frame1=Frame(root,bd=3,width=700,height=280,bg="#32405b")
frame1.pack(pady=(270,250))

listbox=Listbox(frame1,font=('arial',12),width=40,height=16,bg="#32405b",fg="white",cursor="hand2",selectbackground="#5a95ff")

listbox.pack(side=LEFT,fill=BOTH,padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

#delete
Delete_icon=PhotoImage(file="Images/delete.png")
Button(root,image=Delete_icon,bg="#32405b",command=deleteTask).place(x=100,y=500)
# Button(root,image=Delete_icon,command=deleteTask).pack(side=BOTTOM,padx=13)

update_icon = PhotoImage(file="Images/edit2.png")
update_button = tk.Button(root, image=update_icon, bg="#32405b", command=fetchTaskForUpdate)
update_button.place(x=200, y=500)
                                                                                                                                                                
root.mainloop()

