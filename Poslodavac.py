from tkinter import *
from tkinter import messagebox
import pyodbc



conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-RIM8T9PN;"
    "Database=BOX;"
    "Trusted_Connection=yes;"
)

class PoslodavacClass():
    def Poslodavac():
        Poslodavac=Toplevel()
        Poslodavac.title('Poslodavci')
        Poslodavac.geometry('600x600')

        ##
        def Grad(self):
            grad.destroy()
            cursor=conn.cursor()
            sql='SELECT ID FROM Drzava WHERE Naziv=?'
            val=VarD.get()
            cursor.execute(sql,val)
            drzavaid=''
            for row in cursor:
                drzavaid=row[0]
            
            cursor2=conn.cursor()
            sql2='SELECT Naziv FROM Grad WHERE DrzavaID=?'
            val2=drzavaid
            cursor2.execute(sql2,val2)
            gradnaziv=[]
            for row in cursor2:
                gradnaziv += (row)
            global varGr
            varGr=StringVar(Poslodavac)
            varGr.set('Izaberite')
            global gradovi_optionmenu
            gradovi_optionmenu=OptionMenu(Poslodavac,varGr,*gradnaziv,command=lambda self='':[ifOpstinaExists2(),Opstina(self)])
            gradovi_optionmenu.grid(row=6,column=1)

        def Opstina(self):
            opstina.destroy()
            cursor=conn.cursor()
            sql='SELECT DrzavaID,Id FROM Grad WHERE Naziv=?'
            val=varGr.get()
            cursor.execute(sql,val)
            drzavaid=''
            gradid=''
            for row in cursor:
                drzavaid=row[0]
                gradid=row[1]
            
            cursor2=conn.cursor()
            sql2='SELECT Naziv FROM Opstina WHERE Drzavaid=? and Gradid=?'
            val2=(drzavaid,gradid)
            cursor2.execute(sql2,val2)
            opstinanaziv=[]
            for row in cursor2:
                opstinanaziv += (row)
            global varOp
            varOp=StringVar(Poslodavac)
            varOp.set('Izaberite')
            global opstine_optionmenu
            opstine_optionmenu=OptionMenu(Poslodavac,varOp,*opstinanaziv,command=lambda self='':[ifUlicaExists2(),Ulica(self)])
            opstine_optionmenu.grid(row=7,column=1)

        def Ulica(self):
            ulica.destroy()
            cursor=conn.cursor()
            sql='SELECT DrzavaID,GradID,ID FROM Opstina WHERE Naziv=?'
            val=varOp.get()
            cursor.execute(sql,val)
            drzavaid=''
            gradid=''
            opstinaid=''
            for row in cursor:
                drzavaid=row[0]
                gradid=row[1]
                opstinaid=row[2]

            cursor2=conn.cursor()
            sql2='SELECT Naziv FROM Ulica WHERE DrzavaID=? and GradID=? and OpstinaID=?'
            val2=(drzavaid,gradid,opstinaid)
            cursor2.execute(sql2,val2)
            ulicanaziv=[]
            for row in cursor2:
                ulicanaziv += (row)
            global varUl
            varUl=StringVar(Poslodavac)
            varUl.set('Izaberite')
            global ulice_optionmenu
            ulice_optionmenu=OptionMenu(Poslodavac,varUl,*ulicanaziv,command=lambda self='':[ifBrojExists2(),Broj(self)])
            ulice_optionmenu.grid(row=8,column=1)

        def Broj(self):
            broj.destroy()
            cursor=conn.cursor()
            sql='SELECT DrzavaID,GradID,OpstinaID,ID FROM Ulica WHERE Naziv=?'
            val=varUl.get()
            cursor.execute(sql,val)
            drzavaid=''
            gradid=''
            opstinaid=''
            ulicaid=''
            for row in cursor:
                drzavaid=row[0]
                gradid=row[1]
                opstinaid=row[2]
                ulicaid=row[3]
            
            cursor2=conn.cursor()
            sql2='SELECT BrojID FROM Broj WHERE DrzavaID=? AND GradID=? AND OpstinaID=? AND UlicaID=?'
            val2=(drzavaid,gradid,opstinaid,ulicaid)
            cursor2.execute(sql2,val2)
            brojevi=[]
            for row in cursor2:
                brojevi += (row)
            global varBr
            varBr=StringVar(Poslodavac)
            varBr.set('Izaberite')
            global broj_optionmenu
            broj_optionmenu=OptionMenu(Poslodavac,varBr,*brojevi)
            broj_optionmenu.grid(row=9,column=1)

        def ifGradExists2():
            try:
                gradovi_optionmenu
            except Exception:
                pass
            else:
                if grad:
                    gradovi_optionmenu.destroy()
                    try:
                        opstine_optionmenu
                    except Exception:
                        pass
                    else:
                        try:
                            opstine_optionmenu.configure(state='disabled')
                            varOp.set('Izaberite prvo grad')
                        except Exception:
                            pass
                        else:
                            pass

                    try:
                        ulice_optionmenu
                    except Exception:
                        pass
                    else:
                        try:
                            ulice_optionmenu.configure(state='disabled')
                            varUl.set('Izaberite prvo opstinu')
                        except Exception:
                            pass
                        else:
                            pass
                    try:
                        broj_optionmenu
                    except Exception:
                        pass
                    else:
                        try:
                            broj_optionmenu.configure(state='disabled')
                            varBr.set('Izaberite prvo Ulicu')
                        except Exception:
                            pass
                        else:
                            pass           
                else:
                    pass

        def ifOpstinaExists2():
            try:
                opstine_optionmenu
            except Exception:
                pass
            else:
                if opstina:
                    opstine_optionmenu.destroy()
                    try:
                        ulice_optionmenu
                    except Exception:
                        pass
                    else:
                        try:
                            ulice_optionmenu.configure(state='disabled')
                            varUl.set('Izaberite prvo opstinu')
                        except Exception:
                            pass
                        else:
                            pass
                    try:
                        broj_optionmenu
                    except Exception:
                        pass
                    else:
                        try:
                            broj_optionmenu.configure(state='disabled')
                            varBr.set('Izaberite prvo Ulicu')
                        except Exception:
                            pass
                        else:
                            pass  
                else:
                    pass

        def ifUlicaExists2():
            try:
                ulice_optionmenu
            except Exception:
                pass
            else:
                if ulica:
                    ulice_optionmenu.destroy()
                    try: 
                        broj_optionmenu
                    except Exception:
                        pass
                    else:
                        try:
                            broj_optionmenu.configure(state='disabled')
                            varBr.set('Izaberite prvo Ulicu')
                        except Exception:
                            pass
                        else:
                            pass  
                else:
                    pass
        
        def ifBrojExists2():
            try:
                broj_optionmenu
            except Exception:
                pass
            else:
                broj_optionmenu.destroy()

        def sviPoslodavci():
            SviPoslodavci=Toplevel()
            SviPoslodavci.title('Svi poslodavci')
            SviPoslodavci.geometry('600x600')

            cursor=conn.cursor()
            sql='SELECT * FROM Poslodavac'
            cursor.execute(sql)
            poslodavci0=''
            poslodavci1=''
            poslodavci2=''
            poslodavci3=''
            poslodavci4=''
            for row in cursor:
                poslodavci0 += str(row[0]) + "\n"
                poslodavci1 += str(row[1]) + "\n"
                poslodavci2 += str(row[2]) + "\n"
                poslodavci3 += str(row[3]) + "\n"
                poslodavci4 += str(row[4]) + "\n"
            
            poslodavciid=Label(SviPoslodavci,text='ID')
            poslodavciid.grid(row=0,column=0)

            poslodavcinaziv=Label(SviPoslodavci,text='Naziv')
            poslodavcinaziv.grid(row=0,column=1)

            poslodavcitelefon=Label(SviPoslodavci,text='Telefon')
            poslodavcitelefon.grid(row=0,column=2)

            poslodavciPIB=Label(SviPoslodavci,text='PIB')
            poslodavciPIB.grid(row=0,column=3)

            poslodavciTR=Label(SviPoslodavci,text='Tekuci racun')
            poslodavciTR.grid(row=0,column=4)
            ##
            poslodavci0_label=Label(SviPoslodavci,text=poslodavci0)
            poslodavci0_label.grid(row=1,column=0)    

            poslodavci1_label=Label(SviPoslodavci,text=poslodavci1)
            poslodavci1_label.grid(row=1,column=1) 

            poslodavci2_label=Label(SviPoslodavci,text=poslodavci2)
            poslodavci2_label.grid(row=1,column=2) 

            poslodavci3_label=Label(SviPoslodavci,text=poslodavci3)
            poslodavci3_label.grid(row=1,column=3) 

            poslodavci4_label=Label(SviPoslodavci,text=poslodavci4)
            poslodavci4_label.grid(row=1,column=4)    

        def pretragaPoslodavca():
            cursor=conn.cursor()
            sql='SELECT * FROM Poslodavac WHERE Naziv=?'
            val=pretraga_entry.get()
            cursor.execute(sql,val)
            print_cursor=''
            for row in cursor:
                print_cursor += str(row[0]) + " " + str(row[1]) + " " + str(row[2]) +  "\n"     
            if not print_cursor:
                global pretraga_poslodavac_empty
                pretraga_poslodavac_empty=Label(Poslodavac,text='Nije pronadjen ni jedan poslodavac')
                pretraga_poslodavac_empty.grid(row=16,column=1)
            else:
                global pretraga_poslodavac
                pretraga_poslodavac=Label(Poslodavac,text=print_cursor)
                pretraga_poslodavac.grid(row=16,column=1)
            
        def destroyPretraga():
            try:
                pretraga_poslodavac_empty.destroy()
            except Exception:
                pass
            else:
                pass
            try:
                pretraga_poslodavac.destroy()
            except Exception:
                pass
            else:
                pass

        # insert poslodavac#
        def insertPoslodavac():
            try:
                cursorD=conn.cursor()
                sqlD='SELECT ID FROM Drzava WHERE Naziv=?'
                vD=VarD.get()
                cursorD.execute(sqlD,vD)
                DrzavaID=''
                for row in cursorD:
                    DrzavaID=row[0]

                cursorG=conn.cursor()
                sqlG='SELECT ID FROM GRAD WHERE Naziv=? AND DrzavaID=?'
                vGG=(varGr.get(),DrzavaID)
                cursorG.execute(sqlG,vGG)
                GradID=''
                for row in cursorG:
                    GradID=row[0]

                cursorO=conn.cursor()
                sqlO='SELECT ID FROM Opstina WHERE Naziv=? and DrzavaID=? and GradID=?'
                vO=(varOp.get(),DrzavaID,GradID)
                cursorO.execute(sqlO,vO)
                OpstinaID=''
                for row in cursorO:
                    OpstinaID=row[0]

                cursorU=conn.cursor()
                sqlU='SELECT ID FROM Ulica WHERE Naziv=? and DrzavaID=? and GradID=? and OpstinaId=?'
                vU=(varUl.get(),DrzavaID,GradID,OpstinaID)
                cursorU.execute(sqlU,vU)
                UlicaID=''
                for row in cursorU:
                    UlicaID=row[0]

                cursorB=conn.cursor()
                sqlB='SELECT BrojID FROM Broj WHERE DrzavaID=? and GradID=? and OpstinaId=? and UlicaID=? and BrojID=?'
                vB=(DrzavaID,GradID,OpstinaID,UlicaID,varBr.get())
                cursorB.execute(sqlB,vB)
                BrojID=''
                for row in cursorB:
                    BrojID=row[0]

                if entry_naziv.get()=='' :
                    naziv=tuple(entry_naziv.get())
                    messagebox.showerror(title='Neispravan naziv',message='Unesite naziv')
                else:
                    naziv=entry_naziv.get()


            
                cursorInsert=conn.cursor()
                sqlInsert='INSERT INTO Poslodavac (ID,Naziv,Telefon,PIB,TekuciRacun,DrzavaID,GradID,OpstinaID,UlicaID,BrojID) VALUES (?,?,?,?,?,?,?,?,?,?)'
                vInsert=(entry_id.get(),naziv,entry_telefon.get(),entry_pib.get(),entry_tr.get(),DrzavaID,GradID,OpstinaID,UlicaID,BrojID)
                cursorInsert.execute(sqlInsert,vInsert)
                conn.commit()
            except Exception as e:
                messagebox.showerror(title='Neuspesno',message='Popunite sve polja ispravno'+"\n"+"\n"+str(e))
            else:
                messagebox.showinfo(title='Uspesno',message='Uspesno ste uneli poslodavca')

                entry_id.delete(0,END)
                entry_naziv.delete(0,END)
                entry_telefon.delete(0,END)
                entry_pib.delete(0,END)
                entry_tr.delete(0,END)
            
            
            conn.commit()

