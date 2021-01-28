from tkinter import *
from tkinter import messagebox
import pyodbc
from Konekcija import konn

conn = konn
class FakturaClass():
    def Faktura():
        Faktura=Toplevel()
        Faktura.title('Fakture')
        Faktura.geometry('600x600')
        ####
        def insert():
            try:
                cursor2=conn.cursor()
                sql2='SELECT ID FROM Poslodavac WHERE Naziv=?'
                val2=varPs.get()
                cursor2.execute(sql2,val2)
                for row in cursor2:
                    poslodavacid=row[0]

                cursor=conn.cursor()
                sql='INSERT INTO Faktura (ZadrugaID,ID,DatumFakture,OpisFakture,PoslodavacID,PDV) values (?,?,?,?,?,?)'
                val=(1,fakturaid_entry.get(),datum_entry.get(),opis_entry.get(),poslodavacid,pdv_entry.get())
                cursor.execute(sql,val)
                conn.commit()
                
            except Exception as e:
                messagebox.showerror(title='Neuspesno',message='Popunite sve polja ispravno'+"\n"+"\n"+str(e))
            else:
                messagebox.showinfo(title='Uspesno',message='Uspesno ste uneli fakturu')

                fakturaid_entry.delete(0,END)
                datum_entry.delete(0,END)
                opis_entry.delete(0,END)
                pdv_entry.delete(0,END)
            
        def sveFakture():
            Sve=Toplevel()
            Sve.title('Sve fakture')
            Sve.geometry('600x600')

            cursor=conn.cursor()
            sql='SELECT * FROM Faktura'
            cursor.execute(sql)
            global idF
            global datumF
            global opisF
            global iznosF
            global zadrugaF
            global poslodavacidF
            global pdv
            zadrugaF=''
            idF=''
            datumF=''
            opisF=''
            iznosF=''
            poslodavacidF=''
            pdv=''
            for row in cursor:
                zadrugaF += 'Box' + "\n"
                idF += str(row[1]) + "\n"
                datumF += str(row[2]) + "\n"
                opisF += str(row[3]) + "\n"
                iznosF += str(row[4]) + "\n" 
                poslodavacidF += str(row[5]) + "\n"
                pdv += str(row[6]) + "\n"
             ###
            zadruga=Label(Sve,text='Zadruga')
            zadruga.grid(row=0,column=0)

            zadrugaNaziv=Label(Sve,text=zadrugaF)
            zadrugaNaziv.grid(row=1,column=0)
            ###
            faktura=Label(Sve,text='Faktura ID')
            faktura.grid(row=0,column=1)

            fakturaid=Label(Sve,text=idF)
            fakturaid.grid(row=1,column=1)

            ###
            opisFakture=Label(Sve,text='Naziv fakture')
            opisFakture.grid(row=0,column=2)

            opisFaktureE=Label(Sve,text=opisF)
            opisFaktureE.grid(row=1,column=2)
            ###
            datumFaktura=Label(Sve,text='Datum fakture')
            datumFaktura.grid(row=0,column=3)

            datumfakturaF=Label(Sve,text=datumF)
            datumfakturaF.grid(row=1,column=3)
            ###
            iznos=Label(Sve,text='Iznos fakture')
            iznos.grid(row=0,column=4)

            iznosF=Label(Sve,text=iznosF)
            iznosF.grid(row=1,column=4)
            ###
            poslodavac=Label(Sve,text='ID poslodavca')
            poslodavac.grid(row=0,column=5)

            poslodavacF=Label(Sve,text=poslodavacidF)
            poslodavacF.grid(row=1,column=5)
            ###
            pdvSve=Label(Sve,text='PDV')
            pdvSve.grid(row=0,column=6)

            pdvSveF=Label(Sve,text=pdv)
            pdvSveF.grid(row=1,column=6)

        def selectFakturu():
            SelectFaktura=Toplevel()
            SelectFaktura.title('Izabrana faktura')
            SelectFaktura.geometry('750x600')

            cursor=conn.cursor()
            sql='SELECT * FROM Faktura WHERE ID=?'
            val=pretragaid.get()

            try:
                cursor.execute(sql,val)
            except Exception:
                neispravno=Label(SelectFaktura,text='Neispravno unet ID')
                neispravno.grid(row=0,column=0)
            else:
                pass

            fakturaidd=''
            datumfakture=''
            opisfakture=''
            iznosfakture=''
            pdvFakture=''
            for row in cursor:
                fakturaidd=str(row[1])
                datumfakture=str(row[2])
                opisfakture=str(row[3])
                iznosfakture=str(row[4])
                poslodavacid=row[5]
                pdvFakture=str(row[6])
            
            if not fakturaidd:
                nema=Label(SelectFaktura,text='Nije pronadjena ni jedna faktura')
                nema.grid(row=0,column=0)
            else:

                cursor2=conn.cursor()
                sql2='SELECT Naziv FROM Poslodavac WHERE ID=?'
                val2=poslodavacid
                cursor2.execute(sql2,val2)
                nazivposlodavca=''
                for row in cursor2:
                    nazivposlodavca=str(row[0])

                ###
                zadruga=Label(SelectFaktura,text='Zadruga')
                zadruga.grid(row=0,column=0)

                zadrugaN=Label(SelectFaktura,text='Box')
                zadrugaN.grid(row=0,column=1)
                ###
                fakturaid=Label(SelectFaktura,text='ID Fakture')
                fakturaid.grid(row=1,column=0)

                fakturaidN=Label(SelectFaktura,text=fakturaidd)
                fakturaidN.grid(row=1,column=1)

                ###
                fakturadatum=Label(SelectFaktura,text='Datum Fakture')
                fakturadatum.grid(row=2,column=0)

                fakturadatumN=Entry(SelectFaktura,width=30)
                fakturadatumN.grid(row=2,column=1)
                fakturadatumN.insert(0,datumfakture)
                ###
                fakturaopis=Label(SelectFaktura,text='Naziv Fakture')
                fakturaopis.grid(row=3,column=0)

                fakturaopisN=Entry(SelectFaktura,width=30)
                fakturaopisN.grid(row=3,column=1)
                fakturaopisN.insert(0,opisfakture)
                ###
                fakturaiznos=Label(SelectFaktura,text='Iznos Fakture')
                fakturaiznos.grid(row=4,column=0)

                fakturaiznosN=Entry(SelectFaktura,width=30)
                fakturaiznosN.grid(row=4,column=1)
                fakturaiznosN.insert(0,iznosfakture)
                ####
                fakturaPDV=Label(SelectFaktura,text='PDV')
                fakturaPDV.grid(row=5,column=0)

                fakturaPDV_entry=Entry(SelectFaktura,width=30)
                fakturaPDV_entry.grid(row=5,column=1)
                fakturaPDV_entry.insert(0,pdvFakture)
                ###
                fakturaPoslodavacNaziv=Label(SelectFaktura,text='Naziv poslodavca')
                fakturaPoslodavacNaziv.grid(row=6,column=0)

                fakturaPoslodavacNazivN=Label(SelectFaktura,text=nazivposlodavca)
                fakturaPoslodavacNazivN.grid(row=6,column=1)
                ###
                def updateFakturu():
                    try:
                        cursor=conn.cursor()
                        sql='UPDATE Faktura SET DatumFakture=?,OpisFakture=?,PDV=? WHERE ID=?'
                        val=(fakturadatumN.get(),fakturaopisN.get(),fakturaPDV_entry.get(),pretragaid.get())
                        cursor.execute(sql,val)
                        conn.commit()
                    except Exception as e:
                        messagebox.showerror(title='Neuspesno',message='Popunite sve polja ispravno'+"\n"+"\n"+str(e))
                    else:
                        messagebox.showinfo(title='Uspesno',message='Uspesno ste updateovali fakturu')
                        SelectFaktura.destroy()

                def iznosFaktureUpdate():
                    cursor=conn.cursor()
                    sql='SELECT IznosFakture FROM Faktura WHERE ID=?'
                    val=pretragaid.get()
                    cursor.execute(sql,val)
                    iznos=''
                    for row in cursor:
                        iznos=str(row[0])
                    if (iznos != str(fakturaiznosN.get())):
                        cursor2=conn.cursor()
                        sql2='UPDATE Faktura SET IznosFakture=? WHERE ID=?'
                        val2=(fakturaiznosN.get(),pretragaid.get())
                        try: 
                            cursor2.execute(sql2,val2)
                            conn.commit()
                        except Exception as e:
                            messagebox.showerror(title='Neuspesno',message=str(e))
                            SelectFaktura.destroy()
                        else:
                            pass

                def deleteFakturu():
                    try:
                        cursor=conn.cursor()
                        sql='DELETE FROM Faktura WHERE ID=?'
                        val=pretragaid.get()
                        cursor.execute(sql,val)
                        conn.commit()
                    except Exception as e:
                        messagebox.showerror(title='Neuspesno',message=str(e))
                    else:
                        messagebox.showinfo(title='Uspesno',message='Uspesno ste obirsali fakturu')
                        SelectFaktura.destroy()

                def deleteStavkeZaFakturu():
                    cursor=conn.cursor()
                    sql='DELETE FROM StavkaFakture WHERE FakturaID=?'
                    val=pretragaid.get()
                    cursor.execute(sql,val)
                    conn.commit()


                ###
                fakturaUpdate_button=Button(SelectFaktura,text='Update fakturu',command=lambda:[iznosFaktureUpdate(),updateFakturu()])
                fakturaUpdate_button.grid(row=7,column=1)

                fakturaDelete_button=Button(SelectFaktura,text='Obrisite fakturu',command=lambda:[deleteStavkeZaFakturu(),deleteFakturu()])
                fakturaDelete_button.grid(row=8,column=1)       
                ###
                novaStavka=Label(SelectFaktura,text='Dodajte stavku')
                novaStavka.grid(row=16,column=1)
                ###
                noviID=Label(SelectFaktura,text='Unesite ID')
                noviID.grid(row=17,column=0)

                noviID_entry=Entry(SelectFaktura,width=30)
                noviID_entry.grid(row=18,column=0)
                ###
                noviRB=Label(SelectFaktura,text='Unesite redni broj')
                noviRB.grid(row=17,column=1)

                noviRB_entry=Entry(SelectFaktura,width=30)
                noviRB_entry.grid(row=18,column=1)
                ###
                noviOpis=Label(SelectFaktura,text='Unesite opis')
                noviOpis.grid(row=17,column=2)

                noviOpis_entry=Entry(SelectFaktura,width=30)
                noviOpis_entry.grid(row=18,column=2)
                ##
                noviIznos=Label(SelectFaktura,text='Unesite iznos')
                noviIznos.grid(row=17,column=3)

                noviIznos_entry=Entry(SelectFaktura,width=30)
                noviIznos_entry.grid(row=18,column=3)
                ###
                def insertStavku():
                    try:
                        cursor=conn.cursor()
                        sql='SELECT ZadrugaId,ID FROM Faktura WHERE ID=?'
                        val=pretragaid.get()
                        cursor.execute(sql,val)
                        for row in cursor:
                            zadrugaid=row[0]
                            fakturaid=row[1]

                        if noviID_entry.get()=='':
                            nID=tuple(noviID_entry.get())
                            messagebox.showerror(title='Neispravan id',message='Unesite id')
                        else:
                            nID=noviID_entry.get()

                        if noviRB_entry.get()=='':
                            nRB=tuple(noviRB_entry.get())
                            messagebox.showerror(title='Neispravan redni broj',message='Unesite redni broj')
                        else:
                            nRB=noviRB_entry.get()

                        if noviOpis_entry.get()=='':
                            nOpis=tuple(noviOpis_entry.get())
                            messagebox.showerror(title='Neispravan opis',message='Unesite opis')
                        else:
                            nOpis=noviOpis_entry.get()

                        if noviIznos_entry.get()=='':
                            nIznos=tuple(noviIznos_entry.get())
                            messagebox.showerror(title='Neispravan iznos',message='Unesite iznos')
                        else:
                            nIznos=noviIznos_entry.get()

                        cursor2=conn.cursor()
                        sql2='INSERT INTO StavkaFakture VALUES (?,?,?,?,?,?)'
                        val2=(zadrugaid,fakturaid,nID,nRB,nOpis,nIznos)
                        cursor2.execute(sql2,val2)
                        conn.commit()
                    except Exception as e:
                        messagebox.showerror(title='Neuspesno',message='Popunite sve polja ispravno'+"\n"+"\n"+str(e))
                    else:
                        messagebox.showinfo(title='Uspesno',message='Uspesno ste uneli novu stavku fakture')
                        SelectFaktura.destroy()




                ########    
                insertStavka=Button(SelectFaktura,text='Unesite stavku',command=insertStavku)
                insertStavka.grid(row=19,column=1)
                ###
                ##
                cursor3=conn.cursor()
                sql3='SELECT * FROM StavkaFakture WHERE FakturaID=?'
                val3=pretragaid.get()
                cursor3.execute(sql3,val3)
                stavkaId=''
                stavkaRedniBroj=''
                stavkaOpis=''
                stavkaIznos=''
                for row in cursor3:
                    stavkaId += str(row[2]) + "\n"
                    stavkaRedniBroj += str(row[3]) + "\n"
                    stavkaOpis += str(row[4]) + "\n"
                    stavkaIznos += str(row[5]) + "\n"
                
                if not stavkaId :
                    nemaStavki=Label(SelectFaktura,text='Stavke za izabranu fakturu:')
                    nemaStavki.grid(row=9,column=1)

                    nemaStavki=Label(SelectFaktura,text='Nema stavki za izabranu fakturu')
                    nemaStavki.grid(row=10,column=1)
                ###
                else:
                    nemaStavki=Label(SelectFaktura,text='Stavke za izabranu fakturu:')
                    nemaStavki.grid(row=9,column=1)
                    ###
                    idstavka=Label(SelectFaktura,text='Stavka ID')
                    idstavka.grid(row=10,column=0)

                    idstavkaI=Label(SelectFaktura,text=stavkaId)
                    idstavkaI.grid(row=11,column=0)
                    ###
                    rbstavka=Label(SelectFaktura,text='Redni broj stavke')
                    rbstavka.grid(row=10,column=1)

                    rbstavkaI=Label(SelectFaktura,text=stavkaRedniBroj)
                    rbstavkaI.grid(row=11,column=1)
                    ###
                    opisstavka=Label(SelectFaktura,text='Opis stavke')
                    opisstavka.grid(row=10,column=2)

                    opisstavkaI=Label(SelectFaktura,text=stavkaOpis)
                    opisstavkaI.grid(row=11,column=2)
                    ###
                    iznosstavka=Label(SelectFaktura,text='Iznos stavke')
                    iznosstavka.grid(row=10,column=3)

                    iznosstavkaI=Label(SelectFaktura,text=stavkaIznos)
                    iznosstavkaI.grid(row=11,column=3)

                    def stavkaSelect():
                        Stavka=Toplevel()
                        Stavka.title('Stavka fakture')
                        Stavka.geometry('600x600')

                        cursor2=conn.cursor()
                        sql2='SELECT id FROM StavkaFakture WHERE FakturaID=? and ID=?'
                        val2=(pretragaid.get(),selectStavka_entry.get())
                        cursor2.execute(sql2,val2)
                        stavkaiddd=''
                        for row in cursor2:
                            stavkaiddd=row[0]

                        if not stavkaiddd:
                            nemastavke=Label(Stavka,text='Nije pronadjena ni jedna stavka')
                            nemastavke.grid(row=0,column=0)
                        else:
                            ###
                            stavkaid=Label(Stavka,text='Stavka id')
                            stavkaid.grid(row=0,column=0)

                            stavkaid_entry=Entry(Stavka,width=30)
                            stavkaid_entry.grid(row=0,column=1)
                            ###
                            stavkarb=Label(Stavka,text='Redni broj stavke')
                            stavkarb.grid(row=1,column=0)

                            stavkarb_entry=Entry(Stavka,width=30)
                            stavkarb_entry.grid(row=1,column=1)
                            ###
                            stavkaopis=Label(Stavka,text='Opis stavke')
                            stavkaopis.grid(row=2,column=0)

                            stavkaopis_entry=Entry(Stavka,width=30)
                            stavkaopis_entry.grid(row=2,column=1)
                            ###
                            stavkaiznos=Label(Stavka,text='Iznos stavke')
                            stavkaiznos.grid(row=3,column=0)

                            stavkaiznos_entry=Entry(Stavka,width=30)
                            stavkaiznos_entry.grid(row=3,column=1)
                            ###
                            cursor=conn.cursor()
                            sql='SELECT * FROM StavkaFakture WHERE FakturaID=? and ID=?'
                            val=(pretragaid.get(),selectStavka_entry.get())
                            cursor.execute(sql,val)
                            for row in cursor:
                                stavkaid_entry.insert(0,row[2])
                                stavkarb_entry.insert(0,row[3])
                                stavkaopis_entry.insert(0,row[4])
                                stavkaiznos_entry.insert(0,row[5])

                            def updateStavku():
                                try:

                                    if stavkaid_entry.get()=='':
                                        nID=tuple(stavkaid_entry.get())
                                        messagebox.showerror(title='Neispravan id',message='Unesite id')
                                    else:
                                        nID=stavkaid_entry.get()

                                    if stavkarb_entry.get()=='':
                                        nRB=tuple(stavkarb_entry.get())
                                        messagebox.showerror(title='Neispravan redni broj',message='Unesite redni broj')
                                    else:
                                        nRB=stavkarb_entry.get()

                                    if stavkaopis_entry.get()=='':
                                        nOpis=tuple(stavkaopis_entry.get())
                                        messagebox.showerror(title='Neispravan opis',message='Unesite opis')
                                    else:
                                        nOpis=stavkaopis_entry.get()

                                    if stavkaiznos_entry.get()=='':
                                        nIznos=tuple(stavkaiznos_entry.get())
                                        messagebox.showerror(title='Neispravan iznos',message='Unesite iznos')
                                    else:
                                        nIznos=stavkaiznos_entry.get()

                                    #####    
                                    cursor=conn.cursor()
                                    sql='UPDATE StavkaFakture SET ID=?,RedniBroj=?,OpisStavke=?,IznosStavke=? WHERE FakturaID=? and ID=?'
                                    val=(nID,nRB,nOpis,nIznos,pretragaid.get(),selectStavka_entry.get())
                                    cursor.execute(sql,val)
                                    conn.commit()
                                except Exception as e:
                                    messagebox.showerror(title='Neuspesno',message='Popunite sve polja ispravno'+"\n"+"\n"+str(e))
                                else:
                                    messagebox.showinfo(title='Uspesno',message='Uspesno ste updateovali stavku')
                                    Stavka.destroy()
                                    SelectFaktura.destroy()

                            def deleteStavku():
                                try:
                                    cursor=conn.cursor()
                                    sql='DELETE FROM StavkaFakture WHERE FakturaID=? and ID=?'
                                    val=(pretragaid.get(),selectStavka_entry.get())
                                    cursor.execute(sql,val)
                                    conn.commit()
                                except Exception as e:
                                    messagebox.showerror(title='Neuspesno',message=str(e))
                                else:
                                    messagebox.showinfo(title='Uspesno',message='Uspesno ste obrisali stavku')
                                    Stavka.destroy()
                                    SelectFaktura.destroy()
                                
                            ####    
                            stavkaUpdate=Button(Stavka,text='Update stavku',command=updateStavku)
                            stavkaUpdate.grid(row=4,column=1)

                            stavkaDelete=Button(Stavka,text='Obrisite stavku',command=deleteStavku)
                            stavkaDelete.grid(row=5,column=1)


                    ####    
                    selectStavka=Label(SelectFaktura,text='Izaberite stavku')
                    selectStavka.grid(row=13,column=0)

                    selectStavka_entry=Entry(SelectFaktura,width=30)
                    selectStavka_entry.grid(row=13,column=1)

                    selectStavka_btn=Button(SelectFaktura,text='Izaberite stavku',command=stavkaSelect)
                    selectStavka_btn.grid(row=14,column=1)
            

           

        ####
        zadruga=Label(Faktura,text='Zadruga')
        zadruga.grid(row=0,column=0)

        zadrugaNaziv=Label(Faktura,text='BOX')
        zadrugaNaziv.grid(row=0,column=1)
        ###
        fakturaid=Label(Faktura,text='Unesite id fakture')
        fakturaid.grid(row=1,column=0)
        global fakturaid_entry
        fakturaid_entry=Entry(Faktura,width=30)
        fakturaid_entry.grid(row=1,column=1)
        ###
        datum=Label(Faktura,text='Unesite datum fakture')
        datum.grid(row=2,column=0)
        global datum_entry
        datum_entry=Entry(Faktura,width=30)
        datum_entry.grid(row=2,column=1)
        ###
        opis=Label(Faktura,text='Unesite naziv fakture')
        opis.grid(row=3,column=0)
        global opis_entry
        opis_entry=Entry(Faktura,width=30)
        opis_entry.grid(row=3,column=1)
        ###
        pdv=Label(Faktura,text='Unesite pdv (u %) za fakturu ')
        pdv.grid(row=4,column=0)
        global pdv_entry
        pdv_entry=Entry(Faktura,width=30)
        pdv_entry.grid(row=4,column=1)
        ###
        poslodavac=Label(Faktura,text='Izaberite poslodavca')
        poslodavac.grid(row=5,column=0)

        cursor=conn.cursor()
        sql='SELECT Naziv FROM Poslodavac'
        cursor.execute(sql)
        poslodavcii=[]
        for row in cursor:
            poslodavcii += (row)

        global varPs
        varPs=StringVar(Faktura)
        varPs.set('Izaberite')
        poslodavci=OptionMenu(Faktura,varPs,*poslodavcii)
        poslodavci.grid(row=5,column=1)

        ###
        insertButton=Button(Faktura,text='Unesite fakturu',command=insert)
        insertButton.grid(row=6,column=1)

        ###
        pretraga=Label(Faktura,text='Izaberite fakturu po ID-u')
        pretraga.grid(row=7,column=0)

        pretragaid=Entry(Faktura,width=30)
        pretragaid.grid(row=7,column=1)
        ###
        selectFakturu=Button(Faktura,text='Prikazite fakturu',command=selectFakturu)
        selectFakturu.grid(row=8,column=1)
        ##
        sveFakture=Button(Faktura,text='Prikazite sve fakture',command=sveFakture)
        sveFakture.grid(row=9,column=1)


        