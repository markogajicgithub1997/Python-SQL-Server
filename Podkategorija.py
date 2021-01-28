from tkinter import *
from tkinter import messagebox
import pyodbc
from Konekcija import konn

conn = konn

class PodkategorijaClass():
    @staticmethod
    def Podkategorije():
        global Podkategorije
        global podkategorijaid_entry
        global podkategorija_entry
        global Variable1
        global podkategorijaizmena_entry
        Podkategorije=Toplevel()
        Podkategorije.title('Podkategorije')
        Podkategorije.geometry('600x600')

        ##Kategorija#
        cursor=conn.cursor()
        cursor.execute('Select naziv from [box].[dbo].[kategorija] ')
        print_cursor=[]
        for row in cursor:
            print_cursor  += (row) 
        Variable1=StringVar(Podkategorije)
        Variable1.set('Izaberite')
        listboxPK=OptionMenu(Podkategorije,Variable1,*print_cursor)
        listboxPK.grid(row=0,column=1)

        kategorijaPK_label = Label(Podkategorije,text='Izaberite kategoriju')
        kategorijaPK_label.grid(row=0,column=0)

        podkategorijaid_label=Label(Podkategorije,text='Unesite ID podkategorije :')
        podkategorijaid_label.grid(row=1,column=0)

        podkategorijaid_entry = Entry(Podkategorije,width=30)
        podkategorijaid_entry.grid(row=1,column=1,padx=20)

        podkategorija_label = Label(Podkategorije,text='Unesite naziv podkategorije :')
        podkategorija_label.grid(row=2,column=0)

        podkategorija_entry = Entry(Podkategorije,width=30)
        podkategorija_entry.grid(row=2,column=1,padx=20)

        podkategorijainsert_button = Button(Podkategorije,text='Unesite',
            command=PodkategorijaClass.insertPodkategoriju)
        podkategorijainsert_button.grid(row=3,column=1)

        podkategorijaizmena_label = Label(Podkategorije,text='Izaberite podkategoriju za izmenu :')
        podkategorijaizmena_label.grid(row=4,column=0)
        global podkategorijaizmena_entry
        podkategorijaizmena_entry = Entry(Podkategorije,width=30)
        podkategorijaizmena_entry.grid(row=4,column=1,padx=20)

        podkategorijaizmena_button = Button(Podkategorije,text='Izaberite',command=PodkategorijaClass.editPodkategoriju)
        podkategorijaizmena_button.grid(row=5,column=1)

        svepodkategorije_button=Button(Podkategorije,text='Prikazi sve podkategorije',command=PodkategorijaClass.selectsvepodkategorije)
        svepodkategorije_button.grid(row=6,column=1)

        conn.commit()

    @staticmethod
    def insertPodkategoriju():
        if podkategorija_entry.get()=='':
            podkategorijaNaziv=tuple(podkategorija_entry.get())
        else:
            podkategorijaNaziv=podkategorija_entry.get()

        try:
            cursor=conn.cursor()
            g=Variable1.get()
            cursor.execute('SELECT * FROM [BOX].[dbo].[Kategorija] WHERE Naziv=?',g)
            for row in cursor:
                kategorijaidd=row[0]

            cursor2=conn.cursor()
            cursor2.execute('INSERT INTO [BOX].[dbo].[Podkategorija] ([KategorijaID],[ID],[Naziv]) VALUES (?,?,?)', 
                (kategorijaidd,podkategorijaid_entry.get(),podkategorijaNaziv))
            conn.commit()
        except Exception as e:
            messagebox.showerror(title='Neuspesno',message='Popunite sve polja ispravno'+"\n"+"\n"+str(e))
        else:
            messagebox.showinfo(title='Uspesno',message='Uspesno ste uneli podkategoriju')
            podkategorijaid_entry.delete(0,END)
            podkategorija_entry.delete(0,END)


    @staticmethod
    def selectsvepodkategorije():
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM [BOX].[dbo].[Podkategorija]')
        print_cursor=''
        for row in cursor:
            print_cursor += str(row[2]) + " " + str(row[3]) + "\n"
        svepodkategorije_label=Label(Podkategorije,text=print_cursor)
        svepodkategorije_label.grid(row=7,column=1)

    @staticmethod
    def editPodkategoriju():
        global editPodkategoriju
        global editPodkategoriju_entry
        global editKategoriju_entry
        editPodkategoriju=Tk()
        editPodkategoriju.title('Izmenite izabranu podkategoriju')
        editPodkategoriju.geometry('600x600')

        cursor=conn.cursor()
        c=podkategorijaizmena_entry.get()
        cc = "'{}'".format(c)
        print_cursor=''
        cursor.execute("SELECT * FROM [BOX].[dbo].[Podkategorija] WHERE Naziv="+ cc  )  
        for row in cursor:
            print_cursor=row[1]

        if not print_cursor:
            nista=Label(editPodkategoriju,text='Nije pronadjena ni jedna podkategorija')
            nista.grid(row=0,column=0) 
        
        else:
            editPodkategoriju_label=Label(editPodkategoriju,text='Izmenite naziv izabrane podkategorije:')
            editPodkategoriju_label.grid(row=0,column=1)
            ##
            editKategoriju_label=Label(editPodkategoriju,text='Naziv kategorije za izanranu podkategoriu:')
            editKategoriju_label.grid(row=1,column=0)

            editKategoriju_entry=Entry(editPodkategoriju,width=30)
            editKategoriju_entry.grid(row=1,column=1)
            ##
            editPodkategoriju_label=Label(editPodkategoriju,text='Naziv podkategorije:')
            editPodkategoriju_label.grid(row=2,column=0)

            editPodkategoriju_entry=Entry(editPodkategoriju,width=30)
            editPodkategoriju_entry.grid(row=2,column=1)
            ##
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM [BOX].[dbo].[Podkategorija] WHERE Naziv=?",  podkategorijaizmena_entry.get() )  
            for row in cursor:
                editPodkategoriju_entry.insert(0,row[2])
                editKategoriju_entry.insert(0,row[3])

            editPodkategoriju_button=Button(editPodkategoriju,text='Izmeni',
                command=lambda:[PodkategorijaClass.kategorijaUpdate(),PodkategorijaClass.updatePodkategoriju()])
            editPodkategoriju_button.grid(row=3,column=1)

            deletePodkategoriju_button=Button(editPodkategoriju,text='Izbrisi',command=PodkategorijaClass.deletePodkategoriju)
            deletePodkategoriju_button.grid(row=4,column=1)
    @staticmethod
    def kategorijaUpdate():
        cursor1=conn.cursor()
        sql1='SELECT KategorijaID From Podkategorija WHERE Naziv=?'
        val1=podkategorijaizmena_entry.get()
        cursor1.execute(sql1,val1)
        global kategorijaid
        kategorijaid=0
        for row in cursor1:
            kategorijaid=row[0]

        cursor=conn.cursor()
        sql='SELECT Naziv from Kategorija WHERE ID=?'
        val=(kategorijaid)
        cursor.execute(sql,val)
        global kategorijanaziv
        kategorijanaziv=''
        for row in cursor:
            kategorijanaziv=str(row[0])
        if (kategorijanaziv != str(editKategoriju_entry.get())):
            cursor2=conn.cursor()
            sql2='UPDATE Podkategorija SET NazivKategorije=? WHERE Naziv=?'
            val2=(editKategoriju_entry.get(),kategorijanaziv)
            try: 
                cursor2.execute(sql2,val2)
                conn.commit()
            except Exception as e:
                messagebox.showerror(title='Neuspesno',message=str(e))
            editPodkategoriju.destroy()

    @staticmethod
    def updatePodkategoriju():
        try:
            cursor=conn.cursor()
            vals=(editPodkategoriju_entry.get(), podkategorijaizmena_entry.get())
            sql='UPDATE [BOX].[dbo].[Podkategorija] SET Naziv=? WHERE Naziv=?'
            cursor.execute(sql,vals )
            conn.commit()
        except Exception as e:
            messagebox.showerror(title='Neuspesno',message='Popunite sve polja ispravno'+"\n"+"\n"+str(e))
        else:
            messagebox.showinfo(title='Uspesno',message='Uspesno ste izmenili naziv podkategorije')
            editPodkategoriju.destroy()

    @staticmethod
    def deletePodkategoriju():
        try:
            cursor=conn.cursor()
            w=podkategorijaizmena_entry.get()
            cursor.execute('DELETE FROM [BOX].[dbo].[Podkategorija] WHERE Naziv=?',w)
            conn.commit()
        except Exception as e:
            messagebox.showerror(title='Neuspesno',message=str(e))
        else:
            messagebox.showinfo(title='Uspesno',message='Uspesno ste obrisali podkategoriju')
            editPodkategoriju.destroy()