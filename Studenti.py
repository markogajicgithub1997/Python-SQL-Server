from tkinter import *
from tkinter import messagebox
import pyodbc



conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-RIM8T9PN;"
    "Database=BOX;"
    "Trusted_Connection=yes;"
)

class StudentiClass():
    def Studenti():
        Studenti=Toplevel()
        Studenti.title('Studenti')
        Studenti.geometry('600x600')

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
            varGr=StringVar(Studenti)
            varGr.set('Izaberite')
            global gradovi_optionmenu
            gradovi_optionmenu=OptionMenu(Studenti,varGr,*gradnaziv,command=lambda self='':[ifOpstinaExists2(),Opstina(self)])
            gradovi_optionmenu.grid(row=8,column=1)

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
            varOp=StringVar(Studenti)
            varOp.set('Izaberite')
            global opstine_optionmenu
            opstine_optionmenu=OptionMenu(Studenti,varOp,*opstinanaziv,command=lambda self='':[ifUlicaExists2(),Ulica(self)])
            opstine_optionmenu.grid(row=9,column=1)

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
            varUl=StringVar(Studenti)
            varUl.set('Izaberite')
            global ulice_optionmenu
            ulice_optionmenu=OptionMenu(Studenti,varUl,*ulicanaziv,command=lambda self='':[ifBrojExists2(),Broj(self)])
            ulice_optionmenu.grid(row=10,column=1)

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
            varBr=StringVar(Studenti)
            varBr.set('Izaberite')
            global broj_optionmenu
            broj_optionmenu=OptionMenu(Studenti,varBr,*brojevi)
            broj_optionmenu.grid(row=11,column=1)

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

            ### SVI STUDENTI ####
        def svistudenti():
            SviStudentiT=Toplevel()
            SviStudentiT.title('Svi studenti')
            SviStudentiT.geometry('600x600')

            cursor=conn.cursor()
            sql='SELECT * FROM Student'
            cursor.execute(sql)
            studenti0=''
            studenti1=''
            studenti2=''
            studenti3=''
            studenti4=''
            studenti5=''
            for row in cursor:
                studenti0 += str(row[0]) + "\n"
                studenti1 += str(row[1]) + "\n"
                studenti2 += str(row[2]) + "\n"
                studenti3 += str(row[3]) + "\n"
                studenti4 += str(row[4]) + "\n"
                studenti5 += str(row[5]) + "\n"
            
            #####
            studentid_label = Label (SviStudentiT,text='ID')
            studentid_label.grid(row=1,column=1)

            studentime_label = Label (SviStudentiT,text='Ime')
            studentime_label.grid(row=1,column=2)

            studentprezime_label = Label (SviStudentiT,text='Prezime')
            studentprezime_label.grid(row=1,column=3)

            studenttelefon_label = Label (SviStudentiT,text='Telefon')
            studenttelefon_label.grid(row=1,column=4)

            studentBOP_label = Label (SviStudentiT,text='BOP')
            studentBOP_label.grid(row=1,column=5)

            studentTR_label = Label (SviStudentiT,text='Tekuci racun')
            studentTR_label.grid(row=1,column=6)
            #######
            student0_label = Label(SviStudentiT,text=studenti0)
            student0_label.grid(row=2,column=1)

            student1_label = Label(SviStudentiT,text=studenti1)
            student1_label.grid(row=2,column=2)

            student2_label = Label(SviStudentiT,text=studenti2)
            student2_label.grid(row=2,column=3)

            student3_label = Label(SviStudentiT,text=studenti3)
            student3_label.grid(row=2,column=4)

            student4_label = Label(SviStudentiT,text=studenti4)
            student4_label.grid(row=2,column=5)

            student5_label = Label(SviStudentiT,text=studenti5)
            student5_label.grid(row=2,column=6)

            cursor2=conn.cursor()
            sql='SELECT * FROM StudentOstalo'
            cursor2.execute(sql)
            studentostalo=''
            for row in cursor2:
                studentostalo += str(row[1]) + "\n"

            studentostaloEmail=Label(SviStudentiT,text='Email')
            studentostaloEmail.grid(row=1,column=7)

            studentostaloL=Label(SviStudentiT,text=studentostalo)
            studentostaloL.grid(row=2,column=7)
        
        def pretragaStudent():
            cursor=conn.cursor()
            sql='SELECT * FROM Student_View WHERE Ime=?'
            val=pretraga_entry.get()
            cursor.execute(sql,val)
            print_cursor=''
            for row in cursor:
                print_cursor += str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]) + "\n"
            if not print_cursor:
                global pretraga_student_empty
                pretraga_student_empty=Label(Studenti,text='Nije pronadjen ni jedan student')
                pretraga_student_empty.grid(row=18,column=1)
            else:
                global pretraga_student
                pretraga_student=Label(Studenti,text=print_cursor)
                pretraga_student.grid(row=18,column=1)

        def destroyPretraga():
            try:
                pretraga_student_empty.destroy()
            except Exception:
                pass
            else:
                pass
            try:
                pretraga_student.destroy()
            except Exception:
                pass
            else:
                pass
        
        #### INSERT STUDENT ######
        def insertStudent():
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

                if entry_ime.get()=='' :
                    ime=tuple(entry_ime.get())
                    messagebox.showerror(title='Neispravno ime',message='Unesite ime')
                else:
                    ime=entry_ime.get()

                if entry_prezime.get()=='' :
                    prezime=tuple(entry_prezime.get())
                    messagebox.showerror(title='Neispravno prezime',message='Unesite prezime')
                else:
                    prezime=entry_prezime.get()

            
                cursorInsert=conn.cursor()
                sqlInsert='INSERT INTO Student_View (ID,Ime,Prezime,Telefon,BOP,TekuciRacun,Email,DrzavaID,GradID,OpstinaID,UlicaID,BrojID) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)'
                vInsert=(entry_id.get(),ime,prezime,entry_telefon.get(),entry_bop.get(),entry_tr.get(),entry_email.get(),DrzavaID,GradID,OpstinaID,UlicaID,BrojID)
                cursorInsert.execute(sqlInsert,vInsert)
                conn.commit()
            except Exception as e:
                messagebox.showerror(title='Neuspesno',message='Popunite sve polja ispravno'+"\n"+"\n"+str(e))
            else:
                messagebox.showinfo(title='Uspesno',message='Uspesno ste uneli studenta')

                entry_id.delete(0,END)
                entry_ime.delete(0,END)
                entry_prezime.delete(0,END)
                entry_telefon.delete(0,END)
                entry_bop.delete(0,END)
                entry_tr.delete(0,END)
                entry_email.delete(0,END)
            
            
        #####
        ##
        ##Drzava##
        cursor=conn.cursor()
        cursor.execute('SELECT Naziv FROM Drzava')
        print_cursor=[]
        for row in cursor:
            print_cursor += (row)
        global VarD
        VarD=StringVar(Studenti)
        VarD.set('Izaberite')

        drzava=OptionMenu(Studenti,VarD,*print_cursor,command=lambda self='':[ifGradExists2(),Grad(self)])
        drzava.grid(row=7,column=1)

        drzavalabel=Label(Studenti,text='Izaberite drzavu')
        drzavalabel.grid(row=7,column=0)


        ##Grad pre ###
        varG=StringVar(Studenti)
        varG.set('Izaberite prvo drzavu')
        optionsG=''
        global grad
        grad=OptionMenu(Studenti,varG,'',*optionsG)
        grad.grid(row=8,column=1)
        grad.configure(state='disabled')
        global gradlabel
        gradlabel=Label(Studenti,text='Izaberite grad')
        gradlabel.grid(row=8,column=0)

        ##Opstina pre ###
        varO=StringVar(Studenti)
        varO.set('Izaberite prvo grad')
        optionsO=''
        global opstina
        opstina=OptionMenu(Studenti,varO,'',*optionsO)
        opstina.grid(row=9,column=1)
        opstina.configure(state='disabled')
        global opstinalabel
        opstinalabel=Label(Studenti,text='Izaberite opstinu')
        opstinalabel.grid(row=9,column=0)

        ##Ulica pre ###
        varU=StringVar(Studenti)
        varU.set('Izaberite prvo opstinu')
        optionsU=''
        global ulica
        ulica=OptionMenu(Studenti,varU,'',*optionsU)
        ulica.grid(row=10,column=1)
        ulica.configure(state='disabled')
        global ulicalabel
        ulicalabel=Label(Studenti,text='Izaberite ulicu')
        ulicalabel.grid(row=10,column=0)

        ##Broj pre ###
        varB=StringVar(Studenti)
        varB.set('Izaberite prvo ulicu')
        optionsB=''
        global broj
        broj=OptionMenu(Studenti,varB,'',*optionsB)
        broj.grid(row=11,column=1)
        broj.configure(state='disabled')
        global brojlabel
        brojlabel=Label(Studenti,text='Izaberite broj')
        brojlabel.grid(row=11,column=0)

