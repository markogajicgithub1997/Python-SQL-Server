from tkinter import *

import pyodbc

from TrojniUgovo import TrojniUgovorClass
from Poslovi import PosloviClass
from Studenti import StudentiClass
from Poslodavac import PoslodavacClass
from Faktura import FakturaClass
from PristupniFormular import PristupniFormularClass

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-RIM8T9PN;"
    "Database=BOX;"
    "Trusted_Connection=yes;"
)

main = Tk()
main.title('BOX')
main.geometry('600x600')

main_buttonStudenti = Button(main,text='Studenti',command=StudentiClass.Studenti)
main_buttonStudenti.grid(row=0,column=0)

main_buttonPoslodavci=Button(main,text='Poslodavci',command=PoslodavacClass.Poslodavac)
main_buttonPoslodavci.grid(row=0,column=1)

main_buttonPristupniFormular=Button(main,text='Pristupni formular',command=PristupniFormularClass.PristupniFormular)
main_buttonPristupniFormular.grid(row=0,column=2)

main_buttonTU = Button(main,text='Trojni ugovor',command=TrojniUgovorClass.TrojniUgovor)
main_buttonTU.grid(row=0,column=4)

main_buttonPoslovi=Button(main,text='Poslovi',command=PosloviClass.Poslovi)
main_buttonPoslovi.grid(row=0,column=3)

main_buttonFaktura=Button(main,text='Fakture',command=FakturaClass.Faktura)
main_buttonFaktura.grid(row=0,column=5)



main.mainloop()

conn.close()
