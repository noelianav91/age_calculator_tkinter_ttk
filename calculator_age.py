from cgitb import text
from tkinter import ttk
from tkinter import *
from tkcalendar import DateEntry
import datetime,locale

locale.setlocale(locale.LC_ALL,("es_ES"))




class main():
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora de edad")
        self.ventana.geometry("600x500")
        self.ventana.resizable(0,0)
        self.ventana.config(bd=15)
        self.ventana.configure(background="gray91")
        estilos = ttk.Style()
        estilos.configure('mainframe.TFrame',background="Gray91")
        estilos.theme_use("clam")
        mainframe = ttk.Frame(ventana,style="mainframe.TFrame")

    
    #datos entrada
        Label(ventana,text="Fecha de nacimiento", bg='gray91', fg='black', font=('Arial 13 bold')).place(x=135, y=10)
        self.birth_fecha =DateEntry(ventana,width=10)
        self.birth_fecha.place(x=135,y=40)
        Label(ventana,text="Fecha Actual", bg='gray91', fg='black', font=('Arial 13 bold')).place(x=340, y=10)
        self.actual_fecha = DateEntry(ventana,width=10)
        self.actual_fecha.place(x=340,y=40)


    # Estilos botón calcular
        estilos_boton = ttk.Style()
        estilos_boton.configure('Botones.TButton',font="arial 15",width=5,
                                      background="gray40",foreground="white",relief="GROOVE")
    # Botón calcular edad
        ttk.Button(ventana,style='Botones.TButton',text="Calcular edad",command=self.calcular).place(x=150,y=100,width=260)

    # Creamos un frame principal para los resultados
        result_frame = Frame(ventana, bg='gray84')
        result_frame.place(x=10, y=150, width=550, height=310)

    # Creamos un frame secundario para la edad
        frame1 = Frame(result_frame,bg='gray84', bd=1, relief=GROOVE)
        frame1.place(x=0, y=0, width=275, height=150)
        Label(frame1,text="Edad",bg='gray84', fg='black', font=('Arial 18 bold')).place(x=10, y=10)
        self.total_year = Label(frame1,text="00",bg='gray84', fg='dim gray', font=('Arial 30 bold'))
        self.total_year.place(x=55, y=45)
        Label(frame1,text="Años",bg='gray84', fg='black', font=('Arial 15 bold')).place(x=90, y=59)
        self.total_meses = Label(frame1,text="00",bg='gray84', fg='dim gray', font=('Arial 20 bold'))
        self.total_meses.place(x=33,y=93)
        Label(frame1,text="meses, y",bg='gray84', fg='black', font=('Arial 15 bold')).place(x=60, y=98)
        self.total_dias = Label(frame1,text="00",bg='gray84', fg='dim gray', font=('Arial 20 bold'))
        self.total_dias.place(x=132,y=93)
        Label(frame1,text="días",bg='gray84', fg='black', font=('Arial 15 bold')).place(x=160, y=98)
    
    # Creamos un frame secundario para el proximo cumpleaños
        frame2 = Frame(result_frame,bg='gray84', bd=1, relief=GROOVE)
        frame2.place(x=275, y=0, width=275, height=150)
        Label(frame2,text="Próximo cumpleaños",bg='gray84', fg='black', font=('Arial 18 bold')).place(x=10, y=10)
        self.proximo_birth = Label(frame2,text="",bg='gray84', fg='black', font=('Arial 20 bold'))
        self.proximo_birth.place(x=95, y=45)
        self.meses = Label(frame2,text="00",bg='gray84', fg='dim gray', font=('Arial 20 bold'))
        self.meses.place(x=40, y=90)
        Label(frame2,text="meses, y",bg='gray84', fg='black', font=('Arial 15 bold')).place(x=70, y=95)
        self.next_dias = Label(frame2,text="00",bg='gray84', fg='dim gray', font=('Arial 20 bold'))
        self.next_dias.place(x=140,y=90)
        Label(frame2,text="días",bg='gray84', fg='black', font=('Arial 15 bold')).place(x=170, y=95)
    
    # Creamos un frame secundario para el general
        frame3 = Frame(result_frame,bg='gray84', bd=1, relief=GROOVE)
        frame3.place(x=0, y=150, width=550, height=160)
        Label(frame3,text="General",bg='gray84', fg='black', font=('Arial 18 bold')).place(x=225, y=10)
        Label(frame3, text="Años", bg='gray84', fg='black', font=('Arial 15')).place(x=140, y=40)
        self.general_year = Label(frame3,text="00",bg='gray84',fg='black',font=('Arial 15'))
        self.general_year.place(x=145, y=65)
        Label(frame3, text="Meses", bg='gray84', fg='black', font=('Arial 15')).place(x=220, y=40)
        self.general_meses = Label(frame3,text="00",bg='gray84',fg='black',font=('Arial 15'))
        self.general_meses.place(x=230, y=65)
        Label(frame3, text="Semanas", bg='gray84', fg='black', font=('Arial 15')).place(x=310, y=40)
        self.general_semana = Label(frame3,text="00",bg='gray84',fg='black',font=('Arial 15'))
        self.general_semana.place(x=320, y=65)
        Label(frame3, text="Días", bg='gray84', fg='black', font=('Arial 15')).place(x=140, y=95)
        self.general_dias = Label(frame3,text="00",bg='gray84',fg='black',font=('Arial 15'))
        self.general_dias.place(x=135, y=115)
        Label(frame3, text="Horas", bg='gray84', fg='black', font=('Arial 15')).place(x=220, y=95)
        self.general_horas = Label(frame3,text="00",bg='gray84',fg='black',font=('Arial 15'))
        self.general_horas.place(x=220, y=115)
        Label(frame3, text="Minutos", bg='gray84', fg='black', font=('Arial 15')).place(x=310, y=95)
        self.general_minutos = Label(frame3,text="00",bg='gray84',fg='black',font=('Arial 15'))
        self.general_minutos.place(x=310, y=115)

    def calcular (self):
        now = datetime.datetime.now()
        actual = self.actual_fecha.get_date()
        birth = self.birth_fecha.get_date()
       
        fecha_actual = datetime.datetime.strptime(str(actual), '%Y-%m-%d')
        fecha_birth = datetime.datetime.strptime(str(birth), '%Y-%m-%d')

        prox_birth_1 = datetime.datetime(fecha_actual.year,fecha_birth.month,fecha_birth.day)
        prox_birth_2 = datetime.datetime(fecha_actual.year+1,fecha_birth.month,fecha_birth.day)
        prox_birth = prox_birth_1 if prox_birth_1 > now else prox_birth_2
        
        dias_siguiente = prox_birth - fecha_actual 
        dias_restantes = fecha_actual - fecha_birth

        years = ((dias_restantes.total_seconds())/(365.242*24*3600))
        years_init = int(years)
        meses = (years - years_init)*12
        meses_int = int(meses)
        dias = (meses-meses_int)*(365.242/12)
        dias_int = int(dias)
        horas = (dias-dias_int)*24
        horas_int = int(horas)
        minutos = (horas-horas_int)*60
        minutos_int = int(minutos)
        
    #Configuraión de los datos del primer frame
        self.total_year.config(text=years_init)
        self.total_meses.config(text=meses_int)
        self.total_dias.config(text=dias_int)
        
    #Configuración de los datos del segundo frame  
        self.proximo_birth.config(text=prox_birth.strftime("%A"))
        self.meses.config(text=dias_siguiente.days//30)
        self.next_dias.config(text=dias_restantes.days%30)

    #Configuración de los datos del tercer frame
        self.general_year.config(text=years_init)
        self.general_meses.config(text=meses_int*12+meses_int)
        self.general_semana.config(text=dias_restantes.days//7)
        self.general_dias.config(text=dias_restantes.days)
        self.general_horas.config(text=dias_restantes.days*24)
        self.general_minutos.config(text=int(dias_restantes.total_seconds()//60))














ventana = Tk()
obj = main(ventana)
mainloop()

        