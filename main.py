'''
@author: Niko Wahlroos
Palautuspäivä: 22/04/2021

Olio-ohjelmoinnni loppuprojekti.
ToDo-sovellus, jossa käyttäjä pystyy (ainakin teoriassa) tallentamaan haluamansa tehtävän ja myöhemin tehtävän suoritettuaan poistamaan sen.

'''

#Importtaukset
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tiedostohandler import *
 
# lista, johon tehtävät tallennetaan
tasks_list = [] # Kyseessä lista indeksoinnin automatisoinnin vuoksi
counter = 1 # laskee tehtävien määrän


class main: #Sovelluksen pääluokka. Sisältää päälogiikan

    def __init__(self, enterTaskField, taskNumberField, inputError, tekstiAlue):
        self.enterTaskField = enterTaskField
        self.taskNumberField = taskNumberField
        self.inputError = inputError
        self.tekstiAlue = tekstiAlue
        self.tasks_list = []
        self.counter = counter


    def inputError(self, enterTaskField) :     # jos error -> ilmoita käyttäjälle
        if enterTaskField.get() == "" :
            messagebox.showerror("Input Error")   
            return 0
        return 1
 
    def clear_taskNumberField(self, taskNumberField) : # numerokentän tyhjennys
        taskNumberField.delete(0.0, END)
 
    def clear_taskField(self, enterTaskField) :# tehtäväkentän tyhjennys
        enterTaskField.delete(0, END)
 
    def lisaaTehtava(self): # Uuden tehtävän lisääminen
        
        global counter
        value = self.inputError() 
        if value == 0 :
            return
        content = self.enterTaskField.get() + "\n"
 
    # Tallentaa tehtävän listaan
        tasks_list.append(content) 
    # lisää tehtävän sovelluksen tekstikenttään
        self.tekstiAlue.insert('end -1 chars', "[ " + str(counter) + " ] " + content)
        counter += 1
        self.clear_taskField()

    def delete(self, taskNumberField, clear_taskNumberField, tekstiAlue):    # Tehtävien poistaminen
        global counter    
        if len(tasks_list) == 0 :      # Jos tyhjä
            messagebox.showerror("404 tehtävää ei löytynyt")
            return
    
        # Mikä tehtävä poistetaan?
        number = self.taskNumberField().get(1.0, END)
    
        # Jos tyhjä -> ilmoita käyttäjälle
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

    

class SaveAndLoad(): #WIP. Tähän tulee lataus/tallennus systeemit. Tod.näk kopioitu häpeilemättä jostain labratyöstä #! Aika loppui = 404 class not found
    pass

     
class gui: #GUI- luokka. Sisältää tkinter säädöt ja muut mahdolliset Ui elementit. Käyttäjä avaa vain yhden sovellusikkunan, eli gui-elementtien luokassa sijaitseminen ei erityisemmin haittaa

    def __init__(self):
        self.gui = gui
        self.tekstiAlue = main.tekstiAlue
        self.inputError = main.inputError
        self.delete = main.delete

    #UI:n logiikka (napit yms.)
    gui = Tk()
    gui.configure(background = "light gray") # taustan väri
    gui.title("ToDo") # ikkunan otsikko/nimi
    gui.geometry("250x300") # ikkunan koko
    enterTask = Label(gui, text = "Lisää tehtävä", bg = "light gray") # tekstiä
    enterTaskField = Entry(gui) # tekstikenttä itse tehtävälle
    Submit = Button(gui, text = "Lisää", fg = "Black", bg = "gray", command = main.lisaaTehtava) # submit-nappi
    tekstiAlue = Text(gui, height = 5, width = 25, font = "lucida 13") #tekstikenttä sisällön kirjoittamiseen
    taskNumber = Label(gui, text = "Poistettavan tehtävän numero:", bg = "light gray") # lisää tekstiä                       
    taskNumberField = Text(gui, height = 1, width = 2, font = "lucida 13") # tekstikenttä tehtävän numerolle
    main.delete = Button(gui, text = "Poista", fg = "Black", bg = "gray", command = main.delete) # delete - nappi
    Exit = Button(gui, text = "Exit", fg = "Black", bg = "gray", command = exit) # exit - nappi
 
    # ruudukon parametrit & UI-elementit
    enterTask.grid(row = 0, column = 2)             
    enterTaskField.grid(row = 1, column = 2, ipadx = 50)                      
    Submit.grid(row = 2, column = 2)
    tekstiAlue.grid(row = 3, column = 2, padx = 10, sticky = W)                 
    taskNumber.grid(row = 4, column = 2, pady = 5)                      
    taskNumberField.grid(row = 5, column = 2, padx = 90)             
    main.delete.grid(row = 6, column = 2, pady = 5)
                        
    Exit.grid(row = 7, column = 2)
 