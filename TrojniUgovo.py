from tkinter import *
from tkinter import messagebox
import pyodbc


conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-RIM8T9PN;"
    "Database=BOX;"
    "Trusted_Connection=yes;"
)

class TrojniUgovorClass():
    def TrojniUgovor():
        TrojniUgovor=Toplevel()
        TrojniUgovor.title('Trojni ugovor')
        TrojniUgovor.geometry('600x600')
        ####
        def plataZaPosao(self):
            cursor5=conn.cursor()
            sql5='SELECT * FROM Posao WHERE Naziv=? and NazivPoslodavca=?'
            val5=(varPosao.get(),varPs.get())
            cursor5.execute(sql5,val5)

            for row in cursor5:
                plata=row[7]

                if not plata:
                    plata_entry.config(text='Nije uneta plata za izabrani posao')
                else:
                    plata_entry.config(text=str(plata))

        ###
        def Posao(self):
            preposlodavca.destroy()
            cursor=conn.cursor()
            sql='SELECT Naziv FROM Posao WHERE NazivPoslodavca=?'
            val=varPs.get()
            cursor.execute(sql,val)
            posaonaziv=[]
            posaonaziv2=''
            global varPosao
            varPosao=StringVar(TrojniUgovor)

            posaonaziv=[]
            posaonaziv2=''
            for row in cursor:
                posaonaziv +=row
                posaonaziv2=str(row[0])
                varPosao.set('Izaberite')
            
            if not posaonaziv2:
                plata_entry.config(text='Niste izabrali posao')
                global nema_label
                nema_label=Label(TrojniUgovor,text='Nema poslova za izabranog poslodavca')
                nema_label.grid(row=4,column=1)
            else:
                global posao_op
                posao_op=OptionMenu(TrojniUgovor,varPosao,*posaonaziv,command=lambda self='':[plataZaPosao(self)])
                posao_op.grid(row=4,column=1)

        def posaoBrisanje():
            try:
                nema_label.destroy()
            except Exception:
                pass
            else:
                pass
            try:
                posao_op.destroy()
            except Exception:
                pass
            else:
                pass  

        def insertTU():
            try:
                cursor=conn.cursor()
                sql='SELECT * FROM Posao WHERE Naziv=? and NazivPoslodavca=?'
                val=(varPosao.get(),varPs.get())
                cursor.execute(sql,val)
                for row in cursor:
                   KategorijaID=row[0]
                   PodkategorijaID=row[1]
                   RadnoMestoID=row[2]

                cursor2=conn.cursor()
                sql2='SELECT ID FROM Poslodavac WHERE Naziv=?'
                val2=varPs.get()
                cursor2.execute(sql2,val2)
                for row in cursor2:
                    PoslodavacID=row[0]

                cursor3=conn.cursor()
                sql3='SELECT ID FROM Student WHERE ID=?'
                val3=varSt.get().split(' ')
                studentID=val3[0]
                cursor3.execute(sql3,studentID)
                for row in cursor3:
                    StudentID=row[0]

                studentInfo=varSt.get().split(' ')
                studentImeInfo=studentInfo[1]
                studentPrezimeInfo=studentInfo[2]
                zadrugaNaziv='BOX'
                poslodavacNaziv=varPs.get()
                posaoNaziv=varPosao.get()
                info=str(studentImeInfo) + "," + str(studentPrezimeInfo) + "," + str(zadrugaNaziv) + "," + str(poslodavacNaziv) + "," + str(posaoNaziv)

                cursor4=conn.cursor()
                sql4='INSERT INTO TrojniUgovor(ID,ZadrugaID,StudentID,PoslodavacID,KategorijaID,PodkategorijaID,RadnoMestoID,PlataIznos,DatumOD,DatumDO,Info) VALUES (?,?,?,?,?,?,?,?,?,?,?) '
                val4=(trojiugovorID_entry.get(),1,StudentID,PoslodavacID,KategorijaID,PodkategorijaID,RadnoMestoID,plata_entry.cget('text'),datumOd_entry.get(),datumDo_entry.get(),info)
                cursor4.execute(sql4,val4)
                conn.commit()
            except Exception as e:
                messagebox.showerror(title='Neuspesno',message='Popunite sve polja ispravno'+"\n"+"\n"+str(e))
            else:
                messagebox.showinfo(title='Uspesno',message='Uspesno ste uneli trojni ugovor')

                trojiugovorID_entry.delete(0,END)
                datumOd_entry.delete(0,END)
                datumDo_entry.delete(0,END)

        def sviTU():
            SviTu=Toplevel()
            SviTu.title('Svi trojni ugovori')
            SviTu.geometry('800x600')

            cursor=conn.cursor()
            sql='SELECT * FROM TrojniUgovor'
            cursor.execute(sql)
            global idTU
            global infoImeTU
            global infoPrezimeTU
            global infoZadrugaTU
            global infoPoslodavacTU
            global infoPosaoTU
            global infoPlata
            global infoDatumOd
            global infoDatumDo
            idTU=''
            infoTU=''
            infoImeTU=''
            infoPrezimeTU=''
            infoZadrugaTU=''
            infoPoslodavacTU=''
            infoPosaoTU=''
            infoPlata=''
            infoDatumOd=''
            infoDatumDo=''
            for row in cursor:
                idTU += str(row[0]) + "\n"
                infoTU=str(row[10]).split(',')
                infoImeTU += str(infoTU[0]) + "\n"
                infoPrezimeTU += str(infoTU[1]) + "\n"
                infoZadrugaTU += str(infoTU[2]) + "\n"
                infoPoslodavacTU += str(infoTU[3]) + "\n"
                infoPosaoTU += str(infoTU[4]) + "\n"
                infoPlata += str(row[7]) + "\n"
                infoDatumOd += str(row[8]) + "\n"
                infoDatumDo += str(row[9]) + "\n"


            #######
            idTU_label=Label(SviTu,text='ID')
            idTU_label.grid(row=1,column=1)
            
            iddTU=Label(SviTu,text=idTU)
            iddTU.grid(row=2,column=1)
            ####
            ime=Label(SviTu,text='Ime')
            ime.grid(row=1,column=2)

            imee=Label(SviTu,text=infoImeTU)
            imee.grid(row=2,column=2)
            ###
            prezime=Label(SviTu,text='Prezime')
            prezime.grid(row=1,column=3)

            prezimee=Label(SviTu,text=infoPrezimeTU)
            prezimee.grid(row=2,column=3)
            ###
            zadruga=Label(SviTu,text='Zadruga')
            zadruga.grid(row=1,column=4)

            zadrugaa=Label(SviTu,text=infoZadrugaTU)
            zadrugaa.grid(row=2,column=4)
            ###
            poslodavac=Label(SviTu,text='Poslodavac')
            poslodavac.grid(row=1,column=5)

            poslodavacc=Label(SviTu,text=infoPoslodavacTU)
            poslodavacc.grid(row=2,column=5)
            ####
            posao=Label(SviTu,text='Posao')
            posao.grid(row=1,column=6)

            posaoo=Label(SviTu,text=infoPosaoTU)
            posaoo.grid(row=2,column=6)
            ####
            plata=Label(SviTu,text='Plata')
            plata.grid(row=1,column=7)

            plataa=Label(SviTu,text=infoPlata)
            plataa.grid(row=2,column=7)
            ###
            datumOd_label=Label(SviTu,text='Datum od')
            datumOd_label.grid(row=1,column=8)

            datumOdd_label=Label(SviTu,text=infoDatumOd)
            datumOdd_label.grid(row=2,column=8)
            ####
            datumDo_label=Label(SviTu,text='Datum do')
            datumDo_label.grid(row=1,column=9)

            datumDoo_label=Label(SviTu,text=infoDatumDo)
            datumDoo_label.grid(row=2,column=9)

        def selectTU():
            SelectTU=Toplevel()
            SelectTU.title('Trojni ugovor')
            SelectTU.geometry('600x600')

            cursor=conn.cursor()
            sql='SELECT * FROM TrojniUgovor WHERE ID=?'
            val=selectTU_entry.get()
            try:
                cursor.execute(sql,val)
            except Exception:
                neispravno=Label(SelectTU,text='Neispravno unet ID')
                neispravno.grid(row=0,column=0)
            else:
                pass
            
            global idTUS
            global infoImeTUS
            global infoPrezimeTUS
            global infoZadrugaTUS
            global infoPoslodavacTUS
            global infoPosaoTUS
            global infoPlataS
            global infoDatumOdS
            global infoDatumDoS
            idTUS=''
            infoTUS=''
            infoImeTUS=''
            infoPrezimeTUS=''
            infoZadrugaTUS=''
            infoPoslodavacTUS=''
            infoPosaoTUS=''
            infoPlataS=''
            infoDatumOdS=''
            infoDatumDoS=''
            for row in cursor:
                idTUS = str(row[0]) 
                infoTUS=str(row[10]).split(',')
                infoImeTUS = str(infoTUS[0]) 
                infoPrezimeTUS = str(infoTUS[1]) 
                infoZadrugaTUS = str(infoTUS[2]) 
                infoPoslodavacTUS = str(infoTUS[3]) 
                infoPosaoTUS = str(infoTUS[4]) 
                infoPlataS = str(row[7]) 
                infoDatumOdS = str(row[8]) 
                infoDatumDoS = str(row[9]) 

            if not idTUS:
                nema=Label(SelectTU,text='Nije pronadjen ni jedan trojni ugovor')
                nema.grid(row=0,column=0)
            else:
                #######
                idTU_label=Label(SelectTU,text='ID')
                idTU_label.grid(row=1,column=1)

                iddTU=Label(SelectTU,text=idTUS)
                iddTU.grid(row=1,column=2)

                kolonaid=Label(SelectTU,text='Kolona ID')
                kolonaid.grid(row=1,column=0)
                ####
                ime=Label(SelectTU,text='Ime')
                ime.grid(row=2,column=1)

                imee=Label(SelectTU,text=infoImeTUS)
                imee.grid(row=2,column=2)

                kolonainfo1=Label(SelectTU,text='Kolona Info')
                kolonainfo1.grid(row=2,column=0)
                ###
                prezime=Label(SelectTU,text='Prezime')
                prezime.grid(row=3,column=1)

                prezimee=Label(SelectTU,text=infoPrezimeTUS)
                prezimee.grid(row=3,column=2)

                kolonainfo2=Label(SelectTU,text='Kolona Info')
                kolonainfo2.grid(row=3,column=0)
                ###
                zadruga=Label(SelectTU,text='Zadruga')
                zadruga.grid(row=4,column=1)

                zadrugaa=Label(SelectTU,text=infoZadrugaTUS)
                zadrugaa.grid(row=4,column=2)

                kolonainfo3=Label(SelectTU,text='Kolona Info')
                kolonainfo3.grid(row=4,column=0)
                ###
                poslodavac=Label(SelectTU,text='Poslodavac')
                poslodavac.grid(row=5,column=1)

                poslodavacc=Label(SelectTU,text=infoPoslodavacTUS)
                poslodavacc.grid(row=5,column=2)

                kolonainfo4=Label(SelectTU,text='Kolona Info')
                kolonainfo4.grid(row=5,column=0)
                ####
                posao=Label(SelectTU,text='Posao')
                posao.grid(row=6,column=1)

                posaoo=Label(SelectTU,text=infoPosaoTUS)
                posaoo.grid(row=6,column=2)

                kolonainfo5=Label(SelectTU,text='Kolona Info')
                kolonainfo5.grid(row=6,column=0)
                ####
                plata=Label(SelectTU,text='Plata')
                plata.grid(row=7,column=1)

                plataa=Label(SelectTU,text=infoPlataS)
                plataa.grid(row=7,column=2)

                kolonaplata=Label(SelectTU,text='Kolona plata')
                kolonaplata.grid(row=7,column=0)
                ###
                datumOd_label=Label(SelectTU,text='Datum od')
                datumOd_label.grid(row=8,column=1)
                global datumOdd_entry
                datumOdd_entry=Entry(SelectTU,width=30)
                datumOdd_entry.grid(row=8,column=2)
                datumOdd_entry.insert(0,infoDatumOdS)
                #datumOdd_label=Label(SelectTU,text=infoDatumOdS)
                #datumOdd_label.grid(row=8,column=2)

                kolonaDatumOd=Label(SelectTU,text='Kolona DatumOD')
                kolonaDatumOd.grid(row=8,column=0)
                ####
                datumDo_label=Label(SelectTU,text='Datum do')
                datumDo_label.grid(row=9,column=1)
                global datumDoo_entry
                datumDoo_entry=Entry(SelectTU,width=30)
                datumDoo_entry.grid(row=9,column=2)
                datumDoo_entry.insert(0,infoDatumDoS)
                #datumDoo_label=Label(SelectTU,text=infoDatumDoS)
                #datumDoo_label.grid(row=9,column=2)

                kolonaDatumDo=Label(SelectTU,text='Kolona DatumDo')
                kolonaDatumDo.grid(row=9,column=0)
                #####
                def updateTU():
                    try:
                        cursor=conn.cursor()
                        sql='UPDATE TrojniUgovor SET DatumOD=?,DatumDO=? WHERE ID=?'
                        val=(datumOdd_entry.get(),datumDoo_entry.get(),selectTU_entry.get())
                        cursor.execute(sql,val)
                        conn.commit()
                    except Exception as e:
                        messagebox.showerror(title='Neuspesno',message='Popunite sva polja ispravno'+"\n"+"\n"+str(e))
                    else:
                        messagebox.showinfo(title='Uspesno',message='Uspesno ste obrisali trojni ugovor')
                        SelectTU.destroy()

                updateBtn=Button(SelectTU,text='Update trojni ugovor',command=updateTU)
                updateBtn.grid(row=10,column=2)
                ####                    
                def deleteTU():
                    try:
                        cursor=conn.cursor()
                        sql='DELETE FROM TrojniUgovor WHERE ID=?'
                        val=selectTU_entry.get()
                        cursor.execute(sql,val)
                        conn.commit()
                    except Exception as e:
                        messagebox.showerror(title='Neuspesno',message=str(e))
                    else:
                        messagebox.showinfo(title='Uspesno',message='Uspesno ste obrisali trojni ugovor')
                        SelectTU.destroy()
                
                deleteBtn=Button(SelectTU,text='Obrisite trojni ugovor',command=deleteTU)
                deleteBtn.grid(row=11,column=2)

        ###
        trojniugovorID=Label(TrojniUgovor,text='Unesite ID za trojni ugovor')
        trojniugovorID.grid(row=0,column=0)
        global trojiugovorID_entry
        trojiugovorID_entry=Entry(TrojniUgovor,width=30)
        trojiugovorID_entry.grid(row=0,column=1)
        ##
        cursor=conn.cursor()
        sql='SELECT Naziv From Zadruga WHERE ID=1'
        cursor.execute(sql)
        global naziv
        naziv=''
        for row in cursor:
            naziv=str(row[0])

        trojniugovorZadrugaID=Label(TrojniUgovor,text='Studentska zadruga')
        trojniugovorZadrugaID.grid(row=1,column=0)

        trojiugovorZadrugaID_label=Label(TrojniUgovor,text=naziv)
        trojiugovorZadrugaID_label.grid(row=1,column=1)
        ###
        cursor2=conn.cursor()
        sql2='SELECT * FROM Student'
        cursor2.execute(sql2)
        student=''
        student2=[]
        for row in cursor2:
            student = (str(row[0]) + " " + str(row[1]) + " " + str(row[2]))
            student2 += [student]

        studenti_label=Label(TrojniUgovor,text='Izaberite studenta')
        studenti_label.grid(row=2,column=0)    
        global varSt
        varSt=StringVar(TrojniUgovor)
        varSt.set('Izaberite')
        global studenti
        studenti=OptionMenu(TrojniUgovor,varSt,*student2)
        studenti.grid(row=2,column=1)
        ####
        cursor3=conn.cursor()
        sql3='SELECT Naziv FROM Poslodavac'
        cursor3.execute(sql3)
        poslodavacc=[]
        for row in cursor3:
            poslodavacc += (row)

        poslodavac=Label(TrojniUgovor,text='Izaberite poslodavca')
        poslodavac.grid(row=3,column=0)
        global varPs
        varPs=StringVar(TrojniUgovor)
        varPs.set('Izaberite')
        global poslodavci
        poslodavci=OptionMenu(TrojniUgovor,varPs,*poslodavacc,command=lambda self='':[posaoBrisanje(),Posao(self)])
        poslodavci.grid(row=3,column=1)
        ###
        global varPre
        varPre=StringVar(TrojniUgovor)
        varPre.set('Izaberite prvo poslodavca')
        options=''
        global preposlodavca
        preposlodavca=OptionMenu(TrojniUgovor,varPre,'',*options)
        preposlodavca.grid(row=4,column=1)
        preposlodavca.configure(state='disabled')
        ###
        izaberiteposao=Label(TrojniUgovor,text='Izaberite radno mesto')
        izaberiteposao.grid(row=4,column=0)

        ####Plata label###
        plata_label=Label(TrojniUgovor,text='Plata')
        plata_label.grid(row=5,column=0)
        global plata_entry
        plata_entry=Label(TrojniUgovor,text='Niste izabrali posao')
        plata_entry.grid(row=5,column=1)
        ###

        datumOd=Label(TrojniUgovor,text='Datum od')
        datumOd.grid(row=6,column=0)
        
        datumOd_entry=Entry(TrojniUgovor,width=30)
        datumOd_entry.grid(row=6,column=1)
        ##
        datumDo=Label(TrojniUgovor,text='Datum do')
        datumDo.grid(row=7,column=0)

        datumDo_entry=Entry(TrojniUgovor,width=30)
        datumDo_entry.grid(row=7,column=1)
        ##
        insert=Button(TrojniUgovor,text='Unesite trojni ugovor',command=insertTU)
        insert.grid(row=8,column=1)
        ###
        selectTU_label=Label(TrojniUgovor,text='Izaberite trojni ugovor po ID-u')
        selectTU_label.grid(row=9,column=0)

        selectTU_entry=Entry(TrojniUgovor,width=30)
        selectTU_entry.grid(row=9,column=1)

        selectTU_button=Button(TrojniUgovor,text='Izaberite',command=selectTU)
        selectTU_button.grid(row=10,column=1)
        ###
        selectSveTU=Button(TrojniUgovor,text='Prikazite sve trojne ugovore',command=sviTU)
        selectSveTU.grid(row=11,column=1)