#######################################################################################################################################################
        ### STUDENT SELECT - EDIT ############
        def StudentSelect():
            StudentSelect=Toplevel()
            StudentSelect.title('Student')
            StudentSelect.geometry('800x600')
            ###
            
            cursorCheck=conn.cursor()
            sql='select * from student_view where id=?'
            val=izaberitestudentaid.get()

            try:
                cursorCheck.execute(sql,val)
            except Exception:
                neispravanid=Label(StudentSelect,text='Neispravan ID')
                neispravanid.grid(row=0,column=0)
            else:
                pass

            print_cursor=''
            for row in cursorCheck:
               print_cursor= str(row[0])+str(row[1])
            

            if not print_cursor:
                nista=Label(StudentSelect,text='Nije pronadjen ni jedan student')
                nista.grid(row=0,column=0)
            else:
                def studentDelete():
                    cursor=conn.cursor()
                    sql='DELETE FROM Student_View WHERE ID=?'
                    val=izaberitestudentaid.get()
                    cursor.execute(sql,val)
                    conn.commit()
                    
                
                def popupDeleteStudent():
                    try:
                        studentDelete()
                    except Exception as e:
                        messagebox.showerror(title='Neuspesno',message=str(e))
                    else:
                        messagebox.showinfo(title='Uspesno',message='Uspesno ste obrisali studenta')


                
                cursorAdresa=conn.cursor()
                sqlAdresa='SELECT DrzavaID,GradID,OpstinaID,UlicaID,BrojID FROM StudentOstalo WHERE ID=?'
                valAdresa=izaberitestudentaid.get()
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

                drzavaNaziv=Label(StudentSelect,text='Naziv drzave:')
                drzavaNaziv.grid(row=9,column=0)

                drzavaNazivS=Entry(StudentSelect,width=30)
                drzavaNazivS.grid(row=9,column=1)
                drzavaNazivS.insert(0,drzavaNazivAdresa)
                #####
                cursorAdresaGrad=conn.cursor()
                sqlAdresaGrad='select naziv from grad where drzavaid=? and id=?'
                valAdresaGrad=(drzavaIdAdresa,gradIdAdresa)
                cursorAdresaGrad.execute(sqlAdresaGrad,valAdresaGrad)
                for row in cursorAdresaGrad:
                    gradNazivAdresa=row[0]

                gradNaziv=Label(StudentSelect,text='Naziv grada:')
                gradNaziv.grid(row=10,column=0)

                gradNazivS=Entry(StudentSelect,width=30)
                gradNazivS.grid(row=10,column=1)
                gradNazivS.insert(0,gradNazivAdresa)
                ####
                cursorAdresaOpstina=conn.cursor()
                sqlAdresaOpstina='select naziv from opstina where drzavaid=? and gradid=? and id=?'
                valAdresaOpstina=(drzavaIdAdresa,gradIdAdresa,opstinaIdAdresa)
                cursorAdresaOpstina.execute(sqlAdresaOpstina,valAdresaOpstina)
                for row in cursorAdresaOpstina:
                    opstinaNazivAdresa=row[0]

                opstinaNaziv=Label(StudentSelect,text='Naziv opstine:')
                opstinaNaziv.grid(row=11,column=0)

                opstinaNazivS=Entry(StudentSelect,width=30)
                opstinaNazivS.grid(row=11,column=1)
                opstinaNazivS.insert(0,opstinaNazivAdresa)
                ###
                cursorAdresaUlica=conn.cursor()
                sqlAdresaUlica='select naziv from Ulica where drzavaid=? and gradid=? and OpstinaId=? and id=?'
                valAdresaUlica=(drzavaIdAdresa,gradIdAdresa,opstinaIdAdresa,ulicaIdAdresa)
                cursorAdresaUlica.execute(sqlAdresaUlica,valAdresaUlica)
                for row in cursorAdresaUlica:
                    ulicaNazivAdresa=row[0]

                ulicaNaziv=Label(StudentSelect,text='Naziv ulice:')
                ulicaNaziv.grid(row=12,column=0)

                ulicaNazivS=Entry(StudentSelect,width=30)
                ulicaNazivS.grid(row=12,column=1)
                ulicaNazivS.insert(0,ulicaNazivAdresa)
                ###
                cursorAdresaBroj=conn.cursor()
                sqlAdresaBroj='SELECT BrojID From Broj where drzavaid=? and gradid=? and OpstinaId=? and ulicaid=? and brojid=?'
                valAdresaBroj=(drzavaIdAdresa,gradIdAdresa,opstinaIdAdresa,ulicaIdAdresa,brojIdAdresa)
                cursorAdresaBroj.execute(sqlAdresaBroj,valAdresaBroj)
                for row in cursorAdresaBroj:
                    brojAdresa=row[0]

                brojNaziv=Label(StudentSelect,text='Broj:')
                brojNaziv.grid(row=13,column=0)

                brojNazivS=Entry(StudentSelect,width=30)
                brojNazivS.grid(row=13,column=1)  
                brojNazivS.insert(0,brojAdresa)
               
                def studentUpdate():
                    
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
                    sql='UPDATE Student_View SET ID=?,Ime=?,Prezime=?,Telefon=?,BOP=?,TekuciRacun=?,Email=?,DrzavaID=?,GradID=?,OpstinaID=?,UlicaID=?,BrojID=? WHERE ID=?'
                    vals=(entry_id.get(),entry_ime.get(),entry_prezime.get(),entry_telefon.get(),entry_bop.get(),entry_tr.get(),entry_email.get(),didd,gidd,oidd,uidd,bidd,izaberitestudentaid.get())
                    cursor.execute(sql,vals)
                    conn.commit()
                    
                  

                def popupUpdateStudent():
                    try:
                        studentUpdate()
                    except Exception as e:
                        messagebox.showerror(title='Neuspesno',message='Popunite sve polja ispravno'+"\n"+"\n"+str(e))
                    else:
                        messagebox.showinfo(title='Uspesno',message='Uspesno ste izmenili studenta')

                def studentDestroy():
                    StudentSelect.destroy()

                ####
                studentTabela=Label(StudentSelect,text='Tabela Student:')
                studentTabela.grid(row=0,column=1)
                ###3
                idlab=Label(StudentSelect,text='Unesite ID:')
                idlab.grid(row=1,column=0)

                entry_id=Entry(StudentSelect,width=30)
                entry_id.grid(row=1,column=1)
                ##
                ime=Label(StudentSelect,text='Unesite ime:')
                ime.grid(row=2,column=0)

                entry_ime=Entry(StudentSelect,width=30)
                entry_ime.grid(row=2,column=1)
                ##
                prezime=Label(StudentSelect,text='Unesite prezime:')
                prezime.grid(row=3,column=0)

                entry_prezime=Entry(StudentSelect,width=30)
                entry_prezime.grid(row=3,column=1)
                ##
                telefon=Label(StudentSelect,text='Unesite broj telefona:')
                telefon.grid(row=4,column=0)

                entry_telefon=Entry(StudentSelect,width=30)
                entry_telefon.grid(row=4,column=1)
                ##
                bop=Label(StudentSelect,text='Unesite bop:')
                bop.grid(row=5,column=0)

                entry_bop=Entry(StudentSelect,width=30)
                entry_bop.grid(row=5,column=1)
                ##
                tr=Label(StudentSelect,text='Unesite broj tekuceg racuna:')
                tr.grid(row=6,column=0)

                entry_tr=Entry(StudentSelect,width=30)
                entry_tr.grid(row=6,column=1)
                ##
                studentOstaloTable=Label(StudentSelect,text='Tabela StudentOstalo:')
                studentOstaloTable.grid(row=7,column=1)
                ##
                ##
                email=Label(StudentSelect,text='Unesite email:')
                email.grid(row=8,column=0)

                entry_email=Entry(StudentSelect,width=30)
                entry_email.grid(row=8,column=1)
                ###
                izmeniteadresu=Label(StudentSelect,text='Izmenite adresu:')
                izmeniteadresu.grid(row=8,column=3)
                ####
                
                ###
                updateStudentButton=Button(StudentSelect,text='Izmenite Studenta',command=lambda:[popupUpdateStudent(),studentUpdate(),studentDestroy()])
                updateStudentButton.grid(row=14,column=1)
                
                deleteStudentButton=Button(StudentSelect,text='Obrisite studenta',command=lambda:[popupDeleteStudent(),studentDelete(),studentDestroy()])
                deleteStudentButton.grid(row=15,column=1)
                ###
                cursor=conn.cursor()
                sql='SELECT * FROM Student_View WHERE ID=?'
                val=izaberitestudentaid.get()
                cursor.execute(sql,val)
                for row in cursor:
                    entry_id.insert(0,row[0])
                    entry_ime.insert(0,row[1])
                    entry_prezime.insert(0,row[2])
                    entry_telefon.insert(0,row[3])
                    entry_bop.insert(0,row[4])
                    entry_tr.insert(0,row[5])
                    entry_email.insert(0,row[6])



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
                    varGrS=StringVar(StudentSelect)
                    varGrS.set('Izaberite')
                    global gradoviS_optionmenu
                    gradoviS_optionmenu=OptionMenu(StudentSelect,varGrS,*gradnaziv,command=lambda self='':[ifOpstinaExists2(),OpstinaS(self),gradE()])
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
                    varOpS=StringVar(StudentSelect)
                    varOpS.set('Izaberite')
                    global opstineS_optionmenu
                    opstineS_optionmenu=OptionMenu(StudentSelect,varOpS,*opstinanaziv,command=lambda self='':[ifUlicaExists2(),UlicaS(self),opstinaE()])
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
                    varUlS=StringVar(StudentSelect)
                    varUlS.set('Izaberite')
                    global uliceS_optionmenu
                    uliceS_optionmenu=OptionMenu(StudentSelect,varUlS,*ulicanaziv,command=lambda self='':[ifBrojExists2(),BrojS(self),ulicaE()])
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
                    varBrS=StringVar(StudentSelect)
                    varBrS.set('Izaberite')
                    global brojS_optionmenu
                    brojS_optionmenu=OptionMenu(StudentSelect,varBrS,*brojevi,command=brojE)
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
                sqlDS='SELECT DrzavaID FROM Student_View WHERE ID=?'
                valDS=izaberitestudentaid.get()
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
                VarD=StringVar(StudentSelect)
                VarD.set(str(DSNaziv))

                drzavaS=OptionMenu(StudentSelect,VarD,*print_cursor,command=lambda self='':[ifGradExists2(),GradS(self),drzavaE()])
                drzavaS.grid(row=9,column=3)
                drzavalabel=Label(StudentSelect,text='Izaberite drzavu')
                drzavalabel.grid(row=9,column=2)


                ####Grad pre u SELECT###
                cursorGS=conn.cursor()
                sqlGS='SELECT GradID FROM Student_View WHERE ID=?'
                valGS=izaberitestudentaid.get()
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

                varG=StringVar(StudentSelect)
                varG.set(str(GSNaziv))
                optionsG=''
                global gradSS
                gradSS=OptionMenu(StudentSelect,varG,'',*optionsG)
                gradSS.grid(row=10,column=3)
                gradSS.configure(state='disabled')
                global gradlabel
                gradlabel=Label(StudentSelect,text='Izaberite grad')
                gradlabel.grid(row=10,column=2)

                ##Opstina pre ###
                cursorOS=conn.cursor()
                sqlOS='SELECT OpstinaID FROM Student_View WHERE ID=?'
                valOS=izaberitestudentaid.get()
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

                varO=StringVar(StudentSelect)
                varO.set(str(OSNaziv))
                optionsO=''
                global opstinaSS
                opstinaSS=OptionMenu(StudentSelect,varO,'',*optionsO)
                opstinaSS.grid(row=11,column=3)
                opstinaSS.configure(state='disabled')
                global opstinalabel
                opstinalabel=Label(StudentSelect,text='Izaberite opstinu')
                opstinalabel.grid(row=11,column=2)

                ##Ulica pre ###
                cursorUS=conn.cursor()
                sqlUS='SELECT UlicaID FROM Student_View WHERE ID=?'
                valUS=izaberitestudentaid.get()
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


                varU=StringVar(StudentSelect)
                varU.set(str(USNaziv))
                optionsU=''
                global ulicaSS
                ulicaSS=OptionMenu(StudentSelect,varU,'',*optionsU)
                ulicaSS.grid(row=12,column=3)
                ulicaSS.configure(state='disabled')
                global ulicalabel
                ulicalabel=Label(StudentSelect,text='Izaberite ulicu')
                ulicalabel.grid(row=12,column=2)

                ##Broj pre ###
                cursorBS=conn.cursor()
                sqlBS='SELECT BrojID FROM Student_View WHERE ID=?'
                valBS=izaberitestudentaid.get()
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

                varB=StringVar(StudentSelect)
                varB.set(str(BSNaziv))
                optionsB=''
                global brojSS
                brojSS=OptionMenu(StudentSelect,varB,'',*optionsB)
                brojSS.grid(row=13,column=3)
                brojSS.configure(state='disabled')
                global brojlabel
                brojlabel=Label(StudentSelect,text='Izaberite broj')
                brojlabel.grid(row=13,column=2)



            ##### STUDENT SELECT - EDIT CLOSED ############