##
        ##Drzava##
        cursor=conn.cursor()
        cursor.execute('SELECT Naziv FROM Drzava')
        print_cursor=[]
        for row in cursor:
            print_cursor += (row)
        global VarD
        VarD=StringVar(Poslodavac)
        VarD.set('Izaberite')

        drzava=OptionMenu(Poslodavac,VarD,*print_cursor,command=lambda self='':[ifGradExists2(),Grad(self)])
        drzava.grid(row=5,column=1)

        drzavalabel=Label(Poslodavac,text='Izaberite drzavu')
        drzavalabel.grid(row=5,column=0)


        ##Grad pre ###
        varG=StringVar(Poslodavac)
        varG.set('Izaberite prvo drzavu')
        optionsG=''
        global grad
        grad=OptionMenu(Poslodavac,varG,'',*optionsG)
        grad.grid(row=6,column=1)
        grad.configure(state='disabled')
        global gradlabel
        gradlabel=Label(Poslodavac,text='Izaberite grad')
        gradlabel.grid(row=6,column=0)

        ##Opstina pre ###
        varO=StringVar(Poslodavac)
        varO.set('Izaberite prvo grad')
        optionsO=''
        global opstina
        opstina=OptionMenu(Poslodavac,varO,'',*optionsO)
        opstina.grid(row=7,column=1)
        opstina.configure(state='disabled')
        global opstinalabel
        opstinalabel=Label(Poslodavac,text='Izaberite opstinu')
        opstinalabel.grid(row=7,column=0)

        ##Ulica pre ###
        varU=StringVar(Poslodavac)
        varU.set('Izaberite prvo opstinu')
        optionsU=''
        global ulica
        ulica=OptionMenu(Poslodavac,varU,'',*optionsU)
        ulica.grid(row=8,column=1)
        ulica.configure(state='disabled')
        global ulicalabel
        ulicalabel=Label(Poslodavac,text='Izaberite ulicu')
        ulicalabel.grid(row=8,column=0)

        ##Broj pre ###
        varB=StringVar(Poslodavac)
        varB.set('Izaberite prvo ulicu')
        optionsB=''
        global broj
        broj=OptionMenu(Poslodavac,varB,'',*optionsB)
        broj.grid(row=9,column=1)
        broj.configure(state='disabled')
        global brojlabel
        brojlabel=Label(Poslodavac,text='Izaberite broj')
        brojlabel.grid(row=9,column=0)

