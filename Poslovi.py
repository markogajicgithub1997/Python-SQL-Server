from tkinter import *
import pyodbc
from Kategorija import KategorijaClass
from Podkategorija import PodkategorijaClass
from PosloviPoslovi import PosloviPosloviClass
from Konekcija import konn

conn = konn

class PosloviClass:
    @staticmethod
    def Poslovi():
        Poslovi=Toplevel()
        Poslovi.title('Poslovi')
        Poslovi.geometry('600x600')

        kategorije_button=Button(Poslovi,text='Kategorije',command=KategorijaClass.Kategorije)
        kategorije_button.grid(row=0,column=1)

        podesavanjekategorije_label = Label(Poslovi,text='Podesavanje kategorije')
        podesavanjekategorije_label.grid(row=0,column=0)

        podkategorija_button=Button(Poslovi,text='Podkategorije',command=PodkategorijaClass.Podkategorije)
        podkategorija_button.grid(row=1,column=1)

        podesavanjepodkategorije_label = Label(Poslovi,text='Podesavanje podkategorije')
        podesavanjepodkategorije_label.grid(row=1,column=0)

        poslovi_button=Button(Poslovi,text='Poslovi',command=PosloviPosloviClass.PosloviPoslovi)
        poslovi_button.grid(row=2,column=1)

        podesavanjeposlova_label=Label(Poslovi,text='Podesavanje poslova')
        podesavanjeposlova_label.grid(row=2,column=0)