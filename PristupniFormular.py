from tkinter import *
from tkinter import messagebox
import pyodbc

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-RIM8T9PN;"
    "Database=BOX;"
    "Trusted_Connection=yes;"
)

class PristupniFormularClass():
    def PristupniFormular():
        PristupniFormular=Toplevel()
        PristupniFormular.title('Pristupni formular')
        PristupniFormular.geometry('600x600')
        ####
        def sviPF():
            Sve=Toplevel()
            Sve.title('Svi pristupni formulari')
            Sve.geometry('600x600')

            cursor=conn.cursor()
            sql='SELECT * FROM PristupniFormular'
            cursor.execute(sql)
            studentid=''
            idformulara=''
            datumi=''
            zadrugaid=''
            for row in cursor:
                studentid += str(row[0]) +"\n"
                idformulara += str(row[1]) + "\n"
                datumi += str(row[2]) + "\n"
                zadrugaid +=  str(row[3]) + "\n"
                
            sveid=Label(Sve,text='Student ID')
            sveid.grid(row=0,column=0)

            sveidR=Label(Sve,text=studentid)
            sveidR.grid(row=1,column=0)
            ###
            svefid=Label(Sve,text='ID Formulara')
            svefid.grid(row=0,column=1)

            svefidR=Label(Sve,text=idformulara)
            svefidR.grid(row=1,column=1)
            ###
            svedatumi=Label(Sve,text='Datumi')
            svedatumi.grid(row=0,column=2)

            svedatumiR=Label(Sve,text=datumi)
            svedatumiR.grid(row=1,column=2)
            ###
            svezadruga=Label(Sve,text='Zadruga')
            svezadruga.grid(row=0,column=3)

            svezadrugaR=Label(Sve,text=zadrugaid)
            svezadrugaR.grid(row=1,column=3)
        ####
        def insert():
            try:
                cursor=conn.cursor()
                sql='SELECT ID FROM Student WHERE ID=?'
                val=varSt.get().split(' ')
                studentID=val[0]
                cursor.execute(sql,studentID)
                for row in cursor:
                    StudentID=row[0]

                if idPF_entry.get()=='':
                    idPrForm=tuple(idPF_entry.get())
                    messagebox.showerror(title='Neuspesno',message='Unesite ID')
                else:
                    idPrForm=idPF_entry.get()

                if datumPF_entry.get()=='':
                    datumPrForm=tuple(datumPF_entry.get())
                    messagebox.showerror(title='Neuspesno',message='Unesite datum')
                else:
                    datumPrForm=datumPF_entry.get()

                cursor2=conn.cursor()
                sql2='INSERT INTO PristupniFormular VALUES (?,?,?,?)'
                val2=(StudentID,idPrForm,datumPrForm,1)
                cursor2.execute(sql2,val2)
                conn.commit()
            except Exception as e:
                messagebox.showerror(title='Neuspesno',message='Popunite sve polja ispravno'+"\n"+"\n"+str(e))
            else:
                messagebox.showinfo(title='Uspesno',message='Uspesno ste uneli pristupni formular')
                idPF_entry.delete(0,END)
                datumPF_entry.delete(0,END)

        def select():
            Select=Toplevel()
            Select.title('Izabrani pristupni formular')
            Select.geometry('600x600')

            cursor=conn.cursor()
            sql='SELECT ID,Ime,Prezime FROM Student WHERE ID=?'
            val=selectPF_entry.get()
            try:
                cursor.execute(sql,val)
            except Exception:
                neispravno=Label(Select,text='Neispravno uneti podaci')
                neispravno.grid(row=0,column=0)
            else:
                pass
            
            studentt=''
            for row in cursor:
                studentt= str(row[0]) + " " + str(row[1]) + " " + str(row[2])

            cursor2=conn.cursor()
            sql2='SELECT ID,DatumPopunjavanja FROM PristupniFormular WHERE StudentID=? and DatumPopunjavanja=?'
            val2=(selectPF_entry.get(),selectDatum_entry.get())
            try:
                cursor2.execute(sql2,val2)
            except Exception:
                neispravno=Label(Select,text='Neispravno uneti podaci')
                neispravno.grid(row=0,column=0)
            else:
                pass

            pfid=''
            pfdatum=''
            for row in cursor2:
                pfid=row[0]
                pfdatum=row[1]

            if not pfid:
                nista=Label(Select,text='Nije pronadjen ni jedan pristpuni formular')
                nista.grid(row=0,column=0)
            else:
                ###
                zadrugaS=Label(Select,text='Zadruga')
                zadrugaS.grid(row=0,column=0)

                zadrugaS_entry=Label(Select,text='BOX')
                zadrugaS_entry.grid(row=0,column=1)
                ###
                studentS=Label(Select,text='Student')
                studentS.grid(row=1,column=0)

                studentS_entry=Label(Select,text=studentt)
                studentS_entry.grid(row=1,column=1)
                ###
                idS=Label(Select,text='ID pristupnog formulara')
                idS.grid(row=2,column=0)

                idS_entry=Entry(Select,width=30)
                idS_entry.grid(row=2,column=1)
                idS_entry.insert(0,pfid)
                ###
                datumS=Label(Select,text='Datum pristupnog formulara')
                datumS.grid(row=3,column=0)

                datumS_entry=Entry(Select,width=30)
                datumS_entry.grid(row=3,column=1)
                datumS_entry.insert(0,pfdatum)
                ###
                def update():
                    try:
                        if idS_entry.get()=='':
                            idSel=tuple(idS_entry.get())
                            messagebox.showerror(title='Neuspesno',message='Unesite id')
                        else:
                            idSel=idS_entry.get()

                        if datumS_entry.get()=='':
                            idDat=tuple(datumS_entry.get())
                            messagebox.showerror(title='Neuspesno',message='Unesite datum')
                        else:
                            idDat=datumS_entry.get()


                        cursor=conn.cursor()
                        sql='UPDATE PristupniFormular SET ID=?,DatumPopunjavanja=? WHERE StudentID=? and DatumPopunjavanja=?'
                        val=(idSel,idDat,selectPF_entry.get(),selectDatum_entry.get())
                        cursor.execute(sql,val)
                        conn.commit()
                    except Exception:
                        messagebox.showerror(title='Neuspesno',message='Popunite sve polja ispravno'+"\n"+"\n"+str(e))
                    else:
                        messagebox.showinfo(title='Uspesno',message='Uspesno ste izmenili pristupni formular')
                        Select.destroy()

                def delete():
                    try:
                        cursor=conn.cursor()
                        sql='DELETE PristupniFormular WHERE StudentID=? and DatumPopunjavanja=?'
                        val=(selectPF_entry.get(),selectDatum_entry.get())
                        cursor.execute(sql,val)
                        conn.commit()
                    except Exception as e:
                        messagebox.showerror(title='Neuspesno',message=str(e))
                    else:
                        messagebox.showinfo(title='Uspesno',message='Uspesno ste obrisali pristupni formular')
                        Select.destroy()

                #### 
                updateBtn=Button(Select,text='Izmenite',command=update)
                updateBtn.grid(row=4,column=1)

                deleteBtn=Button(Select,text='Izbrisite',command=delete)
                deleteBtn.grid(row=5,column=1)



        ###
        idPF=Label(PristupniFormular,text='Unesite ID za pristupni formular')
        idPF.grid(row=0,column=0)

        idPF_entry=Entry(PristupniFormular,width=30)
        idPF_entry.grid(row=0,column=1)
        ##
        cursor=conn.cursor()
        sql='SELECT * FROM Student'
        cursor.execute(sql)
        student=''
        student2=[]
        for row in cursor:
            student = (str(row[0]) + " " + str(row[1]) + " " + str(row[2]))
            student2 += [student]
        
        studenti_label=Label(PristupniFormular,text='Izaberite studenta')
        studenti_label.grid(row=1,column=0)    
        global varSt
        varSt=StringVar(PristupniFormular)
        varSt.set('Izaberite')
        global studenti
        studenti=OptionMenu(PristupniFormular,varSt,*student2)
        studenti.grid(row=1,column=1)
        ##
        datumPF=Label(PristupniFormular,text='Unesite datum')
        datumPF.grid(row=2,column=0)

        datumPF_entry=Entry(PristupniFormular,width=30)
        datumPF_entry.grid(row=2,column=1)
        ###
        zadrugaPF=Label(PristupniFormular,text='Zadruga')
        zadrugaPF.grid(row=3,column=0)

        zadrugaPF_entry=Label(PristupniFormular,text='BOX')
        zadrugaPF_entry.grid(row=3,column=1)
        #####
        insertPF=Button(PristupniFormular,text='Unesite',command=insert)
        insertPF.grid(row=4,column=1)
        ####
        selectBy=Label(PristupniFormular,text='Izaberite pristupni formular po Student ID-u i datumu')
        selectBy.grid(row=5,column=1)

        selectPF=Label(PristupniFormular,text='Student ID')
        selectPF.grid(row=6,column=0)

        selectPF_entry=Entry(PristupniFormular,width=30)
        selectPF_entry.grid(row=6,column=1)

        selectDatum=Label(PristupniFormular,text='Datum')
        selectDatum.grid(row=7,column=0)

        selectDatum_entry=Entry(PristupniFormular,width=30)
        selectDatum_entry.grid(row=7,column=1)

        selectPF_btn=Button(PristupniFormular,text='Izaberite',command=select)
        selectPF_btn.grid(row=8,column=1)
        ###
        svePF=Button(PristupniFormular,text='Svi pristupni formulari',command=sviPF)
        svePF.grid(row=9,column=1)


        def statistikaPF():
            Particija=Toplevel()
            Particija.title('Statistika')
            Particija.geometry('600x600')

            cursor=conn.cursor()
            sql='select partition_id,partition_number,Rows FROM sys.partitions WHERE OBJECT_NAME(OBJECT_ID)=?'
            val='PristupniFormular'
            cursor.execute(sql,val)
            particije=''
            iznos=''
            for row in cursor:
                particije += str(row[1]) + "\n"
                iznos += str(row[2]) + "\n"

            ###
            particijaa=Label(Particija,text='Particija')
            particijaa.grid(row=0,column=0)

            particijaR=Label(Particija,text=particije)
            particijaR.grid(row=1,column=0)
            ###
            iznoss=Label(Particija,text='Kolicina')
            iznoss.grid(row=0,column=1)

            iznosR=Label(Particija,text=iznos)
            iznosR.grid(row=1,column=1)
            ###
            jedan=Label(Particija,text='1-Pre 2020')
            jedan.grid(row=2,column=0)

            dva=Label(Particija,text='2-Januar')
            dva.grid(row=3,column=0)

            tri=Label(Particija,text='3-Februar')
            tri.grid(row=4,column=0)

            cetiri=Label(Particija,text='4-Mart')
            cetiri.grid(row=5,column=0)

            pet=Label(Particija,text='5-April')
            pet.grid(row=6,column=0)

            sest=Label(Particija,text='6-Maj')
            sest.grid(row=7,column=0)

            sedam=Label(Particija,text='7-Jun')
            sedam.grid(row=8,column=0)

            osam=Label(Particija,text='8-Jul')
            osam.grid(row=9,column=0)

            devet=Label(Particija,text='9-Avgust')
            devet.grid(row=10,column=0)

            deset=Label(Particija,text='10-Septembar')
            deset.grid(row=11,column=0)

            jedanaest=Label(Particija,text='11-Oktobar')
            jedanaest.grid(row=12,column=0)

            dvanaest=Label(Particija,text='12-Novembar')
            dvanaest.grid(row=13,column=0)

            trinaest=Label(Particija,text='13-Decembar')
            trinaest.grid(row=14,column=0)

            cetrnaest=Label(Particija,text='14-Posle 2020')
            cetrnaest.grid(row=15,column=0)

        ### 
        statistika=Button(PristupniFormular,text='Statistika',command=statistikaPF)
        statistika.grid(row=10,column=1)