####################################################################################################################################################
        ### STUDENT SELECT - EDIT ############
        def PoslodavacSelect():
            PoslodavacSelect=Toplevel()
            PoslodavacSelect.title('Poslodavac')
            PoslodavacSelect.geometry('800x600')
            ###

            cursorCheck=conn.cursor()
            sql='select * from Poslodavac where id=?'
            val=izaberiteposlodavcaid.get()

            try:
                cursorCheck.execute(sql,val)
            except Exception:
                neispravanid=Label(PoslodavacSelect,text='Neispravan ID')
                neispravanid.grid(row=0,column=0)
            else:
                pass


            print_cursor=''
            for row in cursorCheck:
               print_cursor= str(row[0])+str(row[1])

            if not print_cursor:
                nista=Label(PoslodavacSelect,text='Nije pronadjen ni jedan poslodavac')
                nista.grid(row=0,column=0)
            else:
                def poslodavacDelete():
                    cursor=conn.cursor()
                    sql='DELETE FROM Poslodavac WHERE ID=?'
                    val=izaberiteposlodavcaid.get()
                    cursor.execute(sql,val)
                    conn.commit()
                    
                
                def popupDeletePoslodavac():
                    try:
                        poslodavacDelete()
                    except Exception as e:
                        messagebox.showerror(title='Neuspesno',message=str(e))
                    else:
                        messagebox.showinfo(title='Uspesno',message='Uspesno ste obrisali poslodavca')

                cursorAdresa=conn.cursor()
                sqlAdresa='SELECT DrzavaID,GradID,OpstinaID,UlicaID,BrojID FROM Poslodavac WHERE ID=?'
                valAdresa=izaberiteposlodavcaid.get()
                cursorAdresa.execute(sqlAdresa,valAdresa)
                for row in cursorAdresa:
                    drzavaIdAdresa=row[0]
                    gradIdAdresa=row[1]
                    opstinaIdAdresa=row[2]
                    ulicaIdAdresa=row[3]
                    brojIdAdresa=row[4]
                #####
                cursorAdresaDrzava=conn.cursor()
                sqlAdresaDrzava='SELECT Naziv FROM Drzava WHERE ID=?'
                valAdresaDrzava=drzavaIdAdresa
                cursorAdresaDrzava.execute(sqlAdresaDrzava,valAdresaDrzava)
                for row in cursorAdresaDrzava:
                    drzavaNazivAdresa=row[0]

                drzavaNaziv=Label(PoslodavacSelect,text='Naziv drzave:')
                drzavaNaziv.grid(row=9,column=0)

                drzavaNazivS=Entry(PoslodavacSelect,width=30)
                drzavaNazivS.grid(row=9,column=1)
                drzavaNazivS.insert(0,drzavaNazivAdresa)
                #####
                cursorAdresaGrad=conn.cursor()
                sqlAdresaGrad='select naziv from grad where drzavaid=? and id=?'
                valAdresaGrad=(drzavaIdAdresa,gradIdAdresa)
                cursorAdresaGrad.execute(sqlAdresaGrad,valAdresaGrad)
                for row in cursorAdresaGrad:
                    gradNazivAdresa=row[0]

                gradNaziv=Label(PoslodavacSelect,text='Naziv grada:')
                gradNaziv.grid(row=10,column=0)

                gradNazivS=Entry(PoslodavacSelect,width=30)
                gradNazivS.grid(row=10,column=1)
                gradNazivS.insert(0,gradNazivAdresa)
                ####
                cursorAdresaOpstina=conn.cursor()
                sqlAdresaOpstina='select naziv from opstina where drzavaid=? and gradid=? and id=?'
                valAdresaOpstina=(drzavaIdAdresa,gradIdAdresa,opstinaIdAdresa)
                cursorAdresaOpstina.execute(sqlAdresaOpstina,valAdresaOpstina)
                for row in cursorAdresaOpstina:
                    opstinaNazivAdresa=row[0]

                opstinaNaziv=Label(PoslodavacSelect,text='Naziv opstine:')
                opstinaNaziv.grid(row=11,column=0)

                opstinaNazivS=Entry(PoslodavacSelect,width=30)
                opstinaNazivS.grid(row=11,column=1)
                opstinaNazivS.insert(0,opstinaNazivAdresa)
                ###
                cursorAdresaUlica=conn.cursor()
                sqlAdresaUlica='select naziv from Ulica where drzavaid=? and gradid=? and OpstinaId=? and id=?'
                valAdresaUlica=(drzavaIdAdresa,gradIdAdresa,opstinaIdAdresa,ulicaIdAdresa)
                cursorAdresaUlica.execute(sqlAdresaUlica,valAdresaUlica)
                for row in cursorAdresaUlica:
                    ulicaNazivAdresa=row[0]

                ulicaNaziv=Label(PoslodavacSelect,text='Naziv ulice:')
                ulicaNaziv.grid(row=12,column=0)

                ulicaNazivS=Entry(PoslodavacSelect,width=30)
                ulicaNazivS.grid(row=12,column=1)
                ulicaNazivS.insert(0,ulicaNazivAdresa)
                ###
                cursorAdresaBroj=conn.cursor()
                sqlAdresaBroj='SELECT BrojID From Broj where drzavaid=? and gradid=? and OpstinaId=? and ulicaid=? and brojid=?'
                valAdresaBroj=(drzavaIdAdresa,gradIdAdresa,opstinaIdAdresa,ulicaIdAdresa,brojIdAdresa)
                cursorAdresaBroj.execute(sqlAdresaBroj,valAdresaBroj)
                for row in cursorAdresaBroj:
                    brojAdresa=row[0]

                brojNaziv=Label(PoslodavacSelect,text='Broj:')
                brojNaziv.grid(row=13,column=0)

                brojNazivS=Entry(PoslodavacSelect,width=30)
                brojNazivS.grid(row=13,column=1)  
                brojNazivS.insert(0,brojAdresa)
          
                def poslodavacUpdate():
                    
                    cursordid=conn.cursor()
                    sqldid='SELECT ID FROM Drzava WHERE Naziv=?'
                    valdid=drzavaNazivS.get()
                    cursordid.execute(sqldid,valdid)
                    
                    for row in cursordid:
                        didd=row[0]
                    ##
                    cursorgid=conn.cursor()
                    sqlgid='SELECT ID FROM Grad where DrzavaID=? and Naziv=?'
                    valgid=(didd,gradNazivS.get())
                    cursorgid.execute(sqlgid,valgid)
                   
                    for row in cursorgid:
                        gidd=row[0]
                    ##
                    cursoroid=conn.cursor()
                    sqloid='SELECT ID FROM Opstina WHERE DrzavaID=? and GradID=? and Naziv=?'
                    valoid=(didd,gidd,opstinaNazivS.get())
                    cursoroid.execute(sqloid,valoid)
                   
                    for row in cursoroid:
                        oidd=row[0]
                    ##
                    cursoruid=conn.cursor()
                    sqluid='SELECT ID FROM Ulica WHERE DrzavaID=? and GradID=? and OpstinaID=? and Naziv=?'
                    valuid=(didd,gidd,oidd,ulicaNazivS.get())
                    cursoruid.execute(sqluid,valuid)
                
                    for row in cursoruid:
                        uidd=row[0]
                    ##
                    cursorbid=conn.cursor()
                    sqlbid='SELECT BrojID from Broj WHERE DrzavaID=? and GradID=? and OpstinaID=? and UlicaID=? and BrojId=?'
                    valbid=(didd,gidd,oidd,uidd,brojNazivS.get())
                    cursorbid.execute(sqlbid,valbid)
                
                    for row in cursorbid:
                        bidd=row[0]

                    cursor=conn.cursor()
                    global sql
                    global vals
                    sql='UPDATE Poslodavac SET ID=?,Naziv=?,Telefon=?,PIB=?,TekuciRacun=?,DrzavaID=?,GradID=?,OpstinaID=?,UlicaID=?,BrojID=? WHERE ID=?'
                    vals=(entry_id.get(),entry_naziv.get(),entry_telefon.get(),entry_pib.get(),entry_tr.get(),didd,gidd,oidd,uidd,bidd,izaberiteposlodavcaid.get())
                    cursor.execute(sql,vals)
                    conn.commit()
 ############# UPDATE###################################################                   

                def popupUpdatePoslodavac():
                    try:
                        poslodavacUpdate()
                    except Exception as e:
                        messagebox.showerror(title='Neuspesno',message='Popunite sve polja ispravno'+"\n"+"\n"+str(e))
                    else:
                        messagebox.showinfo(title='Uspesno',message='Uspesno ste izmenili poslodavca')

                def poslodavacDestroy():
                    PoslodavacSelect.destroy()


                ###
                idlab=Label(PoslodavacSelect,text='Unesite ID:')
                idlab.grid(row=1,column=0)

                entry_id=Entry(PoslodavacSelect,width=30)
                entry_id.grid(row=1,column=1)
                ##
                naziv=Label(PoslodavacSelect,text='Unesite naziv:')
                naziv.grid(row=2,column=0)

                entry_naziv=Entry(PoslodavacSelect,width=30)
                entry_naziv.grid(row=2,column=1)

                ##
                telefon=Label(PoslodavacSelect,text='Unesite broj telefona:')
                telefon.grid(row=4,column=0)

                entry_telefon=Entry(PoslodavacSelect,width=30)
                entry_telefon.grid(row=4,column=1)
                ##
                pib=Label(PoslodavacSelect,text='Unesite bop:')
                pib.grid(row=5,column=0)

                entry_pib=Entry(PoslodavacSelect,width=30)
                entry_pib.grid(row=5,column=1)
                ##
                tr=Label(PoslodavacSelect,text='Unesite broj tekuceg racuna:')
                tr.grid(row=6,column=0)

                entry_tr=Entry(PoslodavacSelect,width=30)
                entry_tr.grid(row=6,column=1)
                ##


                ###
                izmeniteadresu=Label(PoslodavacSelect,text='Izmenite adresu:')
                izmeniteadresu.grid(row=8,column=3)
                ####
                ###
                updatePoslodavacButton=Button(PoslodavacSelect,text='Izmenite poslodavca',command=lambda:[popupUpdatePoslodavac(),poslodavacUpdate(),poslodavacDestroy()])
                updatePoslodavacButton.grid(row=14,column=1)

                deletePoslodavacButton=Button(PoslodavacSelect,text='Obrisite poslodavca',command=lambda:[popupDeletePoslodavac(),poslodavacDelete(),poslodavacDestroy()])
                deletePoslodavacButton.grid(row=15,column=1)
                ###
                cursor=conn.cursor()
                sql='SELECT * FROM Poslodavac WHERE ID=?'
                val=izaberiteposlodavcaid.get()
                cursor.execute(sql,val)
                for row in cursor:
                    entry_id.insert(0,row[0])
                    entry_naziv.insert(0,row[1])
                    entry_telefon.insert(0,row[2])
                    entry_pib.insert(0,row[3])
                    entry_tr.insert(0,row[4])
 



                def GradS(self):
                    gradSS.destroy()
                    cursor=conn.cursor()
                    sql='SELECT ID FROM Drzava WHERE Naziv=?'
                    val=VarD.get()
                    cursor.execute(sql,val)
                    drzavaid=''
                    for row in cursor:
                        drzavaid=row[0]

                    cursor2=conn.cursor()
                    sql2='SELECT Naziv FROM Grad WHERE DrzavaID=?'
                    val2=drzavaid
                    cursor2.execute(sql2,val2)
                    gradnaziv=[]
                    for row in cursor2:
                        gradnaziv += (row)

                    global varGrS
                    varGrS=StringVar(PoslodavacSelect)
                    varGrS.set('Izaberite')
                    global gradoviS_optionmenu
                    gradoviS_optionmenu=OptionMenu(PoslodavacSelect,varGrS,*gradnaziv,command=lambda self='':[ifOpstinaExists2(),OpstinaS(self),gradE()])
                    gradoviS_optionmenu.grid(row=10,column=3)

                def OpstinaS(self):
                    opstinaSS.destroy()
                    cursor=conn.cursor()
                    sql='SELECT DrzavaID,Id FROM Grad WHERE Naziv=?'
                    val=varGrS.get()
                    cursor.execute(sql,val)
                    drzavaid=''
                    gradid=''
                    for row in cursor:
                        drzavaid=row[0]
                        gradid=row[1]

                    cursor2=conn.cursor()
                    sql2='SELECT Naziv FROM Opstina WHERE Drzavaid=? and Gradid=?'
                    val2=(drzavaid,gradid)
                    cursor2.execute(sql2,val2)
                    opstinanaziv=[]
                    for row in cursor2:
                        opstinanaziv += (row)
                    global varOpS
                    varOpS=StringVar(PoslodavacSelect)
                    varOpS.set('Izaberite')
                    global opstineS_optionmenu
                    opstineS_optionmenu=OptionMenu(PoslodavacSelect,varOpS,*opstinanaziv,command=lambda self='':[ifUlicaExists2(),UlicaS(self),opstinaE()])
                    opstineS_optionmenu.grid(row=11,column=3)

                def UlicaS(self):
                    ulicaSS.destroy()
                    cursor=conn.cursor()
                    sql='SELECT DrzavaID,GradID,ID FROM Opstina WHERE Naziv=?'
                    val=varOpS.get()
                    cursor.execute(sql,val)
                    drzavaid=''
                    gradid=''
                    opstinaid=''
                    for row in cursor:
                        drzavaid=row[0]
                        gradid=row[1]
                        opstinaid=row[2]

                    cursor2=conn.cursor()
                    sql2='SELECT Naziv FROM Ulica WHERE DrzavaID=? and GradID=? and OpstinaID=?'
                    val2=(drzavaid,gradid,opstinaid)
                    cursor2.execute(sql2,val2)
                    ulicanaziv=[]
                    for row in cursor2:
                        ulicanaziv += (row)
                    global varUlS
                    varUlS=StringVar(PoslodavacSelect)
                    varUlS.set('Izaberite')
                    global uliceS_optionmenu
                    uliceS_optionmenu=OptionMenu(PoslodavacSelect,varUlS,*ulicanaziv,command=lambda self='':[ifBrojExists2(),BrojS(self),ulicaE()])
                    uliceS_optionmenu.grid(row=12,column=3)

                def BrojS(self):
                    brojSS.destroy()
                    cursor=conn.cursor()
                    sql='SELECT DrzavaID,GradID,OpstinaID,ID FROM Ulica WHERE Naziv=?'
                    val=varUlS.get()
                    cursor.execute(sql,val)
                    drzavaid=''
                    gradid=''
                    opstinaid=''
                    ulicaid=''
                    for row in cursor:
                        drzavaid=row[0]
                        gradid=row[1]
                        opstinaid=row[2]
                        ulicaid=row[3]

                    cursor2=conn.cursor()
                    sql2='SELECT BrojID FROM Broj WHERE DrzavaID=? AND GradID=? AND OpstinaID=? AND UlicaID=?'
                    val2=(drzavaid,gradid,opstinaid,ulicaid)
                    cursor2.execute(sql2,val2)
                    brojevi=[]
                    for row in cursor2:
                        brojevi += (row)
                    global varBrS
                    varBrS=StringVar(PoslodavacSelect)
                    varBrS.set('Izaberite')
                    global brojS_optionmenu
                    brojS_optionmenu=OptionMenu(PoslodavacSelect,varBrS,*brojevi,command=brojE)
                    brojS_optionmenu.grid(row=13,column=3)

                def ifGradExists2():
                    try:
                        gradoviS_optionmenu
                    except Exception:
                        pass
                    else:
                        if grad:
                            gradoviS_optionmenu.destroy()
                            try:
                                opstineS_optionmenu
                            except Exception:
                                pass
                            else:
                                try:
                                    opstineS_optionmenu.configure(state='disabled')
                                    varOpS.set('Izaberite prvo grad')
                                except Exception:
                                    pass
                                else:
                                    pass
                            try:
                                uliceS_optionmenu
                            except Exception:
                                pass
                            else:
                                try:
                                    uliceS_optionmenu.configure(state='disabled')
                                    varUlS.set('Izaberite prvo opstinu')
                                except Exception:
                                    pass
                                else:
                                    pass
                            try:
                                brojS_optionmenu
                            except Exception:
                                pass
                            else:
                                try:
                                    brojS_optionmenu.configure(state='disabled')
                                    varBrS.set('Izaberite prvo Ulicu')
                                except Exception:
                                    pass
                                else:
                                    pass
                        else:
                            pass

                def ifOpstinaExists2():
                    try:
                        opstineS_optionmenu
                    except Exception:
                        pass
                    else:
                        if opstina:
                            opstineS_optionmenu.destroy()
                            try:
                                uliceS_optionmenu
                            except Exception:
                                pass
                            else:
                                try:
                                    uliceS_optionmenu.configure(state='disabled')
                                    varUlS.set('Izaberite prvo opstinu')
                                except Exception:
                                    pass
                                else:
                                    pass
                            try:
                                brojS_optionmenu
                            except Exception:
                                pass
                            else:
                                try:
                                    brojS_optionmenu.configure(state='disabled')
                                    varBrS.set('Izaberite prvo Ulicu')
                                except Exception:
                                    pass
                                else:
                                    pass
                        else:
                            pass

                def ifUlicaExists2():
                    try:
                        uliceS_optionmenu
                    except Exception:
                        pass
                    else:
                        if ulica:
                            uliceS_optionmenu.destroy()
                            try: 
                                brojS_optionmenu
                            except Exception:
                                pass
                            else:
                                try:
                                    brojS_optionmenu.configure(state='disabled')
                                    varBrS.set('Izaberite prvo Ulicu')
                                except Exception:
                                    pass
                                else:
                                    pass
                        else:
                            pass
                        
                def ifBrojExists2():
                    try:
                        brojS_optionmenu
                    except Exception:
                        pass
                    else:
                        brojS_optionmenu.destroy()

                def drzavaE():
                    drzavaNazivS.delete(0,END)
                    gradNazivS.delete(0,END)
                    opstinaNazivS.delete(0,END)
                    ulicaNazivS.delete(0,END)
                    brojNazivS.delete(0,END)
                    drzavaNazivS.insert(0,VarD.get())

                def gradE():
                    gradNazivS.delete(0,END)
                    opstinaNazivS.delete(0,END)
                    ulicaNazivS.delete(0,END)
                    brojNazivS.delete(0,END)
                    gradNazivS.insert(0,varGrS.get())

                def opstinaE():
                    opstinaNazivS.delete(0,END)
                    ulicaNazivS.delete(0,END)
                    brojNazivS.delete(0,END)
                    opstinaNazivS.insert(0,varOpS.get())

                def ulicaE():
                    ulicaNazivS.delete(0,END)
                    brojNazivS.delete(0,END)
                    ulicaNazivS.insert(0,varUlS.get())

                def brojE(self):
                    brojNazivS.delete(0,END)
                    brojNazivS.insert(0,varBrS.get())

                ##Drzava u SELECT##
                cursor=conn.cursor()
                cursor.execute('SELECT Naziv FROM Drzava')
                print_cursor=[]
                for row in cursor:
                    print_cursor += (row)

                cursorDS=conn.cursor()
                sqlDS='SELECT DrzavaID FROM Poslodavac WHERE ID=?'
                valDS=izaberiteposlodavcaid.get()
                cursorDS.execute(sqlDS,valDS)
                global DSID
                for row in cursorDS:
                    DSID=str(row[0])

                cursorDSNaziv=conn.cursor()
                sqlDSNaziv='SELECT Naziv FROM Drzava WHERE ID=?'
                valDSNaziv=DSID
                cursorDSNaziv.execute(sqlDSNaziv,valDSNaziv)
                for row in cursorDSNaziv:
                    DSNaziv=str(row[0])

                global VarD
                VarD=StringVar(PoslodavacSelect)
                VarD.set(str(DSNaziv))

                drzavaS=OptionMenu(PoslodavacSelect,VarD,*print_cursor,command=lambda self='':[ifGradExists2(),GradS(self),drzavaE()])
                drzavaS.grid(row=9,column=3)
                drzavalabel=Label(PoslodavacSelect,text='Izaberite drzavu')
                drzavalabel.grid(row=9,column=2)


                ####Grad pre u SELECT###
                cursorGS=conn.cursor()
                sqlGS='SELECT GradID FROM Poslodavac WHERE ID=?'
                valGS=izaberiteposlodavcaid.get()
                cursorGS.execute(sqlGS,valGS)
                global GSID
                for row in cursorGS:
                    GSID=str(row[0])

                cursorGSNaziv=conn.cursor()
                sqlGSNaziv='SELECT Naziv FROM Grad WHERE DrzavaID=? and ID=?'
                valGSNaziv=(DSID,GSID)
                cursorGSNaziv.execute(sqlGSNaziv,valGSNaziv)
                for row in cursorGSNaziv:
                    GSNaziv=str(row[0])

                varG=StringVar(PoslodavacSelect)
                varG.set(str(GSNaziv))
                optionsG=''
                global gradSS
                gradSS=OptionMenu(PoslodavacSelect,varG,'',*optionsG)
                gradSS.grid(row=10,column=3)
                gradSS.configure(state='disabled')
                global gradlabel
                gradlabel=Label(PoslodavacSelect,text='Izaberite grad')
                gradlabel.grid(row=10,column=2)

                ##Opstina pre ###
                cursorOS=conn.cursor()
                sqlOS='SELECT OpstinaID FROM Poslodavac WHERE ID=?'
                valOS=izaberiteposlodavcaid.get()
                cursorOS.execute(sqlOS,valOS)
                global OSID
                for row in cursorOS:
                    OSID=str(row[0])

                cursorOSNaziv=conn.cursor()
                sqlOSNaziv='SELECT Naziv FROM Opstina WHERE DrzavaID=? and GradID=? and ID=?'
                valOSNaziv=(DSID,GSID,OSID)
                cursorOSNaziv.execute(sqlOSNaziv,valOSNaziv)
                for row in cursorOSNaziv:
                    OSNaziv=str(row[0])

                varO=StringVar(PoslodavacSelect)
                varO.set(str(OSNaziv))
                optionsO=''
                global opstinaSS
                opstinaSS=OptionMenu(PoslodavacSelect,varO,'',*optionsO)
                opstinaSS.grid(row=11,column=3)
                opstinaSS.configure(state='disabled')
                global opstinalabel
                opstinalabel=Label(PoslodavacSelect,text='Izaberite opstinu')
                opstinalabel.grid(row=11,column=2)

                ##Ulica pre ###
                cursorUS=conn.cursor()
                sqlUS='SELECT UlicaID FROM Poslodavac WHERE ID=?'
                valUS=izaberiteposlodavcaid.get()
                cursorUS.execute(sqlUS,valUS)
                global USID
                for row in cursorUS:
                    USID=str(row[0])

                cursorUSNaziv=conn.cursor()
                sqlUSNaziv='SELECT Naziv FROM Ulica WHERE DrzavaID=? and GradID=? and OpstinaID=? and ID=?'
                valUSNaziv=(DSID,GSID,OSID,USID)
                cursorUSNaziv.execute(sqlUSNaziv,valUSNaziv)
                for row in cursorUSNaziv:
                    USNaziv=str(row[0])


                varU=StringVar(PoslodavacSelect)
                varU.set(str(USNaziv))
                optionsU=''
                global ulicaSS
                ulicaSS=OptionMenu(PoslodavacSelect,varU,'',*optionsU)
                ulicaSS.grid(row=12,column=3)
                ulicaSS.configure(state='disabled')
                global ulicalabel
                ulicalabel=Label(PoslodavacSelect,text='Izaberite ulicu')
                ulicalabel.grid(row=12,column=2)

                ##Broj pre ###
                cursorBS=conn.cursor()
                sqlBS='SELECT BrojID FROM Poslodavac WHERE ID=?'
                valBS=izaberiteposlodavcaid.get()
                cursorBS.execute(sqlBS,valBS)
                global BSID
                for row in cursorBS:
                    BSID=str(row[0])

                cursorBSNaziv=conn.cursor()
                sqlBSNaziv='SELECT BrojID FROM Broj WHERE DrzavaID=? and GradID=? and OpstinaID=? and UlicaID=? and BrojID=?'
                valBSNaziv=(DSID,GSID,OSID,USID,BSID)
                cursorBSNaziv.execute(sqlBSNaziv,valBSNaziv)
                for row in cursorBSNaziv:
                    BSNaziv=str(row[0])

                varB=StringVar(PoslodavacSelect)
                varB.set(str(BSNaziv))
                optionsB=''
                global brojSS
                brojSS=OptionMenu(PoslodavacSelect,varB,'',*optionsB)
                brojSS.grid(row=13,column=3)
                brojSS.configure(state='disabled')
                global brojlabel
                brojlabel=Label(PoslodavacSelect,text='Izaberite broj')
                brojlabel.grid(row=13,column=2)



            ##### STUDENT SELECT - EDIT CLOSED ############

