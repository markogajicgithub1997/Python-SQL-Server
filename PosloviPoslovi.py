from tkinter import *
import pyodbc
import tkinter as tk
from tkinter import messagebox
from Konekcija import konn

conn = konn

class PosloviPosloviClass():
    @staticmethod
    def PosloviPoslovi():
        PosloviPoslovi=Toplevel()
        PosloviPoslovi.title('Poslovi')
        PosloviPoslovi.geometry('600x600')

        ##Podkategorija#
        def Podkategorija(self):
            listboxn.destroy()
            listboxn_label.destroy()
            cursor=conn.cursor()
            global listbox2
            global Variable2
            nk=Variable1.get()
            nkk="'{}'".format(nk)
            cursor.execute('select naziv from Podkategorija where nazivkategorije='+nkk)
            print_cursor=[]
            for row in cursor:
                print_cursor  += (row)
            Variable2=StringVar(PosloviPoslovi)
            Variable2.set(print_cursor[0])
            global listbox2
            listbox2=OptionMenu(PosloviPoslovi,Variable2,*print_cursor)
            listbox2.grid(row=1,column=1)

            podkategorijaizb_label = Label(PosloviPoslovi,text='Izaberite podkategoriju')
            podkategorijaizb_label.grid(row=1,column=0)

        def ifPodkExists():
            try:
                listbox2
            except Exception:
                pass
            else:
                listbox2.destroy()

        ###SVI POSLOVI####
        def sviposlovi():
            cursor=conn.cursor()
            cursor.execute('SELECT * FROM [box].[dbo].[posao]')
            print_cursor=''
            for row in cursor:
                print_cursor += str(row[2]) + " " + str(row[3]) + " " + str(row[6]) + " " + str(row[7]) + "\n"
            sviposlovi_label=Label(PosloviPoslovi,text=print_cursor)
            sviposlovi_label.grid(row=17,column=1)

        ##PRETRAGA PO IMENU#####
        def pretragaime():
            searched=searchposaoentry.get()
            searchedd = "'{}'".format(searched)
            cursor.execute('SELECT * FROM Posao WHERE Naziv='+searchedd)
            print_cursor=''
            for row in cursor:
                print_cursor += str(row[2]) + " " + str(row[3]) + " " + str(row[6]) + " " + str(row[7]) + "\n"
            
            if not print_cursor:
                global searched_label_empty
                searched_label_empty=Label(PosloviPoslovi,text='Nije pronadjen ni jedan posao')
                searched_label_empty.grid(row=16,column=1)
            else:
                global searched_label
                searched_label=Label(PosloviPoslovi,text=print_cursor)
                searched_label.grid(row=16,column=1)
        ###PRETRAGA PO POSLODAVAC ID ####
        def pretraPoslodavacID():
            cursor=conn.cursor()
            sql='SELECT ID From Poslodavac WHERE Naziv=?'
            val=Variable4.get()
            cursor.execute(sql,val)
            for row in cursor:
                posid=row[0]
            cursor2=conn.cursor()
            sql2='SELECT * FROM Posao WHERE PoslodavacID=?'
            val2=posid
            cursor2.execute(sql2,val2)
            print_cursor=''
            for row in cursor2:
                print_cursor += str(row[2]) + " " + str(row[3]) + " " + str(row[6]) + " " + str(row[7]) + "\n"
            if not print_cursor:
                global searchedPid_label_empty
                searchedPid_label_empty=Label(PosloviPoslovi,text='Nije pronadjen ni jedan posao')
                searchedPid_label_empty.grid(row=16,column=1)
            else:
                global searchedPid_label
                searchedPid_label=Label(PosloviPoslovi,text=print_cursor)
                searchedPid_label.grid(row=16,column=1)

        def destroyPretrazeno():
            try:
                searched_label_empty.destroy()
            except Exception:
                pass
            else:
                pass
            try:
                searched_label.destroy()
            except Exception:
                pass
            else:
                pass
            try:
                searchedPid_label.destroy()
            except Exception:
                pass
            else:
                pass
            try:
                searchedPid_label_empty.destroy()
            except Exception:
                pass
            else:
                pass

        ###EDIIIT##############
        def editP():
            global EditPosao
            EditPosao=Toplevel()
            EditPosao.title('Izmena posla')
            EditPosao.geometry('600x600')
            #
            cursor2=conn.cursor()

            try:
                cursor2.execute('SELECT * FROM Posao WHERE ID=? and naziv=?',
                    (selectposaoplata_entryid.get(),selectposaoplata_entrynaziv.get()))
            except Exception:
                neispravno=Label(EditPosao,text='Neispravno unet ID')
                neispravno.grid(row=0,column=0)
            else:
                pass

            
            print_cursorrr=''
            for row in cursor2:
                print_cursorrr = str(row[2]) + str(row[3]) 
            #
            cursor=conn.cursor()
            cursor.execute('SELECT * FROM Posao WHERE ID=? and naziv=?',
                (selectposaoplata_entryid.get(),selectposaoplata_entrynaziv.get()))
            #
            if not print_cursorrr:
                nista=Label(EditPosao,text='Nije pronadjen ni jedan posao')
                nista.grid(row=0,column=0)
            else:
                editPnaziv=Label(EditPosao,text='Izmenite naziv posla')
                editPnaziv.grid(row=0,column=0)
                global editPnaziv_entry
                editPnaziv_entry=Entry(EditPosao,width=30)
                editPnaziv_entry.grid(row=0,column=1)
                ##
                editPopis=Label(EditPosao,text='Izmenite opis posla')
                editPopis.grid(row=1,column=0)
                global editPopis_entry
                editPopis_entry=Entry(EditPosao,width=30)
                editPopis_entry.grid(row=1,column=1)
                ##
                editPplata=Label(EditPosao,text='Iznos plate')
                editPplata.grid(row=3,column=0) 
                global eidtPiznosplata_entry
                eidtPiznosplata_entry=Entry(EditPosao,width=30)
                eidtPiznosplata_entry.grid(row=3,column=1)
                ##
                editPoslodavac=Label(EditPosao,text='Naziv poslodavca')
                editPoslodavac.grid(row=2,column=0)
                global editPoslodavac_entry
                editPoslodavac_entry=Entry(EditPosao,width=30)
                editPoslodavac_entry.grid(row=2,column=1)
                ##
                editPbutton=Button(EditPosao,text='Izmenite posao',command=lambda:[nazivPoslodavcaU(),plataUpdateP(),posaoUpdate()])
                editPbutton.grid(row=4,column=1)

                deletePbutton_button=Button(EditPosao,text='Obrisite posao',command=lambda:[posaoPlateDelete(),posaoDelete()])
                deletePbutton_button.grid(row=5,column=1)

                for row in cursor:
                    editPnaziv_entry.insert(0,row[3])
                    editPopis_entry.insert(0,row[4]) 
                    editPoslodavac_entry.insert(0,row[6]) 
                    if (row[7] in (None,'')):
                        pass
                    else:
                        eidtPiznosplata_entry.insert(0,row[7])
                    
        def plataUpdateP():
            cursor1=conn.cursor()
            sql1='SELECT Plata FROM Posao WHERE ID=? AND Naziv=?'
            vals=(selectposaoplata_entryid.get(), selectposaoplata_entrynaziv.get())
            cursor1.execute(sql1,vals)
            global plata
            plata=''
            for row in cursor1:
                plata=str(row[0])
            if (plata != str(eidtPiznosplata_entry.get())):
                cursor=conn.cursor()
                sql='UPDATE Posao SET Plata=?  WHERE ID=? and Naziv=?'
                izmene=(eidtPiznosplata_entry.get(),
                    selectposaoplata_entryid.get(), selectposaoplata_entrynaziv.get() )
                try : 
                    cursor.execute(sql,izmene)
                    conn.commit()
                except Exception as e:
                    messagebox.showerror(title="Neuspesno",message = str(e))
                EditPosao.destroy()

        def nazivPoslodavcaU():
            cursor=conn.cursor()
            sql='SELECT NazivPoslodavca FROM Posao WHERE ID=? AND Naziv=?'
            vals=(selectposaoplata_entryid.get(), selectposaoplata_entrynaziv.get())
            cursor.execute(sql,vals)
            global nazivposl
            nazivposl=''
            for row in cursor:
                nazivposl=str(row[0])
            if(nazivposl != str(editPoslodavac_entry.get())):
                cursor1=conn.cursor()
                sql1='UPDATE Posao SET NazivPoslodavca=? WHERE ID=? AND Naziv=?'
                izmene1=(editPoslodavac_entry.get(),selectposaoplata_entryid.get(), selectposaoplata_entrynaziv.get())
                try: 
                    cursor1.execute(sql1,izmene1)
                    conn.commit()
                except Exception as e:
                    messagebox.showerror(title='Neuspesno',message=str(e))
                EditPosao.destroy()
                
        def posaoUpdate():
            try:
                cursor=conn.cursor()
                sql='UPDATE Posao SET Naziv=?,OpisPosla=?  WHERE ID=? and Naziv=?'
                izmene=(editPnaziv_entry.get(), editPopis_entry.get(),
                    selectposaoplata_entryid.get(), selectposaoplata_entrynaziv.get() )
                cursor.execute(sql,izmene)
                conn.commit()
            except Exception as e:
                messagebox.showerror(title='Neuspesno',message='Popunite sve polja ispravno'+"\n"+"\n"+str(e))
            else:
                messagebox.showinfo(title='Uspesno',message='Uspesno ste azurirali posao')
                EditPosao.destroy()

        def posaoDelete():
            cursor1=conn.cursor()
            sql1='DELETE Posao WHERE ID=? AND Naziv=?'
            where1=(selectposaoplata_entryid.get(), selectposaoplata_entrynaziv.get())
            cursor1.execute(sql1,where1)
            conn.commit()
            messagebox.showinfo(title="Uspesno",message ='Uspesno ste obrisali posao')
            EditPosao.destroy()

        def posaoPlateDelete():
            cursor2=conn.cursor()
            sql2='SELECT KategorijaID,PodkategorijaID,ID FROM Posao WHERE ID=? and Naziv=?'
            where2=(selectposaoplata_entryid.get(), selectposaoplata_entrynaziv.get())
            cursor2.execute(sql2,where2)
            global posaokid
            global posaopkid
            global posaoid
            posaokid=0
            posaopkid=0
            posaoid=0
            for row in cursor2:
                posaokid=row[0]
                posaopkid=row[1]
                posaoid=row[2]
            cursor3=conn.cursor()
            sql3='DELETE IznosPlate where Kategorijaid=? and Podkategorijaid=? and PosaoID=?'
            vals=(posaokid,posaopkid,posaoid)
            cursor3.execute(sql3,vals)
            conn.commit()

        

        ####PLATA #####
        def plata():
            Plata=Toplevel()
            Plata.title('Plata')
            Plata.geometry('600x600')

            cursor1=conn.cursor()
            sql='SELECT kategorijaid,podkategorijaid,id FROM Posao where  id=? and naziv=?'
            vals=(selectposaoplata_entryid.get(),selectposaoplata_entrynaziv.get())
            cursor1.execute(sql,vals)
            global posaob1
            global posaob2
            global posaob3
            posaob1=0
            posaob2=0
            posaob3=0
            rez=''
            for row in cursor1:
                posaob1=row[0]
                posaob2=row[1]
                posaob3=row[2]
                rez=row[0]+row[1]+row[2]

            if not rez:
                nista=Label(Plata,text='Nije pronadjen ni jedan posao')
                nista.grid(row=0,column=0)

            else:
                cursor2=conn.cursor()
                sql2='SELECT * FROM  IznosPlate where Kategorijaid=? and podkategorijaid=? and posaoid=?'
                vals2=(posaob1,posaob2,posaob3)
                cursor2.execute(sql2,vals2)
                datum=''
                iznos=''
                
                for row in cursor2 :
                    datum += str(row[3]) + "\n"
                    iznos += str(row[4]) + "\n"

                izabraniid=Label(Plata,text='ID izabranog posla:')
                izabraniid.grid(row=1,column=0)
                
                izabraniidp=Label(Plata,text=selectposaoplata_entryid.get())
                izabraniidp.grid(row=1,column=1)
                ###
                izabraninaziv=Label(Plata,text='Naziv izabranog posla:')
                izabraninaziv.grid(row=2,column=0)

                izabraninazivv=Label(Plata,text=selectposaoplata_entrynaziv.get())
                izabraninazivv.grid(row=2,column=1)
                ###
                dosadasnje=Label(Plata,text='Dosadasnje plate:')
                dosadasnje.grid(row=7,column=1)
                ###
                platalabeldatum=Label(Plata,text="Datum:")
                platalabeldatum.grid(row=8,column=0)

                platalabeldatumm=Label(Plata,text=datum)
                platalabeldatumm.grid(row=9,column=0)
                ###
                platalabeliznos=Label(Plata,text="Iznos:")
                platalabeliznos.grid(row=8,column=1)
                
                platalabeliznoss=Label(Plata,text=iznos)
                platalabeliznoss.grid(row=9,column=1)
                ###
                insertplatalabel=Label(Plata,text='Unesite novu platu za izabrani posao:')
                insertplatalabel.grid(row=3,column=1)
                ###
                insertplatadate_label=Label(Plata,text='Datum:')
                insertplatadate_label.grid(row=4,column=0)

                insertplatadate_entry=Entry(Plata,width=30)
                insertplatadate_entry.grid(row=4,column=1)
                ###
                insertplatadate_label=Label(Plata,text='Iznos:')
                insertplatadate_label.grid(row=5,column=0)

                insertplataiznos_entry=Entry(Plata,width=30)
                insertplataiznos_entry.grid(row=5,column=1)

                def insertplata():
                    try:
                        cursor=conn.cursor()
                        cursor.execute('INSERT INTO IznosPlate values (?,?,?,?,?)',
                            (posaob1,posaob2,posaob3,insertplatadate_entry.get(),insertplataiznos_entry.get() ) )
                        Plata.destroy()
                        conn.commit()
                    except Exception as e:
                        messagebox.showerror(title='Neuspesno',message='Popunite sve polja ispravno'+"\n"+"\n"+str(e))
                    else:
                        messagebox.showinfo(title='Uspesno',message='Uspesno ste uneli novu platu za izabrani posao')


                insertnpbutton=Button(Plata,text='Unesite',command=insertplata)
                insertnpbutton.grid(row=6,column=1)

        ###
        
        #
        def insertposao():
            try:
                cursor1=conn.cursor()
                v1=Variable1.get()
                v11="'{}'".format(v1)
                cursor1.execute('SELECT * FROM Kategorija WHERE Naziv='+v11)
                for row in cursor1:
                    KID=row[0]
                cursor2=conn.cursor()
                v2=Variable2.get()
                v22="'{}'".format(v2)
                cursor2.execute('SELECT * FROM Podkategorija WHERE Naziv='+v22)
                for row in cursor2:
                    PID=row[1]
                cursor3=conn.cursor()
                v3=Variable3.get()
                v33="'{}'".format(v3)
                cursor3.execute('SELECT * FROM Poslodavac WHERE Naziv='+v33)
                for row in cursor3:
                    PSID=row[0]

                if posao_entry.get()=='' :
                    nazivPosla=tuple(posao_entry.get())
                    messagebox.showerror(title='Neispravno ime',message='Unesite ime')
                else:
                    nazivPosla=posao_entry.get()

                cursor4=conn.cursor()
                sql1='INSERT INTO Posao (KategorijaID,PodkategorijaID,ID,Naziv,OpisPosla,PoslodavacID) VALUES (?,?,?,?,?,?)'
                v4=posaoiddd_entry.get()
                vals=(KID,PID,v4,nazivPosla,opisposla_entry.get(),PSID)
                cursor4.execute(sql1,vals ) 
                conn.commit()    
            except Exception as e:
                messagebox.showerror(title='Neuspesno',message='Popunite sve polja ispravno'+"\n"+"\n"+str(e))
            else:
                messagebox.showinfo(title='Uspesno',message='Uspesno ste uneli posao')       

                posaoiddd_entry.delete(0,END)
                posao_entry.delete(0,END)
                opisposla_entry.delete(0,END)

        ####      
        ####Podkategorija pre biranja ####
        var=StringVar(PosloviPoslovi)
        var.set('Izaberite prvo kategoriju')
        options=''
        listboxn=OptionMenu(PosloviPoslovi,var,'',*options)
        listboxn.grid(row=1,column=1)
        listboxn.configure(state='disabled')

        listboxn_label=Label(PosloviPoslovi,text='Izaberite podkategoriju')
        listboxn_label.grid(row=1,column=0)

        ##Kategorija#
        cursor=conn.cursor()
        global Variable1
        global print_cursorNK
        global listbox1
        cursor.execute('Select naziv from [box].[dbo].[kategorija] ')
        print_cursorNK=[]
        for row in cursor:
            print_cursorNK  += (row) 
        Variable1=StringVar(PosloviPoslovi)
        Variable1.set('Izaberite')
        listbox1=OptionMenu(PosloviPoslovi,Variable1,*print_cursorNK,command=lambda self='':[ifPodkExists(),Podkategorija(self)])
        listbox1.grid(row=0,column=1)
        
        kategorijaizb_label = Label(PosloviPoslovi,text='Izaberite kategoriju')
        kategorijaizb_label.grid(row=0,column=0)

        ###Poslodavac###
        cursor=conn.cursor()
        global Variable3
        cursor.execute('Select naziv from [box].[dbo].[poslodavac]')
        print_cursor=[]
        for row in cursor:
            print_cursor += (row)
        Variable3=StringVar(PosloviPoslovi)
        Variable3.set('Izaberite')
        listbox3=OptionMenu(PosloviPoslovi,Variable3,*print_cursor)
        listbox3.grid(row=2,column=1)

        poslodavacizb_label=Label(PosloviPoslovi,text='Izaberite poslodavca')
        poslodavacizb_label.grid(row=2,column=0)
        ###
        posaoidd_label=Label(PosloviPoslovi,text='Unesite id posla')
        posaoidd_label.grid(row=3,column=0)
        global posaoiddd_entry
        posaoiddd_entry=Entry(PosloviPoslovi,width=30)
        posaoiddd_entry.grid(row=3,column=1)
        ###
        posao_label = Label(PosloviPoslovi,text='Unesite naziv posla')
        posao_label.grid(row=4,column=0)
        global posao_entry
        posao_entry = Entry(PosloviPoslovi,width=30)
        posao_entry.grid(row=4,column=1,padx=20)
        ##
        opisposla_label = Label(PosloviPoslovi,text='Unesite opis posla')
        opisposla_label.grid(row=5,column=0)
        global opisposla_entry
        opisposla_entry=Entry(PosloviPoslovi,width=30)
        opisposla_entry.grid(row=5,column=1,padx=20)
        ##
        insertposao_button=Button(PosloviPoslovi,text='Unesite posao',command=insertposao)
        insertposao_button.grid(row=6,column=1)
        #
        ##
        selectposaoplata_label=Label(PosloviPoslovi,text ='Izaberite posao po ID-u i Nazivu ')
        selectposaoplata_label.grid(row=9,column=0)

        global selectposaoplata_entryid
        selectposaoplata_entryid=Entry(PosloviPoslovi,width=30)
        selectposaoplata_entryid.grid(row=9,column=1)

        global selectposaoplata_entrynaziv
        selectposaoplata_entrynaziv=Entry(PosloviPoslovi,width=30)
        selectposaoplata_entrynaziv.grid(row=10,column=1)
        ##
        selectposao_button=Button(PosloviPoslovi,text='Izaberite',command=editP)
        selectposao_button.grid(row=11,column=1)
        ##
        plata_button=Button(PosloviPoslovi,text='Plata za izabrani posao',command=plata)
        plata_button.grid(row=12,column=1)
        ##
        ##
        searchposaoime_label=Label(PosloviPoslovi,text='Pretrazite posao po nazivu:')
        searchposaoime_label.grid(row=13,column=0)
        global searchposaoentry
        searchposaoentry=Entry(PosloviPoslovi,width=30)
        searchposaoentry.grid(row=13,column=1)
        ##
        searchposaoime_button=Button(PosloviPoslovi,text='Pretrazite',command=lambda:[destroyPretrazeno(),pretragaime()])
        searchposaoime_button.grid(row=13,column=2)
        ###
        searchByPoslodavacID=Label(PosloviPoslovi,text='Prikazite poslove od poslodavca')
        searchByPoslodavacID.grid(row=14,column=0)

        cursor=conn.cursor()
        global Variable4
        cursor.execute('Select naziv from [box].[dbo].[poslodavac]')
        printt_cursor=[]
        for row in cursor:
            printt_cursor += (row)
        Variable4=StringVar(PosloviPoslovi)
        Variable4.set('Izaberite')
        listbox4=OptionMenu(PosloviPoslovi,Variable4,*printt_cursor)
        listbox4.grid(row=14,column=1)

        posIdBtn=Button(PosloviPoslovi,text='Izaberite',command=lambda:[destroyPretrazeno(),pretraPoslodavacID()])
        posIdBtn.grid(row=14,column=2)

        ##
        selectsveposlove_button=Button(PosloviPoslovi,text='Prikazite sve poslove',command=sviposlovi)
        selectsveposlove_button.grid(row=15,column=1)
        ##
        
        

            
            
             