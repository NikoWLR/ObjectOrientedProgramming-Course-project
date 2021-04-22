'''
#TODO: 
Jako luokkiin (done ainakin osittain)
Kommentit kuntoon (done)
Tallennusfunktio (erittäin WIP)
Yleistä hienosäätöä
Paperityöt & raportit (Working on it)
'''

#Importtaukset
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tiedostohandler import *
 
# lista, johon tehtävät tallennetaan
tasks_list = [] #
counter = 1


class main: #Sovelluksen pääluokka. Sisältää päälogiikan

    def __init__(self, enterTaskField, taskNumberField, inputError, tekstiAlue):
        self.enterTaskField = enterTaskField
        self.taskNumberField = taskNumberField
        self.inputError = inputError
        self.tekstiAlue = tekstiAlue
        self.tasks_list = []
        self.counter = counter
        print ("toimii tähän asti")

    def inputError(self, enterTaskField) :     # jos input error -> ilmoita
        if enterTaskField.get() == "" :
            messagebox.showerror("Input Error")   
            return 0
        return 1
 
    def clear_taskNumberField(self, taskNumberField) : # numerokentän tyhjennys
        taskNumberField.delete(0.0, END)
 
    def clear_taskField(self, enterTaskField) :# tehtäväkentän tyhjennys
        enterTaskField.delete(0, END)
 
    def lisaaTehtava(self): # tehtävän lisääminen #? ongelma toivottavasti täällä
        
        global counter
        value = self.inputError() 
        if value == 0 :
            return
        content = self.enterTaskField.get() + "\n"
 
    # tallentaa tehtävän listaan
        tasks_list.append(content) 
    # lisää tehtävän sovelluksen tekstikenttään
        self.tekstiAlue.insert('end -1 chars', "[ " + str(counter) + " ] " + content)
        counter += 1
        self.clear_taskField()

    def delete(self, taskNumberField, clear_taskNumberField, tekstiAlue):    # funktio tehtävien poistamiseen
        global counter    
        if len(tasks_list) == 0 :      # Jos tyhjä
            messagebox.showerror("404 tehtävää ei löytynyt")
            return
    
        # Mikä tehtävä poistetaan
        number = self.taskNumberField().get(1.0, END)
    
        # Jos tyhjä
        if number == "\n" :
            messagebox.showerror("input error")
            return    
        else :
            task_no = int(number)
        self.clear_taskNumberField()

        # poistaa pyydetyn tehtävän
        tasks_list.pop(task_no - 1)
        counter -= 1
        self.tekstiAlue().delete(1.0, END)
    
         # kirjoittaa tehtävälistan uudelleen kun tehtävä on poistettu
        for i in range(len(tasks_list)) :
            self.tekstiAlue().insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i])

    

class SaveAndLoad(): #WIP. Tähän tulee lataus/tallennus systeemit. Tod.näk kopioitu häpeilemättä jostain labratyöstä #TODO: Siirrä omaan tiedostoon
    def __init__(self):
        try:
            self.edellinen = TiedostoHandler().lue('rivi.dat').split(',')
            if len(self.edellinen) >= 3: #tyyppi, määrä ja ainakin yhden nopan silmäluku
                self.noppa.typpi = int(self.edellinen[0])
                self.noppa.maara = int(self.edellinen[1])
                self.entry.insert(0, str(self.noppa.maara)) #jatketaan edellisestä
                s =''
                for i, item in enumerate(self.edellinen[2:]):
                    if item: #ei tyhjiä
                       s += (str(item) + ', ') if i < len(self.edellinen[2:]) -1 else str(item)
                tk.messagebox.showinfo('Edellinen heitto',f'Noppa tyyppi {self.noppa.typpi}: {s}')
        except:
             tk.messagebox.showinfo('Edellistä heittoa ei voitu hakea', 'Tee uusi heitto') 
        
        self.protocol("WM_DELETE_WINDOW", self.close)
        pass

    def close(self):
        s =''
        for i, item in enumerate(self.edellinen):
            if item: #ei tyhjiä
                s += (str(item) + ', ') if i < len(self.edellinen) -1 else str(item)
        TiedostoHandler().kirjoita('rivi.dat', s)
        self.destroy()


     
class gui: #GUI- luokka. Sisältää tkinter säädöt ja muut mahdolliset Ui elementit #TODO: Siirrä omaan tiedstoonsa

    def __init__(self):
        self.gui = gui
        self.tekstiAlue = main.tekstiAlue
        self.inputError = main.inputError
        self.delete = main.delete

    gui = Tk()
    gui.configure(background = "light gray")
    gui.title("ToDo")
    gui.geometry("250x300")
    enterTask = Label(gui, text = "Lisää tehtävä", bg = "light gray")
    enterTaskField = Entry(gui)
    Submit = Button(gui, text = "Lisää", fg = "Black", bg = "gray", command = main.lisaaTehtava) # submit-nappi
    tekstiAlue = Text(gui, height = 5, width = 25, font = "lucida 13") #tekstikenttä sisällön kirjoittamiseen
    taskNumber = Label(gui, text = "Poistettavan tehtävän numero:", bg = "light gray")                        
    taskNumberField = Text(gui, height = 1, width = 2, font = "lucida 13")
    main.delete = Button(gui, text = "Poista", fg = "Black", bg = "gray", command = main.delete)
    Exit = Button(gui, text = "Exit", fg = "Black", bg = "gray", command = exit)
 
    # ruudukon parametrit
    enterTask.grid(row = 0, column = 2)             
    enterTaskField.grid(row = 1, column = 2, ipadx = 50)                      
    Submit.grid(row = 2, column = 2)
    tekstiAlue.grid(row = 3, column = 2, padx = 10, sticky = W)                 
    taskNumber.grid(row = 4, column = 2, pady = 5)                      
    taskNumberField.grid(row = 5, column = 2, padx = 90)             
    main.delete.grid(row = 6, column = 2, pady = 5)
                        
    Exit.grid(row = 7, column = 2)
 