'''
TODO: 
Jako luokkiin (done ainakin osittain)
Kommentit kuntoon (done)
Tallennusfunktio (WIP)
Yleistä hienosäätöä
Paperityöt & raportit


'''
#Importtaukset
from tkinter import *
from tkinter import messagebox
 
# lista, johon tehtävät tallennetaan
tasks_list = []
counter = 1



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
 
    def lisaaTehtava(inputError, enterTaskField, tekstiAlue, clear_taskField):
        
        global counter
        value = inputError() 
        if value == 0 :
            return
        content = enterTaskField.get() + "\n"
 
    # tallentaa tehtävän listaan
        tasks_list.append(content) 
    # lisää tehtävän sovelluksen tekstikenttään
        tekstiAlue.insert('end -1 chars', "[ " + str(counter) + " ] " + content)
        counter += 1
        clear_taskField()

def delete(taskNumberField, clear_taskNumberField, tekstiAlue, *args) :     
    global counter    
    if len(tasks_list) == 0 :      # Jos tyhjä
        messagebox.showerror("404 tehtävää ei löytynyt")
        return
 
        # Mikä tehtävä poistetaan
        number = taskNumberField.get(1.0, END)
 
        # Jos tyhjä
        if number == "\n" :
            messagebox.showerror("input error")
            return    
        else :
            task_no = int(number)
        clear_taskNumberField()
     
        # poistaa pyydetyn tehtävän
        tasks_list.pop(task_no - 1)
        counter -= 1
        tekstiAlue.delete(1.0, END)
 
        # kirjoittaa tehtävälistan uudelleen kun tehtävä on poistettu
        for i in range(len(tasks_list)) :
            tekstiAlue.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i])

    

class SaveAndLoad(): #Work in progress. Tähän tulee lataus/tallennus systeemit
    pass
     
class guiRun(): #GUI- luokka. Sisältää tkinter säädöt ja muut mahdolliset Ui elementit #TODO: Siirrä omaan tiedstoonsa
    gui = Tk()
    gui.configure(background = "light gray")
    gui.title("ToDo")
    gui.geometry("250x300")
    enterTask = Label(gui, text = "Lisää tehtävä", bg = "light gray")
    enterTaskField = Entry(gui)
    Submit = Button(gui, text = "Submit", fg = "Black", bg = "gray", command = main.lisaaTehtava)
    tekstiAlue = Text(gui, height = 5, width = 25, font = "lucida 13") #tekstikenttä sisällön kirjoittamiseen
    taskNumber = Label(gui, text = "Poistettavan tehtävän numero:", bg = "light gray")                        
    taskNumberField = Text(gui, height = 1, width = 2, font = "lucida 13")
    delete = Button(gui, text = "Poista", fg = "Black", bg = "gray", command = delete)
    Exit = Button(gui, text = "Exit", fg = "Black", bg = "gray", command = exit)
 
    # ruudukon parametrit
    enterTask.grid(row = 0, column = 2)             
    enterTaskField.grid(row = 1, column = 2, ipadx = 50)                      
    Submit.grid(row = 2, column = 2)
    tekstiAlue.grid(row = 3, column = 2, padx = 10, sticky = W)                 
    taskNumber.grid(row = 4, column = 2, pady = 5)                      
    taskNumberField.grid(row = 5, column = 2, padx = 90)             
    delete.grid(row = 6, column = 2, pady = 5)
                        
    Exit.grid(row = 7, column = 2)
 
# käynnistää sovelluksen
if __name__ == "__main__" :
        guiRun.gui.mainloop()