#######################################################################################################################################################
        ####
        idlab=Label(Studenti,text='Unesite ID:')
        idlab.grid(row=0,column=0)

        entry_id=Entry(Studenti,width=30)
        entry_id.grid(row=0,column=1)
        ##
        ime=Label(Studenti,text='Unesite ime:')
        ime.grid(row=1,column=0)

        entry_ime=Entry(Studenti,width=30)
        entry_ime.grid(row=1,column=1)
        ##
        prezime=Label(Studenti,text='Unesite prezime:')
        prezime.grid(row=2,column=0)

        entry_prezime=Entry(Studenti,width=30)
        entry_prezime.grid(row=2,column=1)
        ##
        telefon=Label(Studenti,text='Unesite broj telefona:')
        telefon.grid(row=3,column=0)

        entry_telefon=Entry(Studenti,width=30)
        entry_telefon.grid(row=3,column=1)
        ##
        bop=Label(Studenti,text='Unesite bop:')
        bop.grid(row=4,column=0)

        entry_bop=Entry(Studenti,width=30)
        entry_bop.grid(row=4,column=1)
        ##
        tr=Label(Studenti,text='Unesite broj tekuceg racuna:')
        tr.grid(row=5,column=0)

        entry_tr=Entry(Studenti,width=30)
        entry_tr.grid(row=5,column=1)
        ##
        email=Label(Studenti,text='Unesite email:')
        email.grid(row=6,column=0)

        entry_email=Entry(Studenti,width=30)
        entry_email.grid(row=6,column=1)
        ##
        insert=Button(Studenti,text='Unesite studenta',command=insertStudent)
        insert.grid(row=12,column=1)
        
        izaberitestudenta=Label(Studenti,text='Izaberite studenta po ID-u')
        izaberitestudenta.grid(row=13,column=0)
        
        izaberitestudentaid=Entry(Studenti,width=30)
        izaberitestudentaid.grid(row=13,column=1)
        ##
        
        izaberite_button=Button(Studenti,text='Izaberite studenta',command=StudentSelect)
        izaberite_button.grid(row=14,column=1)
        ##
        pretraga=Label(Studenti,text='Pretrazite studente po imenu')
        pretraga.grid(row=15,column=0)

        pretraga_entry=Entry(Studenti,width=30)
        pretraga_entry.grid(row=15,column=1)
        ##
        pretraga_button=Button(Studenti,text='Pretrazite',command=lambda:[destroyPretraga(),pretragaStudent()])
        pretraga_button.grid(row=16,column=1)
        ##
        svistudent=Button(Studenti,text='Prikazite sve studente',command=svistudenti)
        svistudent.grid(row=17,column=1)


        
        
