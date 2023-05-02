from tkinter import*
from tkinter.ttk import Treeview

class Visualizacion():
    def ventanaPrincipal(self):
        ventana=Tk()
        ventana.title("Login")
        # Este es el tamaño de la ventana principal
        ventana.geometry("500x500+500+50")
        pantllaColor="#081118"

        # Esto sirve para que la pantalla no se achique ni se agrende ni se encoja, que quede con el tamaño que le dimos 
        ventana.resizable(width=False,height=False)


        #colores

        fondo_entrar ="#00fcf1"
        fondo_salir = "#00fcf1"

        usuario=StringVar()
        password=StringVar()

        pantalla=Frame(ventana,bg=pantllaColor ,width=500,height=500)
        pantalla.pack()





        def login():
            # ESTE ES EL LOGIN INICIAL DONDE EL USUARIO PUEDE INGRESAR
            # SUS RESPECTIVAS CONTRASEÑAS ESTAN AQUI 
            nombre=usuario.get()
            contraseña=password.get()
            if nombre=="cata" and contraseña=="1":
                Call_Center()
            elif nombre=="juan" and contraseña=="2":
                administrador()
            
            elif nombre=="victor" and contraseña=="3":
                chef()

            
            else:
                incorrecto=Label(ventana,text=" Usuario o contraseña incorrecta",fg="red",background=pantllaColor,font=("calibri",13))
                incorrecto.place(x=140,y=280)

        # AQUI ESTA TODODEL CALL CENTER SI SE NECESITA MODIFICAR ALGO SE HACE AQUI
        # DENTRO DEL DEF EN NINGUN LADO MAS 
        def Call_Center():
            # destruir la ventana padre
            ventana.destroy()
            
            # crear la nueva ventana hija
            window=Tk()
            
            window.title("Usuario")
            window.geometry("500x500+500+50")
            window.configure(background=pantllaColor)
            window.resizable(width=False,height=False)
            Label(window,text="CALL-CENTER",font=20,pady=10,background=pantllaColor,foreground="#00fcf1").pack()
            
            

            marco=LabelFrame(window,pady=40,padx=130,background=pantllaColor,foreground="#00fcf1")
            marco.place(x=5,y=40)

            
            # Nombre
            Label(marco,text="Nombre",font=16,pady=10,background=pantllaColor,foreground="#00fcf1").grid(row=0,column=1)
            nomEntry=Entry(marco,bg=pantllaColor,foreground="#00fcee",font=("calibri",10))
            nomEntry.grid(row=0,column=2)
            nomEntry.configure(highlightthickness=2, highlightbackground="#00fcee")
            # clave
            Label(marco,text="Clave",font=16,pady=10,background=pantllaColor,foreground="#00fcf1").grid(row=1,column=1)
            claEntry=Entry(marco,bg=pantllaColor,foreground="#00fcee",font=("calibri",10))
            claEntry.grid(row=1,column=2)
            claEntry.configure(highlightthickness=2, highlightbackground="#00fcee")

            #Boton
            # sticky=W+E abarcar todo el ancho desde el este al oeste
            Button(marco,text="Actualizar",width=10).place(x=0,y=95)
            Button(marco,text="Eliminar",width=10).place(x=90 ,y=95)
            Button(marco,text="ver menu",width=10).place(x=270,y=95)
            #Tblaaaaaaaaaaaaaaaaa-----------------------------------------------------------------------------------------------
            # Ojo tenemos que areglar la tabla ya que tiene algunas inperfecciones
            tabla=Treeview(window)
            tabla["column"]=("ID","Nombre","Apellido","Edad","awdawd","nada")
            #Definir tamaño
            tabla.column(column="#0",width=10)
            tabla.column(column="ID",width=70)
            tabla.column(column="Nombre",width=70)
            tabla.column(column="Apellido",width=70)
            tabla.column(column="Edad",width=70)
            tabla.column(column="awdawd",width=70)
            tabla.column(column="nada",width=70)
            
        
            tabla.heading(column="#0",text="")
            tabla.heading(column="ID",text="ID")
            tabla.heading(column="Nombre",text="Nombre")
            tabla.heading(column="Apellido",text="Apellido")
            tabla.heading(column="Edad",text="Edad")
            tabla.heading(column="awdawd",text="awdawd")
            tabla.heading(column="nada",text="nada")
            tabla.pack()
            tabla.place(x=35,y=250)
           


            def salirCall():
                window.destroy()
            # agregar los widgets a la nueva ventana hija
            boton3=Button(marco,text="salir",command=salirCall,cursor="hand2",width=10)
            boton3.place(x=180,y=95)
            
            window.mainloop()
        # ------------------------------------------------------------------------------------------------------
         # AQUI ESTA TODO_DEL administrador SI SE NECESITA MODIFICAR ALGO SE HACE AQUI
        # DENTRO DEL DEF EN NINGUN LADO MAS 
        def administrador():
            ventana.destroy()
            
            # crear la nueva ventana hija
            window2=Tk()
            
            window2.title("Usuario")
            window2.geometry("500x500+500+50")
            window2.configure(background=pantllaColor)
            window2.resizable(width=False,height=False)
            Label(window2,text="Administrador",font=20,pady=10,background=pantllaColor,foreground="#00fcf1").pack()

         # AQUI ESTA TODO_DEL CHEF SI SE NECESITA MODIFICAR ALGO SE HACE AQUI
        # DENTRO DEL DEF EN NINGUN LADO MAS 
        def chef():
            ventana.destroy()
            # crear la nueva ventana hija
            window2=Tk()
            window2.title("Usuario")
            window2.geometry("500x500+500+50")
            window2.configure(background=pantllaColor)
            window2.resizable(width=False,height=False)
            Label(window2,text="Chef",font=20,pady=10,background=pantllaColor,foreground="#00fcf1").pack()
            def salirPrograma():
                window2.destroy()
            # --------------------------------------------------------------------------------------------------------------
            # boton Menu.

            def menuChef():
            # crear la nueva ventana hija
                window2.destroy()
                ventanMenu=Tk()
                ventanMenu.title("Usuario")
                ventanMenu.geometry("500x500+500+50")
                ventanMenu.configure(background=pantllaColor)
                ventanMenu.resizable(width=False,height=False)
                Label(ventanMenu,text="Chef",font=20,pady=10,background=pantllaColor,foreground="#00fcf1").pack()
                tabla=Treeview(ventanMenu)
                tabla["column"]=("ID","Nombre","Apellido","Edad","awdawd","nada")
                #Definir tamaño
                tabla.column(column="#0",width=10)
                tabla.column(column="ID",width=70)
                tabla.column(column="Nombre",width=70)
                tabla.column(column="Apellido",width=70)
                tabla.column(column="Edad",width=70)
                tabla.column(column="awdawd",width=70)
                tabla.column(column="nada",width=70)
                
            
                tabla.heading(column="#0",text="")
                tabla.heading(column="ID",text="valor")
                tabla.heading(column="Nombre",text="precio")
                tabla.heading(column="Apellido",text="precio")
                tabla.heading(column="Edad",text="precio")
                tabla.heading(column="awdawd",text="precio")
                tabla.heading(column="nada",text="precio")
                tabla.pack()
                # tabla.place(x=35,y=250)
                def salirPrograma():
                    ventanMenu.destroy()
                botonSalir=Button(ventanMenu,text="Salir",command=salirPrograma,cursor="hand2",width=10)
                botonSalir.place(x=310,y=405)
                ventanMenu.mainloop()

            botonMenu=Button(window2,text="Menu",command=menuChef,cursor="hand2",width=10)
            botonMenu.place(x=0,y=0)
             # -------------------------------------------------------------------------------------------------------------- 
             #  boton actualizar. 
            def actualizar():
                window2.destroy()
                ventanActualizar=Tk()
                ventanActualizar.title("Usuario")
                ventanActualizar.geometry("500x500+500+50")
                ventanActualizar.configure(background=pantllaColor)
                ventanActualizar.resizable(width=False,height=False)
                Label(ventanActualizar,text="Chef",font=20,pady=10,background=pantllaColor,foreground="#00fcf1").pack()
                def salirPrograma():
                    ventanActualizar.destroy()
                botonSalir=Button(ventanActualizar,text="Salir",command=salirPrograma,cursor="hand2",width=10)
                botonSalir.place(x=310,y=405)
                ventanActualizar.mainloop()

            botonMenu=Button(window2,text="Actualizar",command=actualizar,cursor="hand2",width=10)
            botonMenu.place(x=0,y=100)
            #-------------------------------------------------------------------------------------------------------------
             #  boton actualizar. 
            def actualizar():
                window2.destroy()
                ventanActualizar=Tk()
                ventanActualizar.title("Usuario")
                ventanActualizar.geometry("500x500+500+50")
                ventanActualizar.configure(background=pantllaColor)
                ventanActualizar.resizable(width=False,height=False)
                Label(ventanActualizar,text="Chef",font=20,pady=10,background=pantllaColor,foreground="#00fcf1").pack()
                def salirPrograma():
                    ventanActualizar.destroy()
                botonSalir=Button(ventanActualizar,text="Salir",command=salirPrograma,cursor="hand2",width=10)
                botonSalir.place(x=310,y=405)
                ventanActualizar.mainloop()

            botonactu=Button(window2,text="Actualizar",command=actualizar,cursor="hand2",width=10)
            botonactu.place(x=0,y=100)
            #-------------------------------------------------------------------------------------------------------------
            #  boton nose que poner aqui. 
            def actualizar():
                window2.destroy()
                ventananose=Tk()
                ventananose.title("Usuario")
                ventananose.geometry("500x500+500+50")
                ventananose.configure(background=pantllaColor)
                ventananose.resizable(width=False,height=False)
                Label(ventananose,text="Chef",font=20,pady=10,background=pantllaColor,foreground="#00fcf1").pack()
                def salirPrograma():
                    ventananose.destroy()
                botonSalir=Button(ventananose,text="Salir",command=salirPrograma,cursor="hand2",width=10)
                botonSalir.place(x=310,y=405)
                ventananose.mainloop()

            botonNose=Button(window2,text="nose",command=actualizar,cursor="hand2",width=10)
            botonNose.place(x=0,y=200)

            window2.mainloop()

            
            



 

        # TODO_ESTO PARA ABAJO ES DE LA VENTANA PRINCIPAL OJO SE TIENE QUE AREGLAR 
        # ALGUNAS COSAS YA QUE ESTAN DISPAREJAS(NO ESTAN RECTAS).
        # TODOLO lo  QUE QUERAMOS A SER, LO TENEMOS QUE CAMBIAR AQUI
        # En este apartado basicamente va todo lo visual de la pagina principal 
        inciarSeccion=Label(ventana,text="INICIAR SESSION",font=("Tahoma",20,"bold"),bg=pantllaColor,foreground="#00fcee")
        inciarSeccion.place(x=155,y=40)

        usuariotext=Label(ventana,text="Usuario",font=16,bg=pantllaColor,foreground="#00fcee")
        usuariotext.place(x=210,y=110)

        entrada1=Entry(ventana, textvar=usuario, width=22, relief="flat", bg=pantllaColor, foreground="#00fcee",font=("calibri",10))
        entrada1.configure(highlightthickness=2, highlightbackground="#00fcee")
        entrada1.place(x=180,y=150)

        paswordtxt=Label(ventana,text="Password",font=16,bg=pantllaColor,foreground="#00fcee")
        paswordtxt.place(x=200,y=190)

        entrada2=Entry(ventana,textvar=password,show="•",width=22,relief="flat",bg=pantllaColor,foreground="#00fcee",font=("calibri",10))
        entrada2.configure(highlightthickness=2, highlightbackground="#00fcee")
        entrada2.place(x=180,y=230)



        def salir():
            ventana.destroy()
            



#Botones,el cursor va a cambiar a una mano
        boton1=Button(ventana,text="Entrar",command=login,cursor="hand2",bg=fondo_entrar,width=12,relief="raised",
                    font=("Calibre",12,"bold")) 
        #Ubicacion del lugar del boton es esta boton.place(x=60,y=405)
        boton1.place(x=60,y=405)

        boton2=Button(ventana,text="salir",command=salir,cursor="hand2",bg=fondo_salir,width=12,relief="raised",
                    font=("Calibre",12,"bold")) 

        boton2.place(x=310,y=405)

        ventana.mainloop()






