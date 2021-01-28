from tkinter import *
from tkinter import messagebox
import pyodbc

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-RIM8T9PN;"
    "Database=BOX;"
    "Trusted_Connection=yes;"
)

class KategorijaClass():
    @staticmethod
    def Kategorije():
        global Kategorije
        global kategorijaizmena_entry
        global kategorijaid_entry
        global kategorija_entry
        Kategorije=Toplevel()
        Kategorije.title('Kategorije')
        Kategorije.geometry('600x600')

        kategorijaid_label=Label(Kategorije,text='Unesite ID kategorije :')
        kategorijaid_label.grid(row=0,column=0)

        kategorijaid_entry = Entry(Kategorije,width=30)
        kategorijaid_entry.grid(row=0,column=1,padx=20)

        kategorija_label = Label(Kategorije,text='Unesite naziv kategorije :')
        kategorija_label.grid(row=1,column=0)

        kategorija_entry = Entry(Kategorije,width=30)
        kategorija_entry.grid(row=1,column=1,padx=20)

        kategorijainsert_button = Button(Kategorije,text='Unesite',command=KategorijaClass.insertKategoriju)
        kategorijainsert_button.grid(row=2,column=1)

        kategorijaizmena_label = Label(Kategorije,text='Izaberite kategoriju za izmenu :')
        kategorijaizmena_label.grid(row=3,column=0)

        kategorijaizmena_entry = Entry(Kategorije,width=30)
        kategorijaizmena_entry.grid(row=3,column=1,padx=20)

        kategorijaizmena_button = Button(Kategorije,text='Izaberite',command=KategorijaClass.editKategoriju)
        kategorijaizmena_button.grid(row=4,column=1)

        svekategorije_button=Button(Kategorije,text='Prikazi sve kategorije',command=KategorijaClass.selectsvekategorije)
        svekategorije_button.grid(row=5,column=1)

    @staticmethod
    def selectsvekategorije():
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM [BOX].[dbo].[Kategorija]')
        print_cursor=''
        for row in cursor:
            print_cursor += str(row[1]) + "\n"
        svekategorije_label=Label(Kategorije,text=print_cursor)
        svekategorije_label.grid(row=6,column=1)

    @staticmethod
    def insertKategoriju():
        if kategorija_entry.get()=='':
            kategorijaNaziv=tuple(kategorija_entry.get())
        else :
            kategorijaNaziv=kategorija_entry.get()

        try:
            cursor=conn.cursor()
            cursor.execute('INSERT INTO [BOX].[dbo].[Kategorija] ([ID],[Naziv]) VALUES (?,?)', (kategorijaid_entry.get(),kategorijaNaziv))
            conn.commit()
        except Exception as e:
            messagebox.showerror(title='Neuspesno',message='Popunite sve polja ispravno'+"\n"+"\n"+str(e))
        else:
            messagebox.showinfo(title='Uspesno',message='Uspesno ste uneli kategoriju')
            kategorijaid_entry.delete(0,END)
            kategorija_entry.delete(0,END)


    @staticmethod
    def editKategoriju():
        global editKategoriju
        global editKategoriju_entry
        editKategoriju=Tk()
        editKategoriju.title('Izmenite izabranu kategoriju')
        editKategoriju.geometry('600x600')

        cursor=conn.cursor()
        s=kategorijaizmena_entry.get()
        ss = "'{}'".format(s)
        print_cursor=''
        cursor.execute("SELECT * FROM [BOX].[dbo].[Kategorija] WHERE Naziv="+ ss  )  
        for row in cursor:
            print_cursor=row[1]

        if not print_cursor:
            nista=Label(editKategoriju,text='Nije pronadjena ni jedna kategorija')
            nista.grid(row=0,column=0)
        else:
            editKategoriju_label=Label(editKategoriju,text='Izmenite naziv izabrane kategorije:')
            editKategoriju_label.grid(row=0,column=0)

            editKategoriju_entry=Entry(editKategoriju,width=30)
            editKategoriju_entry.grid(row=1,column=0)
            
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM [BOX].[dbo].[Kategorija] WHERE Naziv=?",kategorijaizmena_entry.get())
            for row in cursor:
                editKategoriju_entry.insert(0,row[1])

            editKategoriju_button=Button(editKategoriju,text='Izmeni',command=KategorijaClass.updateKategoriju)
            editKategoriju_button.grid(row=2,column=0)

            deleteKategoriju_button=Button(editKategoriju,text='Izbrisi',command=KategorijaClass.deleteKategoriju)
            deleteKategoriju_button.grid(row=3,column=0)

    @staticmethod
    def updateKategoriju():
        try:
            cursor=conn.cursor()
            s=kategorijaizmena_entry.get()
            ss = "'{}'".format(s)
            cursor.execute('UPDATE [BOX].[dbo].[Kategorija] SET Naziv=? WHERE Naziv='+ss, editKategoriju_entry.get() )
            conn.commit()
        except Exception as e:
            messagebox.showerror(title='Neuspesno',message='Popunite sve polja ispravno'+"\n"+"\n"+str(e))
        else: 
            messagebox.showinfo(title='Uspesno',message='Uspesno ste izmenili naziv kategorije')
            editKategoriju.destroy()

    @staticmethod
    def deleteKategoriju():
        try:
            cursor=conn.cursor()
            s=kategorijaizmena_entry.get()
            ss = "'{}'".format(s)
            cursor.execute('DELETE FROM [BOX].[dbo].[Kategorija] WHERE Naziv='+ss)
            conn.commit()
        except Exception as e:
            messagebox.showerror(title='Neuspesno',message=str(e))
        else:
            messagebox.showinfo(title='Uspesno',message='Uspesno ste izbrisali kategoriju')
            editKategoriju.destroy()