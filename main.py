'''
TODO: 
Jako luokkiin
Kommentit kuntoon
Tallennusfunktio


'''
#Importtaukset
from tkinter import *
from tkinter import messagebox
 
# lista, johon tehtävät tallennetaan
tasks_list = []
counter = 1

def insertTask(inputError, enterTaskField, TextArea, clear_taskField):
        global counter
        value = inputError() 
        if value == 0 :
            return
        content = enterTaskField.get() + "\n"
 
    # tallentaa tehtävän listaan
        tasks_list.append(content) 
    # lisää tehtävän sovelluksen tekstikenttään
        TextArea.insert('end -1 chars', "[ " + str(counter) + " ] " + content)
        counter += 1
        clear_taskField()

class main: #Sovelluksen pääluokka. Sisältää päälogiikan

    def inputError(enterTaskField) :     
        if enterTaskField.get() == "" :
            messagebox.showerror("Input Error")   
            return 0
        return 1
 
    def clear_taskNumberField(taskNumberField) :
     
        taskNumberField.delete(0.0, END)
 
    def clear_taskField(enterTaskField) :
        enterTaskField.delete(0, END)
 
def delete(taskNumberField, clear_taskNumberField, TextArea) :     
    global counter    
    if len(tasks_list) == 0 :      # Jos tyhjä
        messagebox.showerror("No task")
        return
 
    # Mikä tehtävä poistetaan
    number = taskNumberField.get(1.0, END)
 
    # checking for input error when
    # empty input in task number field
    if number == "\n" :
        messagebox.showerror("input error")
        return
     
    else :
        task_no = int(number)

    clear_taskNumberField()
     
    # deleted specified task from the list
    tasks_list.pop(task_no - 1)
 
    # decremented
    counter -= 1
     
    # whole content of text area widget is deleted
    TextArea.delete(1.0, END)
 
    # rewriting the task after deleting one task at a time
    for i in range(len(tasks_list)) :
        TextArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i])
     
class gui(): 
# Driver code
    if __name__ == "__main__" :
 
        gui = Tk()
        gui.configure(background = "light gray")
        gui.title("ToDo")
        gui.geometry("250x300")
 
    # create a label : Enter Your Task
        enterTask = Label(gui, text = "Enter Your Task", bg = "light gray")
 
    # create a text entry box
    # for typing the task
        enterTaskField = Entry(gui)
 
    # create a Submit Button and place into the root window
    # when user press the button, the command or
    # function affiliated to that button is executed

        Submit = Button(gui, text = "Submit", fg = "Black", bg = "gray", command = insertTask)
 
    # create a text area for the root
    # with lunida 13 font
    # text area is for writing the content
        TextArea = Text(gui, height = 5, width = 25, font = "lucida 13")
 
    # create a label : Delete Task Number
        taskNumber = Label(gui, text = "Delete Task Number", bg = "light gray")
                        
        taskNumberField = Text(gui, height = 1, width = 2, font = "lucida 13")
 
    # create a Delete Button and place into the root window
    # when user press the button, the command or
    # function affiliated to that button is executed .
        delete = Button(gui, text = "Delete", fg = "Black", bg = "gray", command = delete)
 
    # create a Exit Button and place into the root window
        Exit = Button(gui, text = "Exit", fg = "Black", bg = "gray", command = exit)
 
    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure.
        enterTask.grid(row = 0, column = 2)             
        enterTaskField.grid(row = 1, column = 2, ipadx = 50)                      
        Submit.grid(row = 2, column = 2)
        TextArea.grid(row = 3, column = 2, padx = 10, sticky = W)                 
        taskNumber.grid(row = 4, column = 2, pady = 5)                      
        taskNumberField.grid(row = 5, column = 2)             
        delete.grid(row = 6, column = 2, pady = 5)
                        
        Exit.grid(row = 7, column = 2)
 
    # start the GUI
        gui.mainloop()