#######################################################################################################################################################
        ####

        ####
        idlab=Label(Poslodavac,text='Unesite ID:')
        idlab.grid(row=0,column=0)

        entry_id=Entry(Poslodavac,width=30)
        entry_id.grid(row=0,column=1)
        ##
        naziv=Label(Poslodavac,text='Unesite naziv:')
        naziv.grid(row=1,column=0)

        entry_naziv=Entry(Poslodavac,width=30)
        entry_naziv.grid(row=1,column=1)
        ##
        telefon=Label(Poslodavac,text='Unesite broj telefona:')
        telefon.grid(row=2,column=0)

        entry_telefon=Entry(Poslodavac,width=30)
        entry_telefon.grid(row=2,column=1)
        ##
        pib=Label(Poslodavac,text='Unesite pib:')
        pib.grid(row=3,column=0)

        entry_pib=Entry(Poslodavac,width=30)
        entry_pib.grid(row=3,column=1)
        ##
        tr=Label(Poslodavac,text='Unesite broj tekuceg racuna:')
        tr.grid(row=4,column=0)

        entry_tr=Entry(Poslodavac,width=30)
        entry_tr.grid(row=4,column=1)
        ##
        insert=Button(Poslodavac,text='Unesite poslodavca',command=insertPoslodavac)
        insert.grid(row=10,column=1)

        izaberiteposlodavca=Label(Poslodavac,text='Izaberite poslodavca po ID-u')
        izaberiteposlodavca.grid(row=11,column=0)
        
        izaberiteposlodavcaid=Entry(Poslodavac,width=30)
        izaberiteposlodavcaid.grid(row=11,column=1)
        ##
        
        izaberite_button=Button(Poslodavac,text='Izaberite poslodavca',command=PoslodavacSelect)
        izaberite_button.grid(row=12,column=1)
        ##
        pretraga=Label(Poslodavac,text='Pretrazite poslodavca po nazivu')
        pretraga.grid(row=13,column=0)

        pretraga_entry=Entry(Poslodavac,width=30)
        pretraga_entry.grid(row=13,column=1)
        ##
        pretraga_button=Button(Poslodavac,text='Pretrazite',command=lambda:[destroyPretraga(),pretragaPoslodavca()])
        pretraga_button.grid(row=14,column=1)
        ##
        sviposlodavac=Button(Poslodavac,text='Prikazite sve poslodavce',command=sviPoslodavci)
        sviposlodavac.grid(row=15,column=1)