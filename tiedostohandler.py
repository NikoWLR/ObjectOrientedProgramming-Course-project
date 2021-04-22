"""
ReadWrite to a text file
"""
class TiedostoHandler:
    def  kirjoita(self, tiedostonimi, txt):
        f = None
        try :                
            f = open(tiedostonimi, 'w') 
            f.write(txt) 
        except IOError as error :
            print(f'Error: {error}')
        finally :
            if f != None :
                f.close()
                
    def lue(self, tiedostonimi): 
        txt = ""
        f = None
        try :
            f =  open(tiedostonimi, 'r')
            txt = f.read()                                     
            f.close()
        except (FileNotFoundError, IOError) as error :
            print(f'Error: {error}')
        finally :
            if f != None :
                f.close()  
        return txt