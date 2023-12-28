# AQUI IMPORTAMOS LIBRERIAS PARA  OCUPARLA EN NUESTRO CODIGO COMO IMPLEMENTACION
from tkinter import *
from tkinter.ttk import Treeview
from ttkthemes import (
    ThemedStyle,
)  # ESTE ES UNA BIBLOTECA QUE LE DA EL ESTILO A LAS TABLAS QUE ESTAN EN EL MARCO

import hashlib#hashlib es una biblioteca estándar de Python que
# proporciona funcionalidades para realizar operaciones de hashing criptográfico.

# Estas son las importaciones de cada uno de los Archivos y sus clases que estan compuestas, dentro de cada uno de los archivos 
from Bebidas import Bebidas
from comida import Comida
from pedidos import Pedidos
from postres import Postres
from usurios import Usuario
usu = Usuario()
pedido = Pedidos()
postre = Postres()
comida = Comida()
bebida = Bebidas()
# La clase Visualizacion es el padre de todos sin el todo se pierde es una de las clases mas importantes
class Visualizacion:
    def ventanaPrincipal(self):
        # La sintaxis def ventanaPrincipal(self) es un metodo de la clase
        # Ahora porque es tan importante el self
        
        # EL "self" se utiliza para referirse al objeto que se está creando a partir de la clase "Visualizacion".Esto se encuentra
        # En el documento Programa.py
        # Es como decir: "Este objeto de visualización quiere realizar una acción". ("Esto sale en la Linea 5 del rpograma ")

        # Cuando defines un método dentro de la clase, necesitas poner "self" como el primer parámetro del
        # método. Esto ayuda al método a saber
        # qué objeto está llamando al método y permite acceder a las
        # características y realizar acciones en ese objeto específico.

        # Por ejemplo, si el método
        # "ventanaPrincipal" quisiera mostrar el contenido de la primera página del libro,
        # necesitaría saber a qué libro se refiere. El "self" te ayuda a hacer eso, ya que se refiere al
        # objeto de la clase "Visualizacion" que está llamando al método.
        ventana = Tk()
        ventana.title("Login")
        # Este es el tamaño de la ventana principal
        #  ventana.geometry("1000x550") es lo mismo que poner ventana.geometry("500x500+500+50")
        #                                                                       Ancho*alto*ancho*alto
        # ESto es la cantidad de espacio que tendra la ventana
        ventana.geometry("500x500+500+50")

        pantllaColor = "#081118"
        # pantllaColor es el color que tendra el marco y otros elemento que estan estan en las  funciones
        #  y estan representados en hecxadecimal

        # Esto sirve para que la pantalla no se achique ni se agrende ni se encoja, que quede con el tamaño que le dimos
        ventana.resizable(width=False, height=False)
        # aqui van las variables que almacenen los colores y QUE IRAN EN CADA UNA DE LAS CACILLAS QUE
        # ESTAN ABAJAO ES DECIR LAS VENTANAS QUE SE CREA TENDRAN UNA VARIABLE QUE ALMACENARA  ESTA VARAIBLE DE COLORES
        fondo_entrar = "#00fcf1"
        fondo_salir = "#00fcf1"

        # Esto lo que hace es crear un marco que tendra todo el ancho  y largo de nuestro pantalla
        pantalla = Frame(ventana, bg=pantllaColor, width=500 + 500, height=500 + 50)
        pantalla.pack()
        # Esto es una funcion que esta abajo y  le pertenece a un boton que esta al principio que tiene
        # Como texto
        def logiin():
                nombre = entrada1.get()
                contraseña = entrada2.get()
                encriptada = hashlib.md5(contraseña.encode()).hexdigest()
                usu.usuario = nombre
                usu.contraseña = encriptada
                resultado = usu.login()
                if resultado != None:
                    # Realiza las acciones correspondientes al inicio e sesión exitoso
                    if usu.tipo_usu_id == 3:
                        Call_Center()
                    elif usu.tipo_usu_id == 2 :
                        chef()
                    elif usu.tipo_usu_id == 1 :
                        administrador()
                    return

            # Si todo es incorrecto nos arrojara un texto " Usuario o contraseña incorrecta"
            # place(lugar)es donde se mostrara el texto en rojo
                else:
                    incorrecto = Label(
                        ventana,
                        text=" Usuario o contraseña incorrecta",
                        fg="red",
                        background=pantllaColor,
                        font=("cSalibri", 13),
                    )
                    incorrecto.place(x=140, y=280)

# -----------------------------------------------------------------------------------------------------------------------------------------
        # CALL CENTER
        # CALL CENTER
        def Call_Center():
            # destruir la ventana padre  ventanaPrincipal y como esta dentro es mucho mas facil de encontrar
            ventana.destroy()

            # Esta funcion construir_ventana_principal() nos permite construir una ventaan 
            def construir_ventana_principal():
                global tablita  # Declarar las variables globales tablita y ventanaCallCenter
                global ventanaCallCenter
                ventanaCallCenter = Tk()  # Crear una nueva ventana llamada ventanaCallCenter
                ventanaCallCenter.title("Usuario")  # Establecer el título de la ventana
                ventanaCallCenter.geometry("700x500+500+50")  # Establecer las dimensiones y posición de la ventana
                ventanaCallCenter.configure(background=pantllaColor)  # Establecer el color de fondo de la ventana
                ventanaCallCenter.resizable(width=False, height=False)  # Hacer que la ventana no sea redimensionable

                Label(
                    ventanaCallCenter,
                    text="CALL-CENTER",
                    font=30,
                    background=pantllaColor,
                    foreground="#00fcf1",
                ).pack()  # Crear una etiqueta para mostrar el título del call-center

                Label(
                    ventanaCallCenter,
                    text="MENU",
                    font=60,
                    background=pantllaColor,
                    foreground="#00fcf1",
                ).pack()  # Crear una etiqueta para mostrar el título del menú

                def salirCall():
                    ventanaCallCenter.destroy()  # Cerrar la ventanaCallCenter al llamar a la función destroy()

                BotonCerrarProgram = Button(
                    ventanaCallCenter,
                    font=("Calibre", 10),
                    text="Cerrar programa",
                    command=salirCall,
                    cursor="hand2",
                    width=14,
                )
                BotonCerrarProgram.place(x=540, y=440)  # Crear un botón para cerrar el programa

                BotonVerPedido = Button(
                    ventanaCallCenter,
                    font=("Calibre", 10),
                    text="Ver pedidos",
                    width=10,
                    command=mostrar_ventana_secundaria,
                    cursor="hand2",
                )
                BotonVerPedido.place(x=410, y=330)  # Crear un botón para ver los pedidos

                DtosComiadas = comida.CargarComida()  # Cargar los datos de comidas

                DatosBebidas = bebida.CargarBebidas()  # Cargar los datos de bebidas

                DatosPostres = postre.CargarPostres()  # Cargar los datos de postres

                # Encabezados de comida.

                encabezadosComidas = (
                    "id",  # ID de la comida
                    "nombre",  # Nombre de la comida
                    "precio",  # Precio de la comida
                    "tamaño",  # Tamaño de la comida
                    "ingredientes",  # Ingredientes de la comida
                    "disponibilidad",  # Disponibilidad de la comida
                )

                encabezadosBebidas = (
                    "id",  # ID de la bebida
                    "nombre",  # Nombre de la bebida
                    "precio",  # Precio de la bebida
                    "tamaño",  # Tamaño de la bebida
                    "disponibilidad",  # Disponibilidad de la bebida
                )

                encabezadosPostres = (
                    "id",  # ID del postre
                    "nombre",  # Nombre del postre
                    "precio",  # Precio del postre
                    "tamaño",  # Tamaño del postre
                    "ingredientes",  # Ingredientes del postre
                    "disponibilidad",  # Disponibilidad del postre
                )

                # Aqui dse definen los anchos que tendran las  cacillas de los encabezados.
                anchos_Comidas = [
                    100,
                    400,
                    200,
                    200,
                    650,
                    100,
                ]  # Anchura personalizada para cada columna en la tabla

                anchos_Bebidas = [
                    100,
                    200,
                    200,
                    200,
                    100,
                ]  # Anchura personalizada para cada columna en la tabla

                anchos_Postres = [
                    100,
                    300,
                    200,
                    200,
                    500,
                    100,
                ]  # Anchura personalizada para cada columna en la tabla

                # -------------------------------------------------------------------------------------------------------------------------
                # Aqui se crea un marco dentro de la ventana principal utilizando la clase Frame
                marco = Frame(ventanaCallCenter)

                marco.pack(
                    side=TOP, pady=10
                )  # Establecer la posición del marco con un relleno de 0 píxeles en el eje x y 10 píxeles en el eje y

                # -----------------------------------------------------------------------------------------------------------------------
                # Crear Scrollbar(Barra de desplazamiento) horizontal personalizado que estara dentro del marco
                scroll_horizontal = Scrollbar(marco, orient=HORIZONTAL)
                scroll_horizontal.pack(side=BOTTOM, fill=X)
                # -----------------------------------------------------------------------------------------------------------------------
                # Se define una variable tabla para almacenar la tabla actual.
                # Inicialmente se establece como None.
                # Luego cuando tenemos ya la tabla inicial este none ya no esta vacio si no ahora es un objeto
                tablita = None
                def crear_tabla(datos, encabezados, anchos_columnas):
                    global tablita
                    # Global nos permite que la variable que afuera tenga las mismas propiedades
                    # en el nombre que esta acompaño de el, es decir tabla
                    # Pejor ojo
                    # En Python, cuando se define una variable dentro de una función, por defecto esa
                    # variable se considera local a la función y no se puede acceder a ella desde fuera
                    # de la función. Si deseas acceder a una variable
                    # global dentro de una función y también permitir que la función modifique esa variable global,
                    # debes utilizar la declaración global para indicar que la variable es global.

                    # En el caso de tablita, se declara como una variable global en
                    # ambos lugares porque se utiliza tanto en la función construir_ventana_principal()
                    # como en la función crear_tabla(). Al declararla como global en ambas funciones, puedes acceder
                    # y modificar la misma variable global desde ambas funciones, asegurando que se mantenga actualizada en todo el programa.
                    if tablita != None:
                        tablita.destroy()
                    # al utilizar xscrollcommand=scroll_horizontal.set, se vincula la barra
                    # de desplazamiento horizontal con la tabla, lo que permite que la tabla se desplace horizontalmente cuando se mueve la barra.
                    tablita = Treeview(
                        marco, show="headings", xscrollcommand=scroll_horizontal.set
                    )
                    # tablita["columns"] es la forma de acceder a la lista de nombres de las columnas de un objeto Treeview en Tkinter
                    # columns es una propiedad que esta almacenda en la clase Treeview y nos permite acceder a las columnas de la tabla
                    # ,mediante su clave el cual es columns,como tabla es un objeto podemos acceder mediante su clave  y darle  valores
                    tablita["columns"] = encabezados
                    estilo = ThemedStyle(marco)
                    # Traemos a la clase  ThemedStyle que es parte de la libreria ttkthemes
                    # Ahora estilo es un objeto y en el podemos acceder facilmente a su propiedades  pero ojo esta anclado o pertenece
                    # Ya al marco por ende podemmos agregarele deiferentes funcionalidades

                    estilo.set_theme("scidgrey")  # Establecer el tema clam
                    # Ahora como estilo esta anclado a el marco donde si ubica nuestra tabla podemos darle diferentes propiedades para poder
                    # crear diferentes estilos

                    # configura las propiedades del estilo para el Treeview con la etiqueta "Custom.Treeview".
                    estilo.configure(
                        "Custom.Treeview",
                        background="#081118",  # Negro para el fondo de las celdas
                        foreground="#FFFFFF",  # Color del texto de las celdas
                        fieldbackground="#081118",  # Negro para el fondo de los campos
                        font=("Roboto", 10),  # Fuente del texto
                        bordercolor="#1E1E1E",  # Color del borde
                        selectbackground="#2979FF",  # Color de fondo de la selección
                        selectforeground="",  # Color del texto de la selección
                    )
                    estilo.configure(
                        "Custom.Treeview.Heading",
                        background="#1E1E1E",  # Color de fondo del encabezado
                        foreground="#081118",  # Color del texto del encabezado
                        font=("Roboto", 9, "bold"),  # Fuente del texto del encabezado
                    )
                    # Aplica el estilo "Custom.Treeview" al la tablita, que es el Treeview que se desea personalizar.
                    tablita.configure(style="Custom.Treeview")
                    tablita.tag_configure(
                        "Custom.Treeview.Heading",
                        background="#212121",
                        foreground="#081118",
                    )
                    # -----------------------------------------------------------------------------------------------------------------------
                    DatosTabla = zip(
                        tablita["columns"], encabezados, anchos_columnas
                    )  # zip lo que hace es agrupar  las listas
                    #  combina los elementos correspondientes
                    # de cada lista en tuplas, formando una secuencia de tuplas.
                    # Cada tupla contendrá un elemento de cada lista en el mismo orden luego se crea una listas con las tuplas credas
                    # Un ejemplito puede ser este:
                    # tabla["columns"] = ["Nombre", "Edad", "País"]
                    # encabezados = ["Nombres", "Years", "Country"]
                    # anchos_columnas = [100, 80, 120]
                    # Luego si utilizamos el zip quedarian asi
                    # [("Nombre", "apellido", 100), ("Edad", "Years", 80), ("País", "Country", 120)]
                    # ahora siguiendo con nuestro explicacion
                    # Ahora como estan agrupados, podemos recorrerlas sin problema
                    for columna, encabezado, ancho in DatosTabla:
                        # Ahora ocupando    el ejemplo anterior, el bucle se ejecutaría tres veces, una vez para cada tupla.
                        # En la primera iteración, columna tendría el valor "Nombre", encabezado tendría el valor "Nombres" y ancho tendría el
                        # valor 100. Luego se llamaría a tabla.column("Nombre", width=100) y tabla.heading("Nombre", text="Nombres", anchor=CENTER)
                        # Y SE LE ENTREGARA SUS RESPECTIVOS VALORES
                        # stretch lo que hace es estirar las cacillas de las cabeceras
                        tablita.column(columna, width=ancho, stretch=False)
                        tablita.heading(columna, text=encabezado, anchor=CENTER)

                    for dato in datos:
                        # Incorrporar iid=dato[0] para los id de oracle despues
                        tablita.insert("", END, values=dato)
                        # Al proporcionar "", indicamos que la fila se agregará al
                        #  nivel superior, es decir, no tendrá un elemento padre específico.
                        # END: Es el índice de posición en el que se va a insertar
                        # la fila. Al proporcionar END, la fila se añadirá al final de la tabla.

                    # Aqui lo que hacemos es
                    tablita.pack(
                        side=LEFT, fill=Y
                    )  # Alinear la tabla a la izquierda y rellenar en el eje Y

                    # se están realizando configuraciones para establecer la
                    # conexión entre la barra de desplazamiento horizontal y la tabla.
                    scroll_horizontal.config(command=tablita.xview)
                    tablita.config(xscrollcommand=scroll_horizontal.set)

                # Este es la primera tabla y le entegamos los datos que esta arriba y se va a la funcion a crearce
                crear_tabla(DtosComiadas, encabezadosComidas, anchos_Comidas)

                # La expresión lambda en este código se utiliza para definir una
                # función anónima que se ejecutará cuando se haga clic en el botón
                # y su función es llamar a la función crear_tabla con los argumentos proporcionados, lo mismo con el de abajo solo que tiene
                # diferentes argumentos de datos .
                BotonBebidas = Button(
                    ventanaCallCenter,
                    font=("Calibre", 11),
                    text="Bebidas",
                    cursor="hand2",
                    command=lambda: crear_tabla(
                        DatosBebidas, encabezadosBebidas, anchos_Bebidas
                    ),
                )

                BotonBebidas.place(x=110, y=330)

                # Crear botón para mostrar la tabla de comidas
                BotonComida = Button(
                    ventanaCallCenter,
                    font=("Calibre", 11),
                    cursor="hand2",
                    text="Comida",
                    command=lambda: crear_tabla(DtosComiadas, encabezadosComidas, anchos_Comidas),
                )
                BotonComida.place(x=200, y=330)

                # Crear botón para mostrar la tabla de postres
                BotonPostres = Button(
                    ventanaCallCenter,
                    cursor="hand2",
                    text="Postres",
                    font=("Calibre", 10),
                    width=10,
                    command=lambda: crear_tabla(DatosPostres, encabezadosPostres, anchos_Postres),
                )
                BotonPostres.place(x=290, y=330)

                # Nos permite darle incio a la ventana ventanaCallCenter
                ventanaCallCenter.mainloop()

            def VerPedidos():
                global ventanaPedido
                ventanaPedido = Tk()
                ventanaPedido.title("Usuario")
                ventanaPedido.geometry("700x500+500+50")
                ventanaPedido.configure(background=pantllaColor)
                ventanaPedido.resizable(width=False, height=False)

                # Etiqueta para el título "PEDIDOS"
                Label(
                    ventanaPedido,
                    text="PEDIDOS",
                    font=30,
                    background=pantllaColor,
                    foreground="#00fcf1",
                ).pack()

                # Etiqueta para "Eliminar pedido"
                Label(
                    ventanaPedido,
                    text="Eliminar pedido",
                    font=30,
                    background=pantllaColor,
                    foreground="#00fcf1",
                ).place(x=290, y=40)

                def CaputarIDBorrar():
                    # Obtener el ID ingresado en la caja de texto
                    ID = CajaBorrarID.get()

                    if ID.isdigit():  # Verificar si el ID es un número entero
                        pedido.id = ID
                        pedido.EliminarPedido()  # Eliminar el pedido correspondiente al ID
                        ventanaPedido.destroy()
                        VerPedidos()  # Actualizar la ventana para mostrar los pedidos actualizados
                    elif ID == "":
                        mensaje.config(text="Por favor, ingrese un ID válido.")
                    else:
                        mensaje.config(text="Error. Por favor, ingrese un ID numérico válido.")
                        CajaBorrarID.delete(0, END)
                    return

                # Etiqueta para mostrar mensajes
                mensaje = Label(
                    ventanaPedido,
                    background=pantllaColor,
                    foreground="#00fcf1",
                    fg="red"
                )
                mensaje.place(x=270, y=105)


                # Etiqueta "ID" para indicar el campo de entrada del ID
                Label(
                    ventanaPedido,
                    text="ID:",
                    font=5,
                    pady=10,
                    background=pantllaColor,
                    foreground="#00fcf1",
                ).place(x=250, y=60)

                # Caja de entrada para el ID del pedido a borrar
                CajaBorrarID = Entry(
                    ventanaPedido,
                    bg=pantllaColor,
                    foreground="#00fcee",
                    font=("calibri", 10),
                )
                CajaBorrarID.place(x=290, y=74)

                # Botón "Retroceder" para regresar a la ventana anterior
                BotonRetroceder = Button(
                    ventanaPedido,
                    text="Retroceder",
                    width=10,
                    command=ocultar_ventana_secundaria,
                    cursor="hand2",
                )
                BotonRetroceder.place(x=435, y=140)

                # Botón "Borrar" para eliminar el pedido con el ID ingresado
                BotonBorrarID = Button(
                    ventanaPedido,
                    text="Borrar🗑",
                    width=10,
                    cursor="hand2",
                    command=CaputarIDBorrar,
                )
                BotonBorrarID.place(x=245, y=140)

                def CrearPedido():
                    ventanaPedido.destroy()
                    def CrearPedido1():
                        global ventanaCrearPedido
                        ventanaCrearPedido = Tk()
                        ventanaCrearPedido.geometry("700x500+500+50")
                        ventanaCrearPedido.title("CREAR")

                        ventanaCrearPedido.configure(background=pantllaColor)
                        ventanaCrearPedido.resizable(width=False, height=False)
                        Label(
                            ventanaCrearPedido,
                            text="CREAR PEDIDOS",
                            font=30,
                            background=pantllaColor,
                            foreground="#00fcf1",
                        ).pack()
                        # esta funcion nos permite capturar los datos dentro de los entry
                        def Pedidoscapturados():
                            #
                            comida.id = ComidaEntry.get()
                            bebida.id = BebidaEntry.get()
                            postre.id = PostreEntry.get()
                            cantidad_comida = CantidadComidaEntry.get()
                            cantidad_bebida = CantidadBebidaEntry.get()
                            cantidad_postre = CantidadPostreEntry.get()

                            if(cantidad_comida.isdigit()   and cantidad_bebida.isdigit() 
                                 and cantidad_postre.isdigit() and comida.id.isdigit() 
                                 and bebida.id.isdigit() and postre.id.isdigit() ):
                                
                                comida.ComidaTotal()
                                pedido.comidas = comida.nombre
                                bebida.BebidaTotal()
                                pedido.bebidas = bebida.nombre
                                postre.PostresTotal()
                                pedido.postres = postre.nombre
                                
                                if(comida.disponibilidad == 1 and bebida.disponibilidad == 1 and postre.disponibilidad == 1):
                                    pedido.total = (comida.precio * int(cantidad_comida)) + (bebida.precio * int(cantidad_bebida)) + (postre.precio * int(cantidad_postre))
                                    pedido.cantidad_de_comida = cantidad_comida
                                    pedido.cantidad_de_bebidas = cantidad_bebida
                                    pedido.cantidad_de_postres = cantidad_postre
                                    pedido.CrearPedido()

                                    ventanaCrearPedido.destroy()
                                    CrearPedido1()
                                else:
                                    mensajeCrearPedido.config(text="Ingrese datos disponibles.")

                            elif (
                                comida == ""
                                or bebida == ""
                                or postre == ""
                                or cantidad_comida == ""
                                or cantidad_bebida == ""
                                or cantidad_postre==""
                            ):
                                mensajeCrearPedido.config(text="Por favor, completa todos los campos.")
                                return
                            
                            else:
                                mensajeCrearPedido.config(
                                    text="Porfavor,ingrese valores numéricos")
                                CantidadComidaEntry.delete(0, END)
                                CantidadBebidaEntry.delete(0, END)
                                CantidadPostreEntry.delete(0, END)
                                ComidaEntry.delete(0, END)
                                BebidaEntry.delete(0, END)
                                PostreEntry.delete(0, END)
                                return

                        mensajeCrearPedido = Label(
                            ventanaCrearPedido,
                            background=pantllaColor,
                            foreground="#00fcf1",
                            fg="red")
                        mensajeCrearPedido.place(x=135, y=460)


                        # Creación de la etiqueta "ID de comida"
                        Label(
                            ventanaCrearPedido,
                            text="ID de comida:",  # Texto de la etiqueta
                            font=5,  # Fuente de la etiqueta
                            pady=10,  # Espacio interno vertical
                            background=pantllaColor,  # Color de fondo de la etiqueta
                            foreground="#00fcf1",  # Color de texto de la etiqueta
                        ).place(x=60, y=50)  # Posicionamiento de la etiqueta en la ventana

                        # Creación del campo de entrada para el ID de comida
                        ComidaEntry = Entry(
                            ventanaCrearPedido,
                            bg=pantllaColor,  # Color de fondo del campo de entrada
                            foreground="#00fcee",  # Color de texto del campo de entrada
                            font=("calibri", 10),  # Fuente del campo de entrada
                        )
                        ComidaEntry.place(x=230, y=64)  # Posicionamiento del campo de entrada en la ventana
                        ComidaEntry.configure(
                            highlightthickness=2, highlightbackground="#00fcee"
                        )  # Configuración del resaltado del campo de entrada

                        # Creación de la etiqueta "ID de bebida" (similar a la etiqueta "ID de comida")
                        Label(
                            ventanaCrearPedido,
                            text="ID de Bebida:",
                            font=5,
                            pady=10,
                            background=pantllaColor,
                            foreground="#00fcf1",
                        ).place(x=60, y=90)

                        # Creación del campo de entrada para el ID de bebida (similar al campo de entrada para el ID de comida)
                        BebidaEntry = Entry(
                            ventanaCrearPedido,
                            bg=pantllaColor,
                            foreground="#00fcee",
                            font=("calibri", 10),
                        )
                        BebidaEntry.place(x=230, y=104)
                        BebidaEntry.configure(
                            highlightthickness=2, highlightbackground="#00fcee"
                        )

                        # Creación de la etiqueta "ID de postre" (similar a la etiqueta "ID de comida")
                        Label(
                            ventanaCrearPedido,
                            text="ID de Postre:",
                            font=5,
                            pady=10,
                            background=pantllaColor,
                            foreground="#00fcf1",
                        ).place(x=60, y=130)

                        # Creación del campo de entrada para el ID de postre (similar al campo de entrada para el ID de comida)
                        PostreEntry = Entry(
                            ventanaCrearPedido,
                            bg=pantllaColor,
                            foreground="#00fcee",
                            font=("calibri", 10),
                        )
                        PostreEntry.place(x=230, y=144)
                        PostreEntry.configure(
                            highlightthickness=2, highlightbackground="#00fcee"
                        )

                        # Creación de la etiqueta "Cantidad" (similar a la etiqueta "ID de comida")
                        Label(
                            ventanaCrearPedido,
                            text="Cantidad:",
                            font=5,
                            pady=10,
                            background=pantllaColor,
                            foreground="#00fcf1",
                        ).place(x=470, y=20)

                        # Creación del campo de entrada para la cantidad de comida (similar al campo de entrada para el ID de comida)
                        CantidadComidaEntry = Entry(
                            ventanaCrearPedido,
                            bg=pantllaColor,
                            foreground="#00fcee",
                            font=("calibri", 10),
                        )
                        CantidadComidaEntry.place(x=470, y=64)
                        CantidadComidaEntry.configure(
                            highlightthickness=2, highlightbackground="#00fcee"
                        )

                        # Creación del campo de entrada para la cantidad de bebida (similar al campo de entrada para el ID de comida)
                        CantidadBebidaEntry = Entry(
                            ventanaCrearPedido,
                            bg=pantllaColor,
                            foreground="#00fcee",
                            font=("calibri", 10),
                        )
                        CantidadBebidaEntry.place(x=470, y=104)
                        CantidadBebidaEntry.configure(
                            highlightthickness=2, highlightbackground="#00fcee"
                        )


                        # Creación del campo de entrada para la cantidad de postre (similar al campo de entrada para el ID de comida)
                        CantidadPostreEntry = Entry(
                            ventanaCrearPedido,
                            bg=pantllaColor,
                            foreground="#00fcee",
                            font=("calibri", 10),
                        )
                        CantidadPostreEntry.place(x=470, y=144)
                        CantidadPostreEntry.configure(
                            highlightthickness=2, highlightbackground="#00fcee"
                        )

                        # Creación del botón "Crear Pedido" que llama a la función "Pedidoscapturados" al ser presionado
                        BotonCrearPedido = Button(
                            ventanaCrearPedido,
                            cursor="hand2",
                            text="Crear Pedido 📂",  # Texto del botón
                            width=14,  # Ancho del botón
                            command=Pedidoscapturados,  # Función a ejecutar al presionar el botón
                        )
                        BotonCrearPedido.place(x=20, y=460)  # Posicionamiento del botón en la ventana

                        # Creación del botón "Retroceder" que llama a la función "mostrar_ventana_VerPedidos1" al ser presionado
                        BotonRetroceder = Button(
                            ventanaCrearPedido,
                            cursor="hand2",
                            text="Retroceder",  # Texto del botón
                            width=10,  # Ancho del botón
                            command=mostrar_ventana_VerPedidos1,  # Función a ejecutar al presionar el botón
                        )
                        BotonRetroceder.place(x=510, y=460)  # Posicionamiento del botón en la ventana

                        # Definición de la función "SalirDeCrearPedido" que destruye la ventana actual
                        def SalirDeCrearPedido():
                            ventanaCrearPedido.destroy()

                        # Creación del botón "Cerrar programa" que llama a la función "SalirDeCrearPedido" al ser presionado
                        BotonoCerrarPrograma = Button(
                            ventanaCrearPedido,
                            text="Cerrar programa",  # Texto del botón
                            cursor="hand2",
                            width=12,  # Ancho del botón
                            command=SalirDeCrearPedido,  # Función a ejecutar al presionar el botón
                        )
                        BotonoCerrarPrograma.place(x=600, y=460)  # Posicionamiento del botón en la ventana


                        datos_originales = pedido.CargarPedido()  # Lista para almacenar los datos de los pedidos

                        encabezados_originales = (
                            "id",
                            "comidas",
                            "bebidas",
                            "Postres",
                            "cantidad de comida",
                            "cantidad de bebidas",
                            "cantidad de postres",
                            "total",
                            "fechas",
                            "Estado",
                        )  # Lista de encabezados de las columnas de la tabla

                        anchos_columnas_originales = [
                            100,
                            300,
                            300,
                            300,
                            150,
                            150,
                            150,
                            200,
                            200,
                            100,
                        ]  # Lista de anchos de las columnas de la tabla

                        marco2 = Frame(ventanaCrearPedido)
                        marco2.pack(side=BOTTOM, padx=0, pady=50)

                        scroll_horizontal = Scrollbar(marco2, orient=HORIZONTAL)
                        scroll_horizontal.pack(side=BOTTOM, fill=X)

                        def crear_tabla(datos, encabezados, anchos_columnas):
                            # Crear el widget Treeview para mostrar la tabla
                            tablita = Treeview(
                                marco2,
                                show="headings",
                                xscrollcommand=scroll_horizontal.set,
                            )
                            tablita["columns"] = encabezados

                            estilo = ThemedStyle(marco2)
                            estilo.set_theme("scidgrey")

                            # Configuración del estilo de la tabla
                            estilo.configure(
                                "Custom.Treeview",
                                background="#081118",
                                foreground="#FFFFFF",
                                fieldbackground="#081118",
                                font=("Roboto", 10),
                                bordercolor="#1E1E1E",
                                selectbackground="#2979FF",
                                selectforeground="",
                            )
                            estilo.configure(
                                "Custom.Treeview.Heading",
                                background="#1E1E1E",
                                foreground="#081118",
                                font=("Roboto", 9, "bold"),
                            )
                            tablita.configure(style="Custom.Treeview")
                            tablita.tag_configure(
                                "Custom.Treeview.Heading",
                                background="#212121",
                                foreground="#081118",
                            )

                            # Configuración de columnas y encabezados
                            DatosTabla = zip(tablita["columns"], encabezados, anchos_columnas)
                            for columna, encabezado, ancho in DatosTabla:
                                tablita.column(columna, width=ancho, stretch=False)
                                tablita.heading(columna, text=encabezado, anchor=CENTER)

                            # Inserción de los datos en la tabla
                            for dato in datos:
                                tablita.insert("", END, values=dato)

                            tablita.pack(side=LEFT, fill=Y)
                            scroll_horizontal.config(command=tablita.xview)
                            tablita.config(xscrollcommand=scroll_horizontal.set)

                        crear_tabla(
                            datos_originales,
                            encabezados_originales,
                            anchos_columnas_originales,
                        )
                        ventanaCrearPedido.mainloop()
                    CrearPedido1()

                Button(
                    ventanaPedido,
                    text="Crear",
                    width=10,
                    command=CrearPedido,
                    cursor="hand2",
                ).place(x=340, y=140)

                def EditarPedido():
                    ventanaPedido.destroy()
                    def EditarPedido1():
                        global ventanaEditarPedido
                        ventanaEditarPedido = Tk()
                        ventanaEditarPedido.geometry("700x500+500+50")
                        ventanaEditarPedido.title("EDITAR")

                        ventanaEditarPedido.configure(background=pantllaColor)
                        ventanaEditarPedido.resizable(width=False, height=False)
                        Label(
                            ventanaEditarPedido,
                            text="EDITAR PEDIDOS",
                            font=30,
                            background=pantllaColor,
                            foreground="#00fcf1",
                        ).pack()
                        
                        # Funcion que captura los datos de los Entry
                        def capturarEditarPedidos():
                            comida.id = ComidaEntry.get()
                            bebida.id = BebidaEntry.get()
                            postre.id = PostreEntry.get()
                            CantidadComida = CantidadComidaEntry.get()
                            CantidadBebida = CantidadBebidaEntry.get()
                            CantidaPostres = CantidadPostreEntry.get()
                            ID = IDEntry.get()
                            pedido.id = ID
                            if (
                                comida.id == ""
                                or bebida.id == ""
                                or postre.id == ""
                                or CantidadComida == ""
                                or CantidadBebida == ""
                                or CantidaPostres == ""
                            ):
                                mensajeEditarPedido.config(text="Por favor, completa todos los campos.")
                                return

                            elif (
                                comida.id.isdigit() 
                                and bebida.id.isdigit()
                                and postre.id.isdigit()
                                and CantidadComida.isdigit()
                                and CantidadBebida.isdigit()
                                and CantidaPostres.isdigit()
                                and ID.isdigit()
                            ):
                                
                                comida.ComidaTotal()                  
                                pedido.comidas = comida.nombre
                                bebida.BebidaTotal()
                                pedido.bebidas = bebida.nombre
                                postre.PostresTotal()
                                pedido.postres = postre.nombre

                                if(bebida.BebidaTotal()==None):
                                    mensajeEditarPedido.config(
                                    text="Error. Por favor, ingrese los datos válidos.")
                                    return 
                                
                                elif(comida.ComidaTotal()==None  ):
                                    mensajeEditarPedido.config(
                                    text="Error. Por favor, ingrese los datos válidos.")
                                    return 
                                      
                                elif(postre.PostresTotal()==None):
                                    mensajeEditarPedido.config(
                                    text="Error. Por favor, ingrese los datos válidos.")
                                    return 
                                elif(comida.disponibilidad == 2):
                                    mensajeEditarPedido.config(text="Datos no disponibles.")
                                    return                                
                                elif(bebida.disponibilidad== 2):
                                    mensajeEditarPedido.config(text="Datos no disponibles.")
                                    return
                                elif(postre.disponibilidad == 2):
                                    mensajeEditarPedido.config(text="Datos no disponibles.")
                                    return
                                
                                pedido.total = (comida.precio * int(CantidadComida)) + (bebida.precio * int(CantidadBebida)) + (postre.precio * int(CantidaPostres))
                                pedido.cantidad_de_comida = CantidadComida
                                pedido.cantidad_de_bebidas = CantidadBebida
                                pedido.cantidad_de_postres = CantidaPostres
                                pedido.CapEstado()
                                if (pedido.Estados == "aceptado" or pedido.Estados == "Aceptado" or pedido.Estados == "ACEPTADO"):
                                    mensajeEditarPedido.config(text="El pedido ya ha sido aceptado y no se puede editar.")
                                    ComidaEntry.delete(0, END)
                                    BebidaEntry.delete(0, END)
                                    PostreEntry.delete(0, END)
                                    CantidadComidaEntry.delete(0, END)
                                    CantidadBebidaEntry.delete(0, END)
                                    CantidadPostreEntry.delete(0, END)
                                    IDEntry.delete(0, END)
                                    return   
                                else:
                                    if comida.disponibilidad == 1 and bebida.disponibilidad == 1 and postre.disponibilidad == 1:
                                        pedido.EditarPedido()
                                        ventanaEditarPedido.destroy()
                                        EditarPedido1()
                                        return
                                    else:
                                        mensajeEditarPedido.config(text="No se puede editar un pedido ya aceptado.")
                
                            else:
                                mensajeEditarPedido.config(
                                    text="Error. Por favor, ingrese los datos válidos.")
                                ComidaEntry.delete(0, END)
                                BebidaEntry.delete(0, END)
                                PostreEntry.delete(0, END)
                                CantidadComidaEntry.delete(0, END)
                                CantidadBebidaEntry.delete(0, END)
                                CantidadPostreEntry.delete(0, END)
                                IDEntry.delete(0, END)
                                
                                
                                

                        mensajeEditarPedido = Label(
                            ventanaEditarPedido,
                            background=pantllaColor,
                            foreground="#00fcf1",
                            fg="red"
                        )
                        mensajeEditarPedido.place(x=135, y=460)

                        # Etiqueta y campo de entrada para el ID de comida
                        Label(
                            ventanaEditarPedido,
                            text="ID de comida:",
                            font=5,
                            pady=10,
                            background=pantllaColor,
                            foreground="#00fcf1",
                        ).place(x=60, y=50)
                        ComidaEntry = Entry(
                            ventanaEditarPedido,
                            bg=pantllaColor,
                            foreground="#00fcee",
                            font=("calibri", 10),
                        )
                        ComidaEntry.place(x=230, y=64)
                        ComidaEntry.configure(
                            highlightthickness=2, highlightbackground="#00fcee"
                        )

                        # Etiqueta y campo de entrada para el ID de bebida
                        Label(
                            ventanaEditarPedido,
                            text="ID de bebida:",
                            font=5,
                            pady=10,
                            background=pantllaColor,
                            foreground="#00fcf1",
                        ).place(x=60, y=90)
                        BebidaEntry = Entry(
                            ventanaEditarPedido,
                            bg=pantllaColor,
                            foreground="#00fcee",
                            font=("calibri", 10),
                        )
                        BebidaEntry.place(x=230, y=104)
                        BebidaEntry.configure(
                            highlightthickness=2, highlightbackground="#00fcee"
                        )

                        # Etiqueta y campo de entrada para el ID de postre
                        Label(
                            ventanaEditarPedido,
                            text="ID de Postre:",
                            font=5,
                            pady=10,
                            background=pantllaColor,
                            foreground="#00fcf1",
                        ).place(x=60, y=130)
                        PostreEntry = Entry(
                            ventanaEditarPedido,
                            bg=pantllaColor,
                            foreground="#00fcee",
                            font=("calibri", 10),
                        )
                        PostreEntry.place(x=230, y=144)
                        PostreEntry.configure(
                            highlightthickness=2, highlightbackground="#00fcee"
                        )

                        # Etiqueta y campo de entrada para la cantidad de comida
                        Label(
                            ventanaEditarPedido,
                            text="Editar cantidad:",
                            font=3,
                            pady=3,
                            background=pantllaColor,
                            foreground="#00fcf1",
                        ).place(x=468, y=30)
                        CantidadComidaEntry = Entry(
                            ventanaEditarPedido,
                            bg=pantllaColor,
                            foreground="#00fcee",
                            font=("calibri", 10),
                        )
                        CantidadComidaEntry.place(x=470, y=64)
                        CantidadComidaEntry.configure(
                            highlightthickness=2, highlightbackground="#00fcee"
                        )

                        # Campo de entrada para la cantidad de bebida
                        CantidadBebidaEntry = Entry(
                            ventanaEditarPedido,
                            bg=pantllaColor,
                            foreground="#00fcee",
                            font=("calibri", 10),
                        )
                        CantidadBebidaEntry.place(x=470, y=104)
                        CantidadBebidaEntry.configure(
                            highlightthickness=2, highlightbackground="#00fcee"
                        )

                        # Campo de entrada para la cantidad de postre
                        CantidadPostreEntry = Entry(
                            ventanaEditarPedido,
                            bg=pantllaColor,
                            foreground="#00fcee",
                            font=("calibri", 10),
                        )
                        CantidadPostreEntry.place(x=470, y=144)
                        CantidadPostreEntry.configure(
                            highlightthickness=2, highlightbackground="#00fcee"
                        )

                        # Etiqueta y campo de entrada para el ID
                        Label(
                            ventanaEditarPedido,
                            text="ID:",
                            font=5,
                            pady=10,
                            background=pantllaColor,
                            foreground="#00fcf1",
                        ).place(x=60, y=170)
                        IDEntry = Entry(
                            ventanaEditarPedido,
                            bg=pantllaColor,
                            foreground="#00fcee",
                            font=("calibri", 10),
                        )
                        IDEntry.place(x=230, y=180)
                        IDEntry.configure(
                            highlightthickness=2, highlightbackground="#00fcee"
                        )

                        # Botón para guardar la edición
                        BotonGuardarEdicion = Button(
                            ventanaEditarPedido,
                            cursor="hand2",
                            text="Guardar Edicion 💾",
                            width=15,
                            command=capturarEditarPedidos,
                        )
                        BotonGuardarEdicion.place(x=20, y=460)

                        # Botón para retroceder
                        BotonRetroceder = Button(
                            ventanaEditarPedido,
                            cursor="hand2",
                            text="Retroceder",
                            width=10,
                            command=mostrar_ventana_VerPedidos2,
                        )
                        BotonRetroceder.place(x=490, y=460)

                        # Función para cerrar la ventana de detalles del pedido
                        def SalirDeDetallesPedido():
                            ventanaEditarPedido.destroy()

                        # Botón para cerrar el programa
                        BotonCerrarPrograma = Button(
                            ventanaEditarPedido,
                            cursor="hand2",
                            text="Cerrar programa",
                            width=12,
                            command=SalirDeDetallesPedido,
                        )
                        BotonCerrarPrograma.place(x=585, y=460)


                        datos_originales = pedido.CargarPedido()

                        encabezados_originales = (
                            "id",
                            "comidas",
                            "bebidas",
                            "Postres",
                            "cantidad de comida",
                            "cantidad de bebidas",
                            "cantidad de postres",
                            "total",
                            "fechas",
                            "Estado",
                        )
                        anchos_columnas_originales = [
                            100,
                            300,
                            300,
                            300,
                            150,
                            150,
                            150,
                            200,
                            200,
                            100,
                        ]

                        marco2 = Frame(ventanaEditarPedido)
                        marco2.pack(side=BOTTOM, padx=0, pady=50)
                        # -----------------------------------------------------------------------------------------------------------------------
                        scroll_horizontal = Scrollbar(marco2, orient=HORIZONTAL)
                        scroll_horizontal.pack(side=BOTTOM, fill=X)

                        def crear_tabla(datos, encabezados, anchos_columnas):
                            tablita = Treeview(
                                marco2,
                                show="headings",
                                xscrollcommand=scroll_horizontal.set,
                            )
                            tablita["columns"] = encabezados
                            estilo = ThemedStyle(marco2)
                            estilo.set_theme("scidgrey")
                            estilo.configure(
                                "Custom.Treeview",
                                background="#081118",
                                foreground="#FFFFFF",
                                fieldbackground="#081118",
                                font=("Roboto", 10),
                                bordercolor="#1E1E1E",
                                selectbackground="#2979FF",
                                selectforeground="",
                            )
                            estilo.configure(
                                "Custom.Treeview.Heading",
                                background="#1E1E1E",
                                foreground="#081118",
                                font=("Roboto", 9, "bold"),
                            )
                            tablita.configure(style="Custom.Treeview")
                            tablita.tag_configure(
                                "Custom.Treeview.Heading",
                                background="#212121",
                                foreground="#081118",
                            )
                            # -----------------------------------------------------------------------------------------------------------------------
                            DatosTabla = zip(
                                tablita["columns"], encabezados, anchos_columnas
                            )
                            for columna, encabezado, ancho in DatosTabla:
                                tablita.column(columna, width=ancho, stretch=False)
                                tablita.heading(columna, text=encabezado, anchor=CENTER)
                            for dato in datos:
                                tablita.insert("", END, values=dato)
                            tablita.pack(side=LEFT, fill=Y)
                            scroll_horizontal.config(command=tablita.xview)
                            tablita.config(xscrollcommand=scroll_horizontal.set)

                        crear_tabla(
                            datos_originales,
                            encabezados_originales,
                            anchos_columnas_originales,
                        )
                        ventanaEditarPedido.mainloop()
                    EditarPedido1()
                    

                BotonoEditarPedido = Button(
                    ventanaPedido,
                    text="Editar",
                    width=10,
                    cursor="hand2",
                    command=EditarPedido,
                )
                BotonoEditarPedido.place(x=150, y=140)

                def salirPedido():
                    ventanaPedido.destroy()

                BotonCerrarProgram = Button(
                    ventanaPedido,
                    text="Cerrar programa",
                    command=salirPedido,
                    cursor="hand2",
                    width=12,
                )
                BotonCerrarProgram.place(x=600, y=460)
                datos_originales = pedido.CargarPedido()

                encabezados_originales = (
                    "id",
                    "comidas",
                    "bebidas",
                    "Postres",
                    "cantidad de comida",
                    "cantidad de bebidas",
                    "cantidad de postres",
                    "total",
                    "fechas",
                    "Estado",
                )
                anchos_columnas_originales = [
                    100,
                    300,
                    300,
                    300,
                    150,
                    150,
                    150,
                    200,
                    200,
                    100,
                ]

                marco2 = Frame(ventanaPedido)
                marco2.pack(side=BOTTOM, padx=0, pady=50)
                # -----------------------------------------------------------------------------------------------------------------------
                scroll_horizontal = Scrollbar(marco2, orient=HORIZONTAL)
                scroll_horizontal.pack(side=BOTTOM, fill=X)

                def crear_tabla(datos, encabezados, anchos_columnas):
                    tablita = Treeview(
                        marco2, show="headings", xscrollcommand=scroll_horizontal.set
                    )
                    tablita["columns"] = encabezados
                    estilo = ThemedStyle(marco2)
                    estilo.set_theme("scidgrey")
                    estilo.configure(
                        "Custom.Treeview",
                        background="#081118",
                        foreground="#FFFFFF",
                        fieldbackground="#081118",
                        font=("Roboto", 10),
                        bordercolor="#1E1E1E",
                        selectbackground="#2979FF",
                        selectforeground="",
                    )

                    estilo.configure(
                        "Custom.Treeview.Heading",
                        background="#1E1E1E",
                        foreground="#081118",
                        font=("Roboto", 9, "bold"),
                    )

                    tablita.configure(style="Custom.Treeview")
                    tablita.tag_configure(
                        "Custom.Treeview.Heading",
                        background="#212121",
                        foreground="#081118",
                    )
                    DatosTabla = zip(tablita["columns"], encabezados, anchos_columnas)
                    for columna, encabezado, ancho in DatosTabla:
                        tablita.column(columna, width=ancho, stretch=False)
                        tablita.heading(columna, text=encabezado, anchor=CENTER)
                    for dato in datos:
                        tablita.insert("", END, values=dato)
                    tablita.pack(side=LEFT, fill=Y)
                    scroll_horizontal.config(command=tablita.xview)
                    tablita.config(xscrollcommand=scroll_horizontal.set)

                crear_tabla(
                    datos_originales, encabezados_originales, anchos_columnas_originales
                )
                ventanaPedido.mainloop()
            def mostrar_ventana_secundaria():
                ventanaCallCenter.destroy()  # Cierra la ventana del call center
                VerPedidos()  # Muestra la ventana de ver pedidos
            def mostrar_ventana_VerPedidos1():
                ventanaCrearPedido.destroy()  # Cierra la ventana de crear pedido
                VerPedidos()  # Muestra la ventana de ver pedidos
            def mostrar_ventana_VerPedidos2():
                ventanaEditarPedido.destroy()  # Cierra la ventana de editar pedido
                VerPedidos()  # Muestra la ventana de ver pedidos
            def ocultar_ventana_secundaria():
                ventanaPedido.destroy()  # Cierra la ventana del pedido
                construir_ventana_principal()  # Reconstruye y muestra la ventana principal
            construir_ventana_principal()  # Construye y muestra la ventana principal

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

        def administrador():
            ventana.destroy()

            def ventanaPrincipalAdmin():
                # Crear la ventana principal del administrador
                global ventanaAdmin
                ventanaAdmin = Tk()
                ventanaAdmin.title("Usuario")
                ventanaAdmin.geometry("700x500+500+50")
                ventanaAdmin.configure(background=pantllaColor)
                ventanaAdmin.resizable(width=False, height=False)

                # Etiquetas y elementos de la ventana principal del administrador
                Label(
                    ventanaAdmin,
                    text=" ADMINISTRADOR",
                    font=("Calibre", 14),
                    background=pantllaColor,
                    foreground="#00fcf1",
                ).place(x=290, y=0)

                Label(
                    ventanaAdmin,
                    text="Crear usuario",
                    font=("Calibre", 14),
                    background=pantllaColor,
                    foreground="#00fcf1",
                ).place(x=320, y=25)

                # Función para capturar los datos del usuario ingresado
                def CapturaringresarUsuario():
                    # Obtener nombre de usuario
                    usu.usuario = CajaNombre.get()
                    # Obtener clave y encriptarla con MD5
                    clave = CajaClave.get()
                    encriptada = hashlib.md5(clave.encode())
                    usu.contraseña = encriptada.hexdigest()
                    # Obtener tipo de usuario
                    tipo_usu = CajaTipoDeUsuario.get()

                    # Verificar si se ingresaron todos los campos requeridos
                    if usu.usuario == "" or usu.contraseña == "" or usu.tipo_usu_id == "":
                        mensajeAdmin.config(text="Por favor,Ingrese todos los campos correspondientes.")
                    else:
                        # Crear el usuario
                        if tipo_usu == "admin" or tipo_usu == "Admin" or tipo_usu == "ADMIN" or tipo_usu == "administrador" or tipo_usu == "Administrador" or tipo_usu == "ADMINISTRADOR" or tipo_usu == "1":
                            usu.tipo_usu_id = 1
                            usu.CrearUsuario()
                            #   # Quiere eliminarlo y que se vuelva a poner es como un reiniciiar basicamente 
                            ventanaAdmin.destroy()
                            ventanaPrincipalAdmin()

                        elif tipo_usu == "Chef" or tipo_usu == "CHEF" or tipo_usu == "chef" or tipo_usu == "Cocina" or tipo_usu == "COCINA" or tipo_usu == "cocina" or tipo_usu == "2":
                            usu.tipo_usu_id = 2
                            usu.CrearUsuario()
                            ventanaAdmin.destroy()
                            ventanaPrincipalAdmin()

                        elif tipo_usu == "call-center" or tipo_usu == "Call-center" or tipo_usu == "CALL-CENTER" or tipo_usu == "CALL" or tipo_usu == "Call" or tipo_usu == "call" or tipo_usu == "3":
                            usu.tipo_usu_id = 3
                            usu.CrearUsuario() 
                            ventanaAdmin.destroy()
                            ventanaPrincipalAdmin()

                        else:
                            mensajeAdmin.config(text="Tipo de usuario invalido.")

                mensajeAdmin = Label(
                    ventanaAdmin,
                    background=pantllaColor,
                    foreground="#00fcf1",
                    fg="red"
                )
                mensajeAdmin.place(x=410, y=150)

                # Etiqueta y campo de entrada para el nombre del usuario
                Label(
                    ventanaAdmin,
                    text="Nombre:",
                    font=5,
                    pady=10,
                    background=pantllaColor,
                    foreground="#00fcf1",
                ).place(x=230, y=40)
                CajaNombre = Entry(
                    ventanaAdmin,
                    bg=pantllaColor,
                    foreground="#00fcee",
                    font=("calibri", 10),
                )
                CajaNombre.place(x=310, y=54)
                CajaNombre.configure(
                    highlightthickness=2, highlightbackground="#00fcee"
                )

                # Etiqueta y campo de entrada para la clave del usuario
                Label(
                    ventanaAdmin,
                    text="Clave:",
                    font=16,
                    pady=10,
                    background=pantllaColor,
                    foreground="#00fcf1",
                ).place(x=250, y=76)
                CajaClave = Entry(
                    ventanaAdmin,
                    bg=pantllaColor,
                    foreground="#00fcee",
                    font=("calibri", 10),
                )
                CajaClave.place(x=310, y=90)
                CajaClave.configure(highlightthickness=2, highlightbackground="#00fcee")

                # Etiqueta y campo de entrada para el tipo de usuario
                Label(
                    ventanaAdmin,
                    text="Tipo de usuario:",
                    font=16,
                    pady=10,
                    background=pantllaColor,
                    foreground="#00fcf1",
                ).place(x=160, y=110)
                CajaTipoDeUsuario = Entry(
                    ventanaAdmin,
                    bg=pantllaColor,
                    foreground="#00fcee",
                    font=("calibri", 10),
                )
                CajaTipoDeUsuario.place(x=310, y=125)
                CajaTipoDeUsuario.configure(
                    highlightthickness=2, highlightbackground="#00fcee"
                )

                # Botón para ingresar el usuario
                BotonIngresar = Button(
                    ventanaAdmin,
                    text="Ingresar 📝",
                    width=10,
                    cursor="hand2",
                    command=CapturaringresarUsuario,
                )
                BotonIngresar.place(x=230, y=170)

                def EditarUsuario():
                    # Función para editar un usuario
                    ventanaAdmin.destroy()

                    def EditarUsuario1():
                        # Ventana para editar un usuario
                        global ventanaEditarUsuario
                        ventanaEditarUsuario = Tk()
                        ventanaEditarUsuario.title("Usuario")
                        ventanaEditarUsuario.geometry("700x500+500+50")
                        ventanaEditarUsuario.configure(background=pantllaColor)
                        ventanaEditarUsuario.resizable(width=False, height=False)

                        # Etiquetas y elementos de la ventana de edición de usuario
                        Label(
                            ventanaEditarUsuario,
                            text="EDITAR",
                            font=30,
                            background=pantllaColor,
                            foreground="#00fcf1",
                        ).pack()
                        Label(
                            ventanaEditarUsuario,
                            text="Editar usuario",
                            font=30,
                            background=pantllaColor,
                            foreground="#00fcf1",
                        ).place(x=290, y=40)
                        Label(
                            ventanaEditarUsuario,
                            text="ID:",
                            font=5,
                            pady=10,
                            background=pantllaColor,
                            foreground="#00fcf1",
                        ).place(x=0, y=80)
                        Label(
                            ventanaEditarUsuario,
                            text="Tipo de usuario:",
                            font=5,
                            pady=10,
                            background=pantllaColor,
                            foreground="#00fcf1",
                        ).place(x=128, y=135)
                        Label(
                            ventanaEditarUsuario,
                            text="Nombre:",
                            font=5,
                            pady=10,
                            background=pantllaColor,
                            foreground="#00fcf1",
                        ).place(x=195, y=80)
                        Label(
                            ventanaEditarUsuario,
                            text="Clave:",
                            font=5,
                            pady=10,
                            background=pantllaColor,
                            foreground="#00fcf1",
                        ).place(x=426, y=80)

                        def CapturarEditarUsuarioUsuario():
                            # Función para capturar los datos del usuario a editar
                            usu.id = CajaID.get()
                            usu.usuario = CajaNombre.get()
                            clave = CajaClave.get()
                            encriptada = hashlib.md5(clave.encode())
                            usu.contraseña = encriptada.hexdigest()
                            tipo_usu = CajaTipoDeUsuario.get()

                            # Verificar si se ingresaron todos los campos requeridos
                            if usu.id == "" or usu.usuario == "" or usu.contraseña == "" or tipo_usu == "":
                                mensajeEditaAdmin.config(text="Por favor,Ingrese todos los campos correspondientes.")                          

                            else:
                                if tipo_usu == "admin" or tipo_usu == "Admin" or tipo_usu == "ADMIN" or tipo_usu == "administrador" or tipo_usu == "Administrador" or tipo_usu == "ADMINISTRADOR":
                                    usu.tipo_usu_id = 1
                                    if usu.ContarAdmin() > 1:
                                        usu.EditarUsuario()
                                        ventanaEditarUsuario.destroy()
                                        EditarUsuario1()
                                    else:
                                        mensajeEditaAdmin.config(text="No puedes editar al unico aministrador.")
                                    usu.EditarUsuario()
                                    #   # Quiere eliminarlo y que se vuelva a poner es como un reiniciiar basicamente 
                                    
                                elif tipo_usu == "Chef" or tipo_usu == "CHEF" or tipo_usu == "chef" or tipo_usu == "Cocina" or tipo_usu == "COCINA" or tipo_usu == "cocina" :
                                    usu.tipo_usu_id = 2
                                    if usu.ContarAdmin() > 1:
                                        usu.EditarUsuario()
                                        ventanaEditarUsuario.destroy()
                                        EditarUsuario1()
                                    else:
                                        mensajeEditaAdmin.config(text="No puedes editar al unico aministrador.")

                                elif tipo_usu == "CALL-CENTER" or tipo_usu == "call-center" or tipo_usu == "Call-center" or tipo_usu == "CALL-CENTER" or tipo_usu == "CALL" or tipo_usu == "call" or tipo_usu == "call":
                                    usu.tipo_usu_id = 3
                                    usu.EditarUsuario()
                                    ventanaEditarUsuario.destroy()
                                    EditarUsuario1()

                                else:
                                    mensajeEditaAdmin.config(text="Tipo de usuario invalido.")

                        mensajeEditaAdmin = Label(
                            ventanaEditarUsuario,
                            background=pantllaColor,
                            fg="red"
                        )
                        mensajeEditaAdmin.place(x=170, y=180)


                        # Caja de entrada para el ID del usuario
                        CajaID = Entry(
                            ventanaEditarUsuario,
                            bg=pantllaColor,
                            foreground="#00fcee",
                            font=("calibri", 10),
                        )
                        CajaID.place(x=40, y=94)
                        CajaID.configure(
                            highlightthickness=2, highlightbackground="#00fcee"
                        )

                        # Caja de entrada para el nombre del usuario
                        CajaNombre = Entry(
                            ventanaEditarUsuario,
                            bg=pantllaColor,
                            foreground="#00fcee",
                            font=("calibri", 10),
                        )
                        CajaNombre.place(x=275, y=94)
                        CajaNombre.configure(
                            highlightthickness=2, highlightbackground="#00fcee"
                        )

                        # Caja de entrada para la clave del usuario
                        CajaClave = Entry(
                            ventanaEditarUsuario,
                            bg=pantllaColor,
                            foreground="#00fcee",
                            font=("calibri", 10),
                        )
                        CajaClave.place(x=490, y=94)
                        CajaClave.configure(
                            highlightthickness=2, highlightbackground="#00fcee"
                        )

                        # Caja de entrada para el tipo de usuario
                        CajaTipoDeUsuario = Entry(
                            ventanaEditarUsuario,
                            bg=pantllaColor,
                            foreground="#00fcee",
                            font=("calibri", 10),
                        )
                        CajaTipoDeUsuario.place(x=275, y=148)
                        CajaTipoDeUsuario.configure(
                            highlightthickness=2, highlightbackground="#00fcee"
                        )

                        # Botón "Ingresar"
                        BotonIngresar = Button(
                            ventanaEditarUsuario,
                            text="Ingresar 📝",
                            width=10,
                            cursor="hand2",
                            command=CapturarEditarUsuarioUsuario,
                        )
                        BotonIngresar.place(x=470, y=175)

                        # Botón "Retroceder"
                        BotonRetroceder = Button(
                            ventanaEditarUsuario,
                            text="Retroceder",
                            width=10,
                            cursor="hand2",
                            command=mostrar_ventana_Principal2,
                        )
                        BotonRetroceder.place(x=570, y=175)


                        def SalirDEeditarUsuario():
                            # Función para cerrar la ventana de editar usuario
                            ventanaEditarUsuario.destroy()

                        BotonCerrarPrograma = Button(
                            ventanaEditarUsuario,
                            text="Cerrar programa",
                            command=SalirDEeditarUsuario,  # Llama a la función SalirDEeditarUsuario cuando se hace clic en el botón
                            cursor="hand2",
                            width=12,
                        )
                        BotonCerrarPrograma.place(x=600, y=460)

                        # Cargar datos originales
                        datos_originales = usu.CargarUsuarios()
                        encabezados_originales = ("ID", "Nombre Usuario", "Tipo de usuario")
                        anchos_columnas_originales = [200, 300, 620]

                        # Crear marco
                        marco2 = Frame(ventanaEditarUsuario)
                        marco2.pack(side=BOTTOM, padx=0, pady=50)

                        scroll_horizontal = Scrollbar(marco2, orient=HORIZONTAL)
                        scroll_horizontal.pack(side=BOTTOM, fill=X)

                        def crear_tabla(datos, encabezados, anchos_columnas):
                            # Crear tabla
                            tablita = Treeview(
                                marco2,
                                show="headings",
                                xscrollcommand=scroll_horizontal.set,
                            )
                            tablita["columns"] = encabezados

                            estilo = ThemedStyle(marco2)
                            estilo.set_theme("scidgrey")
                            estilo.configure(
                                "Custom.Treeview",
                                background="#081118",
                                foreground="#FFFFFF",
                                fieldbackground="#081118",
                                font=("Roboto", 10),
                                bordercolor="#1E1E1E",
                                selectbackground="#2979FF",
                                selectforeground="",
                            )
                            estilo.configure(
                                "Custom.Treeview.Heading",
                                background="#1E1E1E",
                                foreground="#081118",
                                font=("Roboto", 9, "bold"),
                            )

                            tablita.configure(style="Custom.Treeview")
                            tablita.tag_configure(
                                "Custom.Treeview.Heading",
                                background="#212121",
                                foreground="#081118",
                            )

                            DatosTabla = zip(
                                tablita["columns"], encabezados, anchos_columnas
                            )
                            for columna, encabezado, ancho in DatosTabla:
                                tablita.column(columna, width=ancho, stretch=False)
                                tablita.heading(columna, text=encabezado, anchor=CENTER)
                            for dato in datos:
                                tablita.insert("", END, values=dato)

                            tablita.pack(side=LEFT, fill=Y)
                            scroll_horizontal.config(command=tablita.xview)
                            tablita.config(xscrollcommand=scroll_horizontal.set)

                        crear_tabla(
                            datos_originales,
                            encabezados_originales,
                            anchos_columnas_originales,
                        )

                        ventanaEditarUsuario.mainloop()

                    EditarUsuario1()  # Llama a la función EditarUsuario1 después de que se cierre la ventana



                BotonoEditar = Button(  # Crear un botón llamado BotonoEditar
                    ventanaAdmin,  # Colocar el botón en la ventana ventanaAdmin
                    text="Editar",  # Establecer el texto del botón como "Editar"
                    width=10,  # Establecer el ancho del botón como 10 unidades
                    cursor="hand2",  # Cambiar el cursor al estilo "hand2" (mano)
                    command=EditarUsuario,  # Asignar la función EditarUsuario como la acción a realizar al hacer clic en el botón
                )
                BotonoEditar.place(x=440, y=170)  # Colocar el botón en las coordenadas (440, 170) dentro de la ventana

                def EliminarUsuario():  # Definir una función llamada EliminarUsuario
                    ventanaAdmin.destroy()  # Cerrar la ventana ventanaAdmin

                    def EliminarUsuario1():  # Definir una función anidada llamada EliminarUsuario1
                        global ventanaEliminarUsua  # Declarar la variable ventanaEliminarUsua como global
                        ventanaEliminarUsua = Tk()  # Crear una nueva ventana llamada ventanaEliminarUsua
                        ventanaEliminarUsua.title("Usuario")  # Establecer el título de la ventana como "Usuario"
                        ventanaEliminarUsua.geometry("700x500+500+50")  # Establecer las dimensiones y la posición de la ventana
                        ventanaEliminarUsua.configure(background=pantllaColor)  # Establecer el color de fondo de la ventana
                        ventanaEliminarUsua.resizable(width=False, height=False)  # Hacer que la ventana no sea redimensionable

                        Label(  # Crear una etiqueta dentro de la ventanaEliminarUsua
                            ventanaEliminarUsua,
                            text="ELIMINAR",  # Establecer el texto de la etiqueta como "ELIMINAR"
                            font=30,  # Establecer el tamaño de fuente de la etiqueta
                            background=pantllaColor,  # Establecer el color de fondo de la etiqueta
                            foreground="#00fcf1",  # Establecer el color del texto de la etiqueta
                        ).pack()

                        Label(  # Crear otra etiqueta dentro de ventanaEliminarUsua
                            ventanaEliminarUsua,
                            text="Eliminar usuario",  # Establecer el texto de la etiqueta como "Eliminar usuario"
                            font=30,  # Establecer el tamaño de fuente de la etiqueta
                            background=pantllaColor,  # Establecer el color de fondo de la etiqueta
                            foreground="#00fcf1",  # Establecer el color del texto de la etiqueta
                        ).place(x=290, y=40)

                        Label(  # Crear otra etiqueta dentro de ventanaEliminarUsua
                            ventanaEliminarUsua,
                            text="ID:",  # Establecer el texto de la etiqueta como "ID:"
                            font=5,  # Establecer el tamaño de fuente de la etiqueta
                            pady=10,  # Establecer el relleno vertical de la etiqueta como 10 unidades
                            background=pantllaColor,  # Establecer el color de fondo de la etiqueta
                            foreground="#00fcf1",  # Establecer el color del texto de la etiqueta
                        ).place(x=250, y=60)


                        def capturarIdUsuarioEliminar():
                                ID = CajaIdBorrar.get()                              
                                if ID.isdigit():
                                    usu.id = ID
                                    CantidadAdmin = usu.ContarAdmin()
                                    TipoUsuario = usu.CapTipoUsuario()
                                    if(CantidadAdmin==None):
                                         mensajeEliminar.config(text="Por favor, ingrese un ID válido.")
                                         return                                    
                                    if(TipoUsuario==None):
                                         mensajeEliminar.config(text="Por favor, ingrese un ID válido.")
                                         return

                                    if TipoUsuario == 1 and CantidadAdmin == 1:
                                        mensajeEliminar.config(text="No se puede eliminar al único administrador restante.")
                                    else:
                                        usu.EliminarUsuario()
                                        ventanaEliminarUsua.destroy()
                                        EliminarUsuario1()
                                elif ID == "":
                                    mensajeEliminar.config(text="Por favor, ingrese un ID válido.")
                                else:
                                    mensajeEliminar.config(text="Error. Por favor, ingrese un ID numérico válido.")
                                    CajaIdBorrar.delete(0, END)
                                    return


                        mensajeEliminar = Label(  # Crear una etiqueta llamada mensajeEliminar
                            ventanaEliminarUsua,
                            background=pantllaColor,
                            foreground="#00fcf1",
                            fg="red"
                        )
                        mensajeEliminar.place(x=295, y=110)  # Colocar la etiqueta en las coordenadas (260, 95)

                        CajaIdBorrar = Entry(  # Crear una entrada de texto llamada CajaIdBorrar
                            ventanaEliminarUsua,
                            bg=pantllaColor,
                            foreground="#00fcee",
                            font=("calibri", 10)
                    
                        )
                        CajaIdBorrar.place(x=300, y=80)  # Colocar la entrada de texto en las coordenadas (290, 74)
                        CajaIdBorrar.configure(
                            highlightthickness=2, highlightbackground="#00fcee"
                        )  # Configurar el grosor y color del borde de la entrada de texto

                        BotonBorrar = Button(  # Crear un botón llamado BotonBorrar
                            ventanaEliminarUsua,
                            text="Borrar🗑",  # Establecer el texto del botón como "Borrar🗑"
                            width=10,  # Establecer el ancho del botón como 10 unidades
                            cursor="hand2",  # Cambiar el cursor al estilo "hand2" (mano)
                            command=capturarIdUsuarioEliminar,  # Asignar la función capturarIdUsuarioEliminar como la acción al hacer clic en el botón
                        )
                        BotonBorrar.place(x=270, y=140)  # Colocar el botón en las coordenadas (270, 140)

                        BotonoRetroceder = Button(  # Crear un botón llamado BotonoRetroceder
                            ventanaEliminarUsua,
                            text="Retroceder",  # Establecer el texto del botón como "Retroceder"
                            width=10,  # Establecer el ancho del botón como 10 unidades
                            cursor="hand2",  # Cambiar el cursor al estilo "hand2" (mano)
                            command=mostrar_ventana_Principal,  # Asignar la función mostrar_ventana_Principal como la acción al hacer clic en el botón
                        )
                        BotonoRetroceder.place(x=370, y=140)  # Colocar el botón en las coordenadas (370, 140)

                        def SalirDEeliminarUsua():  # Definir una función llamada SalirDEeliminarUsua
                            ventanaEliminarUsua.destroy()  # Cerrar la ventana ventanaEliminarUsua

                        BotonCerrarPrograma = Button(  # Crear un botón llamado BotonCerrarPrograma
                            ventanaEliminarUsua,
                            text="Cerrar programa",  # Establecer el texto del botón como "Cerrar programa"
                            command=SalirDEeliminarUsua,  # Asignar la función SalirDEeliminarUsua como la acción al hacer clic en el botón
                            cursor="hand2",  # Cambiar el cursor al estilo "hand2" (mano)
                            width=12,  # Establecer el ancho del botón como 12 unidades
                        )
                        BotonCerrarPrograma.place(x=600, y=460)  # Colocar el botón en las coordenadas (600, 460) en la ventan, ventanaEliminarUsua


                        datos_originales = usu.CargarUsuarios()  # Obtener los datos originales de usuarios mediante el método CargarUsuarios de la instancia usu
                        encabezados_originales = ("ID", "Nombre Usuario", "Tipo de usuario")  # Definir los encabezados de la tabla
                        anchos_columnas_originales = [200, 300, 620]  # Definir los anchos de las columnas de la tabla

                        marco2 = Frame(ventanaEliminarUsua)  # Crear un marco dentro de ventanaEliminarUsua
                        marco2.pack(side=BOTTOM, padx=0, pady=50)  # Colocar el marco en la parte inferior con relleno en los ejes X e Y

                        scroll_horizontal = Scrollbar(marco2, orient=HORIZONTAL)  # Crear una barra de desplazamiento horizontal en el marco2
                        scroll_horizontal.pack(side=BOTTOM, fill=X)  # Colocar la barra de desplazamiento en la parte inferior y que ocupe todo el ancho

                        def crear_tabla(datos, encabezados, anchos_columnas):  # Definir una función llamada crear_tabla que recibe los datos, encabezados y anchos de columna
                            tablita = Treeview(  # Crear un widget Treeview llamado tablita
                                marco2,
                                show="headings",
                                xscrollcommand=scroll_horizontal.set,
                            )
                            tablita["columns"] = encabezados  # Establecer las columnas de la tabla
                            estilo = ThemedStyle(marco2)  # Crear un objeto ThemedStyle para personalizar el estilo del Treeview
                            estilo.set_theme("scidgrey")  # Establecer el tema del estilo del Treeview
                            estilo.configure(
                                "Custom.Treeview",
                                background="#081118",
                                foreground="#FFFFFF",
                                fieldbackground="#081118",
                                font=("Roboto", 10),
                                bordercolor="#1E1E1E",
                                selectbackground="#2979FF",
                                selectforeground="",
                            )  # Configurar el estilo del Treeview
                            estilo.configure(
                                "Custom.Treeview.Heading",
                                background="#1E1E1E",
                                foreground="#081118",
                                font=("Roboto", 9, "bold"),
                            )  # Configurar el estilo de los encabezados del Treeview

                            tablita.configure(style="Custom.Treeview")  # Aplicar el estilo personalizado al Treeview
                            tablita.tag_configure(
                                "Custom.Treeview.Heading",
                                background="#212121",
                                foreground="#081118",
                            )  # Configurar el estilo de los encabezados del Treeview

                            DatosTabla = zip(tablita["columns"], encabezados, anchos_columnas)  # Combinar las columnas, encabezados y anchos en un solo iterable
                            for columna, encabezado, ancho in DatosTabla:
                                tablita.column(columna, width=ancho, stretch=False)  # Establecer el ancho y el estiramiento de la columna
                                tablita.heading(columna, text=encabezado, anchor=CENTER)  # Establecer el texto y la alineación del encabezado
                            for dato in datos:
                                tablita.insert("", END, values=dato)  # Insertar los datos en la tabla

                            tablita.pack(side=LEFT, fill=Y)  # Colocar la tabla en el lado izquierdo y que ocupe todo el alto
                            scroll_horizontal.config(command=tablita.xview)  # Configurar la barra de desplazamiento horizontal
                            tablita.config(xscrollcommand=scroll_horizontal.set)

                        crear_tabla(
                            datos_originales,
                            encabezados_originales,
                            anchos_columnas_originales,
                        )  # Llamar a la función crear_tabla con los datos originales, encabezados originales y anchos de columna originales
                        ventanaEliminarUsua.mainloop()  # Iniciar el bucle principal de la ventanaEliminarUsua
                    EliminarUsuario1()  # Llamar a la función EliminarUsuario1


                def salirAdministrador():
                    ventanaAdmin.destroy()  # Cerrar la ventanaAdmin al llamar a la función destroy()

                BotonCerrarPrograma = Button(
                    ventanaAdmin,
                    text="Cerrar programa",
                    command=salirAdministrador,
                    cursor="hand2",
                    width=12,
                )
                BotonCerrarPrograma.place(x=600, y=460)  # Crear un botón para cerrar el programa

                Button(
                    ventanaAdmin,
                    text="Eliminar usuario",
                    width=13,
                    command=EliminarUsuario,
                ).place(x=324, y=170)  # Crear un botón para eliminar un usuario

                datos_originales = usu.CargarUsuarios()  # Obtener los datos originales de usuarios mediante el método CargarUsuarios de la instancia usu
                encabezados_originales = ("ID", "Nombre Usuario", "Tipo de usuario")  # Definir los encabezados de la tabla
                anchos_columnas_originales = [200, 300, 620]  # Definir los anchos de las columnas de la tabla

                marco2 = Frame(ventanaAdmin)  # Crear un marco dentro de ventanaAdmin
                marco2.pack(side=BOTTOM, padx=0, pady=50)  # Colocar el marco en la parte inferior con relleno en los ejes X e Y

                scroll_horizontal = Scrollbar(marco2, orient=HORIZONTAL)  # Crear una barra de desplazamiento horizontal en el marco2
                scroll_horizontal.pack(side=BOTTOM, fill=X)  # Colocar la barra de desplazamiento en la parte inferior y que ocupe todo el ancho

                def crear_tabla(datos, encabezados, anchos_columnas):  # Definir una función llamada crear_tabla que recibe los datos, encabezados y anchos de columna
                    tablita = Treeview(
                        marco2, show="headings", xscrollcommand=scroll_horizontal.set
                    )  # Crear un widget Treeview llamado tablita
                    tablita["columns"] = encabezados  # Establecer las columnas de la tabla
                    estilo = ThemedStyle(marco2)  # Crear un objeto ThemedStyle para personalizar el estilo del Treeview
                    estilo.set_theme("scidgrey")  # Establecer el tema del estilo del Treeview
                    estilo.configure(
                        "Custom.Treeview",
                        background="#081118",
                        foreground="#FFFFFF",
                        fieldbackground="#081118",
                        font=("Roboto", 10),
                        bordercolor="#1E1E1E",
                        selectbackground="#2979FF",
                        selectforeground="",
                    )  # Configurar el estilo del Treeview
                    estilo.configure(
                        "Custom.Treeview.Heading",
                        background="#1E1E1E",
                        foreground="#081118",
                        font=("Roboto", 9, "bold"),
                    )  # Configurar el estilo de los encabezados del Treeview

                    tablita.configure(style="Custom.Treeview")  # Aplicar el estilo personalizado al Treeview
                    tablita.tag_configure(
                        "Custom.Treeview.Heading",
                        background="#212121",
                        foreground="#081118",
                    )  # Configurar el estilo de los encabezados del Treeview

                    DatosTabla = zip(tablita["columns"], encabezados, anchos_columnas)  # Combinar las columnas, encabezados y anchos de columna
                    for columna, encabezado, ancho in DatosTabla:
                        tablita.column(columna, width=ancho, stretch=False)  # Configurar el ancho de cada columna
                        tablita.heading(columna, text=encabezado, anchor=CENTER)  # Configurar el texto y alineación de los encabezados
                    for dato in datos:
                        tablita.insert("", END, values=dato)  # Insertar los datos en la tabla

                    tablita.pack(side=LEFT, fill=Y)  # Colocar la tabla en el lado izquierdo y que ocupe todo el alto
                    scroll_horizontal.config(command=tablita.xview)  # Configurar la barra de desplazamiento horizontal
                    tablita.config(xscrollcommand=scroll_horizontal.set)

                crear_tabla(
                    datos_originales, encabezados_originales, anchos_columnas_originales
                )  # Llamar a la función crear_tabla con los datos originales, encabezados originales y anchos de columna originales

                BotonEliminarUsuario = Button(
                    ventanaAdmin,
                    text="Eliminar usuario",
                    width=13,
                    cursor="hand2",
                    command=EliminarUsuario,
                )
                BotonEliminarUsuario.place(x=324, y=170)  # Crear un botón para eliminar un usuario

                def salirAdministrador():
                    ventanaAdmin.destroy()  # Cerrar la ventanaAdmin al llamar a la función destroy()

                BotonCerrarPrograma = Button(
                    ventanaAdmin,
                    text="Cerrar programa",
                    command=salirAdministrador,
                    cursor="hand2",
                    width=12,
                )
                BotonCerrarPrograma.place(x=600, y=460)  # Crear un botón para cerrar el programa

                ventanaAdmin.mainloop()  # Iniciar el bucle principal de la ventanaAdmin

            def mostrar_ventana_Principal():
                ventanaEliminarUsua.destroy()
                ventanaPrincipalAdmin()  # Llamar a la función ventanaPrincipalAdmin después de cerrar la ventanaEliminarUsua

            def mostrar_ventana_Principal2():
                ventanaEditarUsuario.destroy()
                ventanaPrincipalAdmin()  # Llamar a la función ventanaPrincipalAdmin después de cerrar la ventanaEditarUsuario

            ventanaPrincipalAdmin()  # Llamar a la función ventanaPrincipalAdmin que nos sirve para mostrar la ventana principal del administrador

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

        def chef():
            ventana.destroy()  # Destruye la ventana actual
            # Definir la función "construir_ventana_principal()"
            def construir_ventana_principal():
                ventanaChef = Tk()  # Crea una nueva ventana llamada "ventanaChef"
                ventanaChef.title("Usuario")  # Establece el título de la ventana
                ventanaChef.geometry("700x500+500+50")  # Establece el tamaño y la posición de la ventana
                ventanaChef.configure(background=pantllaColor)  # Establece el color de fondo de la ventana
                ventanaChef.resizable(width=False, height=False)  # Desactiva la capacidad de redimensionar la ventana

                # Etiqueta "CHEF"
                Label(
                    ventanaChef,
                    text="CHEF",
                    font=("Calibre", 14),
                    background=pantllaColor,
                    foreground="#00fcf1",
                ).place(x=326, y=28)  # Coloca la etiqueta en la posición especificada (coordenadas x, y)

                # Función "capturadoIDAceptar()"
                def capturadoIDAceptar():
                    ID = CajaID.get()  # Obtiene el valor de la entrada de texto llamada "CajaID"

                    if ID.isdigit():  # Verifica si el ID ingresado es un número
                        pedido.id = ID
                        pedido.AceptarPedido()
                        ventanaChef.destroy()  # Destruye la ventana actual
                        construir_ventana_principal()  # Vuelve a construir la ventana principal

                    elif ID == "":
                        mensajePedidoChef.config(
                            text="Por favor, ingrese un ID válido."
                        )

                    else:
                        mensajePedidoChef.config(
                            text="Error. Por favor, ingrese un ID numérico válido."
                        )

                        CajaID.delete(0, END)  # Borra el contenido de la entrada de texto "CajaID"

                    return

                # Función "capturadoIDrechazar()"
                def capturadoIDrechazar():
                    ID = CajaID.get()  # Obtiene el valor de la entrada de texto llamada "CajaID"

                    if ID.isdigit():  # Verifica si el ID ingresado es un número
                        pedido.id = ID
                        pedido.RechazarPedido()
                        ventanaChef.destroy()  # Destruye la ventana actual
                        construir_ventana_principal()  # Vuelve a construir la ventana principal

                    elif ID == "":
                        mensajePedidoChef.config(
                            text="Por favor, ingrese un ID válido."
                        )

                    else:
                        mensajePedidoChef.config(
                            text="Error. Por favor, ingrese un ID numérico válido."
                        )

                        CajaID.delete(0, END)  # Borra el contenido de la entrada de texto "CajaID"

                    return

                mensajePedidoChef = Label(
                    ventanaChef,
                    background=pantllaColor, # Establece el color de fondo de la etiqueta
                    foreground="#00fcf1", #Establece el color del texto de la etiqueta
                    fg="red"
                )
                mensajePedidoChef.place(x=428, y=75)  # Coloca la etiqueta en la posición especificada (coordenadas x, y)


                # Etiqueta "ID" para indicar el campo de entrada de ID
                Label(
                    ventanaChef,
                    text="ID:",  # Texto que se muestra en la etiqueta
                    font=5,  # Fuente de la etiqueta
                    pady=10,  # Espacio vertical entre la etiqueta y los elementos cercanos
                    background=pantllaColor,  # Color de fondo de la etiqueta
                    foreground="#00fcf1",  # Color del texto de la etiqueta
                ).place(x=240, y=60)  # Coloca la etiqueta en la posición especificada (coordenadas x, y)

                # Campo de entrada para ingresar el ID del pedido
                CajaID = Entry(
                    ventanaChef,
                    bg=pantllaColor,  # Color de fondo del campo de entrada
                    foreground="#00fcee",  # Color del texto del campo de entrada
                    font=("calibri", 10),  # Fuente del campo de entrada
                )
                CajaID.place(x=280, y=73)  # Coloca el campo de entrada en la posición especificada (coordenadas x, y)
                CajaID.configure(highlightthickness=2, highlightbackground="#00fcee")  # Configuración del resaltado del campo de entrada

                # Botón "Rechazar" para rechazar un pedido
                BotonRechazar = Button(
                    ventanaChef,
                    text="Rechazar ✖️",  # Texto que se muestra en el botón
                    width=10,  # Ancho del botón
                    cursor="hand2",  # Cambia el cursor al pasar sobre el botón
                    command=capturadoIDrechazar,  # Función a ejecutar al hacer clic en el botón
                )
                BotonRechazar.place(x=200, y=120)  # Coloca el botón en la posición especificada (coordenadas x, y)

                # Botón "Aceptar" para aceptar un pedido
                BotonAceptar = Button(
                    ventanaChef,
                    text="Aceptar ✔️",  # Texto que se muestra en el botón
                    width=10,  # Ancho del botón
                    cursor="hand2",  # Cambia el cursor al pasar sobre el botón
                    command=capturadoIDAceptar,  # Función a ejecutar al hacer clic en el botón
                )
                BotonAceptar.place(x=100, y=120)  # Coloca el botón en la posición especificada (coordenadas x, y)


                def Comida():
                    ventanaChef.destroy()  # Destruir la ventana actual 'ventanaChef'

                    def Comida2():
                        # Declaración de la ventana 'ventanaComida'
                        global ventanaComida
                        ventanaComida = Tk()
                        ventanaComida.title("Usuario")  # Título de la ventana
                        ventanaComida.geometry("700x500+500+50")  # Dimensiones y posición de la ventana
                        ventanaComida.configure(background=pantllaColor)  # Color de fondo de la ventana
                        ventanaComida.resizable(width=False, height=False)  # Desactivar el redimensionamiento de la ventana

                        Label(
                            ventanaComida,
                            text="DESHABILITAR-HABILITAR",  # Texto de la etiqueta
                            font=30,  # Fuente y tamaño del texto
                            background=pantllaColor,  # Color de fondo
                            foreground="#00fcf1",  # Color de fuente
                        ).pack()  # Empaquetar y mostrar la etiqueta en la ventana

                        def capturadoIDHabiliar():
                            # Obtener el ID ingresado en la caja de texto 'CajaID'
                            ID = CajaID.get()

                            if ID.isdigit():  # Verificar si el ID es un número
                                comida.id = ID
                                comida.HabilitarComida()  # Llamar a la función para habilitar la comida
                                ventanaComida.destroy()  # Cerrar la ventana actual
                                Comida2()  # Llamar a la función Comida2 nuevamente
                            elif ID == "":
                                mensaje.config(text="Por favor, ingrese un ID válido.")  # Actualizar mensaje de error
                            else:
                                mensaje.config(text="Error. Por favor, ingrese un ID numérico válido.")  # Actualizar mensaje de error
                                CajaID.delete(0, END)  # Borrar contenido de la caja de texto
                            return

                        def capturadoIDdesabilitar():
                            # Obtener el ID ingresado en la caja de texto 'CajaID'
                            ID = CajaID.get()

                            if ID.isdigit():  # Verificar si el ID es un número
                                comida.id = ID
                                comida.DeshabilitarComida()  # Llamar a la función para deshabilitar la comida
                                ventanaComida.destroy()  # Cerrar la ventana actual
                                Comida2()  # Llamar a la función Comida2 nuevamente
                            elif ID == "":
                                mensaje.config(text="Por favor, ingrese un ID válido.")  # Actualizar mensaje de error
                            else:
                                mensaje.config(text="Error. Por favor, ingrese un ID numérico válido.")  # Actualizar mensaje de error
                                CajaID.delete(0, END)  # Borrar contenido de la caja de texto
                            return
                        
                        
                        # Este Mensaje mostrara los errores que existen es una variable que se ocupa arriba 
                        # cuando se intenta verificar.
                        mensaje = Label(
                            ventanaComida,
                            background=pantllaColor,
                            foreground="#00fcf1",
                            fg="red"
                        )
                        mensaje.place(x=260, y=95)  # Posicionar la etiqueta en la ventana


                        Label(
                            ventanaComida,
                            text="ID:",  # Texto de la etiqueta
                            font=5,  # Fuente y tamaño del texto
                            pady=10,  # Espacio vertical interno de la etiqueta
                            background=pantllaColor,  # Color de fondo
                            foreground="#00fcf1",  # Color de fuente
                        ).place(x=235, y=50)  # Posicionar la etiqueta en la ventana

                        CajaID = Entry(
                            ventanaComida,
                            bg=pantllaColor,  # Color de fondo de la caja de texto
                            foreground="#00fcee",  # Color de fuente de la caja de texto
                            font=("calibri", 10),  # Fuente y tamaño del texto de la caja
                        )
                        CajaID.place(x=270, y=64)  # Posicionar la caja de texto en la ventana
                        CajaID.configure(
                            highlightthickness=2,  # Grosor del borde resaltado
                            highlightbackground="#00fcee",  # Color del borde resaltado
                        )

                        BotonHabilitar = Button(
                            ventanaComida,
                            text="Habilitar✅",  # Texto del botón
                            width=13,  # Ancho del botón
                            cursor="hand2",  # Cambiar el cursor al pasar sobre el botón
                            command=capturadoIDHabiliar,  # Función a ejecutar al hacer clic en el botón
                        )
                        BotonHabilitar.place(x=290, y=120)  # Posicionar el botón en la ventana

                        BotonDesabilitar = Button(
                            ventanaComida,
                            text="Desabilitar❎",  # Texto del botón
                            width=13,  # Ancho del botón
                            cursor="hand2",  # Cambiar el cursor al pasar sobre el botón
                            command=capturadoIDdesabilitar,  # Función a ejecutar al hacer clic en el botón
                        )
                        BotonDesabilitar.place(x=180, y=120)  # Posicionar el botón en la ventana

                        def salirChef():
                            ventanaComida.destroy()

                        BotonoCerrarPrograma = Button(
                            ventanaComida,
                            text="Cerrar programa",  # Texto del botón
                            command=salirChef,  # Función a ejecutar al hacer clic en el botón
                            cursor="hand2",  # Cambiar el cursor al pasar sobre el botón
                            width=14,  # Ancho del botón
                        )
                        BotonoCerrarPrograma.place(x=540, y=440)  # Posicionar el botón en la ventana

                        BotonRetroceder = Button(
                            ventanaComida,
                            text="Retroceder",  # Texto del botón
                            width=10,  # Ancho del botón
                            cursor="hand2",  # Cambiar el cursor al pasar sobre el botón
                            command=mostrar_ventana_Principal_Chef1,  # Función a ejecutar al hacer clic en el botón
                        )
                        BotonRetroceder.place(x=400, y=120)  # Posicionar el botón en la ventana

                        DtosComiadas = comida.CargarComida()  # Obtener datos de las comidas

                        encabezadosComidas = (
                            "id",
                            "nombre",
                            "precio",
                            "tamaño",
                            "ingredientes",
                            "disponibilidad",
                        )  # Encabezados de las columnas en la tabla

                        anchos_Comidas = [
                            100,
                            400,
                            200,
                            200,
                            650,
                            100,
                        ]  # Anchura personalizada para cada columna en la tabla

                        marco2 = Frame(ventanaComida)  # Crear un marco en la ventana
                        marco2.pack(side=BOTTOM, padx=0, pady=90)  # Posicionar el marco en la ventana

                        scroll_horizontal = Scrollbar(marco2, orient=HORIZONTAL)  # Crear una barra de desplazamiento horizontal
                        scroll_horizontal.pack(side=BOTTOM, fill=X)  # Posicionar la barra de desplazamiento en el marco

                        def crear_tabla(datos, encabezados, anchos_columnas):
                            tablita = Treeview(
                                marco2,
                                show="headings",
                                xscrollcommand=scroll_horizontal.set,
                            )  # Crear un objeto Treeview para mostrar la tabla
                            tablita["columns"] = encabezados  # Establecer las columnas de la tabla

                            estilo = ThemedStyle(marco2)
                            estilo.set_theme("scidgrey")
                            estilo.configure(
                                "Custom.Treeview",
                                background="#081118",
                                foreground="#FFFFFF",
                                fieldbackground="#081118",
                                font=("Roboto", 10),
                                bordercolor="#1E1E1E",
                                selectbackground="#2979FF",
                                selectforeground="",
                            )  # Establecer el estilo personalizado para la tabla

                            estilo.configure(
                                "Custom.Treeview.Heading",
                                background="#1E1E1E",
                                foreground="#081118",
                                font=("Roboto", 9, "bold"),
                            )  # Establecer el estilo personalizado para los encabezados de la tabla

                            tablita.configure(style="Custom.Treeview")  # Aplicar el estilo personalizado a la tabla
                            tablita.tag_configure(
                                "Custom.Treeview.Heading",
                                background="#212121",
                                foreground="#081118",
                            )  # Configurar el estilo personalizado para los encabezados de la tabla

                            # Establecer las columnas y los encabezados en la tabla
                            DatosTabla = zip(tablita["columns"], encabezados, anchos_columnas)
                            for columna, encabezado, ancho in DatosTabla:
                                tablita.column(columna, width=ancho, stretch=False)
                                tablita.heading(columna, text=encabezado, anchor=CENTER)

                            # Insertar los datos en la tabla
                            for dato in datos:
                                tablita.insert("", END, values=dato)

                            tablita.pack(side=LEFT, fill=Y)  # Mostrar la tabla en el marco
                            scroll_horizontal.config(command=tablita.xview)  # Configurar la barra de desplazamiento horizontal
                            tablita.config(xscrollcommand=scroll_horizontal.set)

                        # Crear la tabla con los datos obtenidos
                        crear_tabla(
                            DtosComiadas,
                            encabezadosComidas,
                            anchos_Comidas,
                        )

                    Comida2()  # se  llama a la función Comida2 para que ejecute todo
                    # su contenido que esta dentro

                Button(
                    ventanaChef,
                    text="Comida",  # Texto del botón
                    width=10,  # Ancho del botón
                    cursor="hand2",  # Cambiar el cursor al pasar sobre el botón
                    command=Comida,  # Función a ejecutar al hacer clic en el botón
                ).place(x=300, y=120)  # Posicionar el botón en la ventana

                def Postres():
                    ventanaChef.destroy()  # Cerrar la ventana actual (ventanaChef)

                    def postre2():
                        global VentanaPostres
                        VentanaPostres = Tk()  # Crear una nueva ventana
                        VentanaPostres.title("Usuario")  # Establecer el título de la ventana
                        VentanaPostres.geometry("700x500+500+50")  # Establecer el tamaño y la posición de la ventana
                        VentanaPostres.configure(background=pantllaColor)  # Establecer el color de fondo de la ventana
                        VentanaPostres.resizable(width=False, height=False)  # Hacer que la ventana no sea redimensionable

                        Label(
                            VentanaPostres,
                            text="DESHABILITAR-HABILITAR",  # Texto de la etiqueta
                            font=30,  # Fuente y tamaño del texto
                            background=pantllaColor,  # Color de fondo de la etiqueta
                            foreground="#00fcf1",  # Color de fuente de la etiqueta
                        ).pack()  # Mostrar la etiqueta en la ventana

                        def capturadoIDHabiliar():
                            ID = CajaID.get()  # Obtener el valor ingresado en la caja de texto

                            if ID.isdigit():  # Verificar si el valor es un número entero
                                pass
                                postre.id = ID  # Asignar el ID al objeto postre
                                postre.HabilitarPostre()  # Llamar al método HabilitarPostre del objeto postre
                                VentanaPostres.destroy()  # Cerrar la ventana VentanaPostres
                                postre2()  # Llamar a la función postre2 para volver a mostrar la ventana

                            elif ID == "":  # Verificar si el valor está vacío
                                mensaje2.config(text="Por favor, ingrese un ID válido.")  # Mostrar un mensaje de error

                            else:
                                mensaje2.config(text="Error. Por favor, ingrese un ID numérico válido.")  # Mostrar un mensaje de error
                                CajaID.delete(0, END)  # Borrar el contenido de la caja de texto

                            return

                        def capturadoIDdesabilitar():
                            ID = CajaID.get()  # Obtener el valor ingresado en la caja de texto

                            if ID.isdigit():  # Verificar si el valor es un número entero
                                postre.id = ID  # Asignar el ID al objeto postre
                                postre.DeshabilitarPostre()  # Llamar al método DeshabilitarPostre del objeto postre
                                VentanaPostres.destroy()  # Cerrar la ventana VentanaPostres
                                postre2()  # Llamar a la función postre2 para volver a mostrar la ventana

                            elif ID == "":  # Verificar si el valor está vacío
                                mensaje2.config(text="Por favor, ingrese un ID válido.")  # Mostrar un mensaje de error

                            else:
                                mensaje2.config(text="Error. Por favor, ingrese un ID numérico válido.")  # Mostrar un mensaje de error

                                CajaID.delete(0, END)  # Borrar el contenido de la caja de texto

                            return

                        mensaje2 = Label(
                            VentanaPostres,
                            background=pantllaColor, #Color de fondo 
                            foreground="#00fcf1",
                            fg="red"
                        )  # Crear una etiqueta para mostrar mensajes
                        mensaje2.place(x=260, y=95)  # Posicionar la etiqueta en la ventana

                        Label(
                            VentanaPostres,
                            text="ID:",  # Texto de la etiqueta
                            font=5,  # Fuente y tamaño del texto
                            pady=10,  # Espacio vertical interno de la etiqueta
                            background=pantllaColor,  # Color de fondo de la etiqueta
                            foreground="#00fcf1",  # Color de fuente de la etiqueta
                        ).place(x=235, y=50)  # Posicionar la etiqueta en la ventana

                        CajaID = Entry(
                            VentanaPostres,
                            bg=pantllaColor,  # Color de fondo de la caja de texto
                            foreground="#00fcee",  # Color de fuente de la caja de texto
                            font=("calibri", 10),  # Fuente y tamaño del texto de la caja de texto
                        )
                        CajaID.place(x=270, y=64)  # Posicionar la caja de texto en la ventana
                        CajaID.configure(
                            highlightthickness=2, highlightbackground="#00fcee"  # Configurar el resaltado de la caja de texto
                        )

                        BotonHabilitar = Button(
                            VentanaPostres,
                            text="Habilitar✅",  # Texto del botón
                            width=13,  # Ancho del botón
                            cursor="hand2",  # Cambiar el cursor al pasar sobre el botón
                            command=capturadoIDHabiliar,  # Función a ejecutar al hacer clic en el botón
                        )
                        BotonHabilitar.place(x=290, y=120)  # Posicionar el botón en la ventana

                        BotonDesabilitar = Button(
                            VentanaPostres,
                            text="Desabilitar❎",  # Texto del botón
                            width=13,  # Ancho del botón
                            cursor="hand2",  # Cambiar el cursor al pasar sobre el botón
                            command=capturadoIDdesabilitar,  # Función a ejecutar al hacer clic en el botón
                        )
                        BotonDesabilitar.place(x=180, y=120)  # Posicionar el botón en la ventana

                        def salirChef():
                            VentanaPostres.destroy()  # Cerrar la ventana VentanaPostres

                        BotonoCerrarPrograma = Button(
                            VentanaPostres,
                            text="Cerrar programa",  # Texto del botón
                            command=salirChef,  # Función a ejecutar al hacer clic en el botón
                            cursor="hand2",  # Cambiar el cursor al pasar sobre el botón
                            width=14,  # Ancho del botón
                        )
                        BotonoCerrarPrograma.place(x=540, y=440)  # Posicionar el botón en la ventana

                        BotonRetroceder = Button(
                            VentanaPostres,
                            text="Retroceder",  # Texto del botón
                            width=10,  # Ancho del botón
                            cursor="hand2",  # Cambiar el cursor al pasar sobre el botón
                            command=mostrar_ventana_Principal_Chef,  # Función a ejecutar al hacer clic en el botón
                        )
                        BotonRetroceder.place(x=400, y=120)  # Posicionar el botón en la ventana

                        # datos postres
                        datos_De_Postres = postre.CargarPostres()  # Obtener los datos de los postres

                        encabezadosPostres = (
                            "id",
                            "nombre",
                            "precio",
                            "tamaño",
                            "ingredientes",
                            "disponibilidad",
                        )  # Encabezados de las columnas de la tabla

                        anchos_Postres = [
                            100,
                            300,
                            200,
                            200,
                            500,
                            100,
                        ]  # Anchura personalizada para cada columna en la tabla

                        marco2 = Frame(VentanaPostres)
                        marco2.pack(side=BOTTOM, padx=0, pady=90)

                        scroll_horizontal = Scrollbar(marco2, orient=HORIZONTAL)
                        scroll_horizontal.pack(side=BOTTOM, fill=X)

                        def crear_tabla(datos, encabezados, anchos_columnas):
                            tablita = Treeview(
                                marco2,
                                show="headings",
                                xscrollcommand=scroll_horizontal.set,
                            )
                            tablita["columns"] = encabezados
                            estilo = ThemedStyle(marco2)
                            estilo.set_theme("scidgrey")
                            estilo.configure(
                                "Custom.Treeview",
                                background="#081118",
                                foreground="#FFFFFF",
                                fieldbackground="#081118",
                                font=("Roboto", 10),
                                bordercolor="#1E1E1E",
                                selectbackground="#2979FF",
                                selectforeground="",
                            )
                            estilo.configure(
                                "Custom.Treeview.Heading",
                                background="#1E1E1E",
                                foreground="#081118",
                                font=("Roboto", 9, "bold"),
                            )
                            tablita.configure(style="Custom.Treeview")
                            tablita.tag_configure(
                                "Custom.Treeview.Heading",
                                background="#212121",
                                foreground="#081118",
                            )
                            DatosTabla = zip(
                                tablita["columns"], encabezados, anchos_columnas
                            )
                            for columna, encabezado, ancho in DatosTabla:
                                tablita.column(columna, width=ancho, stretch=False)
                                tablita.heading(columna, text=encabezado, anchor=CENTER)
                            for dato in datos:
                                tablita.insert("", END, values=dato)
                            tablita.pack(side=LEFT, fill=Y)
                            scroll_horizontal.config(command=tablita.xview)
                            tablita.config(xscrollcommand=scroll_horizontal.set)

                        crear_tabla(
                            datos_De_Postres, encabezadosPostres, anchos_Postres
                        ) # Funcion que le pasan argumentos para la creacion de la tabla .
                       
                        
                    postre2()  # llamo  a la función postre2()

                Button(
                    ventanaChef,  # Ventana en la que se muestra el botón
                    text="Postres",  # Texto que se muestra en el botón
                    width=10,  # Ancho del botón
                    cursor="hand2",  # Cambiar el cursor al pasar sobre el botón
                    command=Postres,  # Función a ejecutar al hacer clic en el botón
                ).place(x=400, y=120)  # Posicionar el botón en la ventana en la posición (400, 120)


                def Bebidas():
                    # Se destruye la ventana actual (ventanaChef)
                    ventanaChef.destroy()

                    def bebida2():
                        # Se define la función bebida2 que muestra la ventana de bebidas
                        global VentanaBebidas
                        VentanaBebidas = Tk()  # Se crea una nueva instancia de la ventana
                        VentanaBebidas.title("Usuario")  # Se establece el título de la ventana
                        VentanaBebidas.geometry("700x500+500+50")  # Se define la geometría de la ventana (ancho x alto + posición x + posición y)
                        VentanaBebidas.configure(background=pantllaColor)  # Se establece el color de fondo de la ventana
                        VentanaBebidas.resizable(width=False, height=False)  # Se desactiva la posibilidad de redimensionar la ventana en ancho y alto

                        # Etiqueta de texto  de nuestra ventana
                        Label(
                            VentanaBebidas,
                            text="DESHABILITAR-HABILITAR",
                            font=30,
                            background=pantllaColor,
                            foreground="#00fcf1",
                        ).pack()

                        def capturadoIDHabiliar():
                            # Función para capturar el ID y habilitar la bebida correspondiente
                            ID = CajaID.get()

                            if ID.isdigit():
                                # Si el ID es un número, se procede a habilitar la bebida
                                bebida.id = ID
                                bebida.HabilitarBebida()
                                VentanaBebidas.destroy()
                                bebida2()
                            elif ID == "":
                                # Si el ID está vacío, se muestra un mensaje de error
                                mensaje3.config(text="Por favor, ingrese un ID válido.")
                            else:
                                # Si el ID no es un número, se muestra un mensaje de error y se limpia la entrada
                                mensaje3.config(text="Error. Por favor, ingrese un ID numérico válido.")
                                CajaID.delete(0, END)
                            return

                        def capturadoIDdesabilitar():
                            # Función para capturar el ID y deshabilitar la bebida correspondiente
                            ID = CajaID.get()

                            if ID.isdigit():
                                # Si el ID es un número, se procede a deshabilitar la bebida
                                bebida.id = ID
                                bebida.DeshabilitarBebida()
                                VentanaBebidas.destroy()
                                bebida2()
                            elif ID == "":
                                # Si el ID está vacío, se muestra un mensaje de error
                                mensaje3.config(text="Por favor, ingrese un ID válido.")
                            else:
                                # Si el ID no es un número, se muestra un mensaje de error y se limpia la entrada
                                mensaje3.config(text="Error. Por favor, ingrese un ID numérico válido.")
                                CajaID.delete(0, END)
                            return


                        mensaje3 = Label(
                            VentanaBebidas,  # Se especifica la ventana padre donde se mostrará el widget
                            background=pantllaColor,  # Se establece el color de fondo del widget
                            foreground="#00fcf1",  # Se establece el color del texto del widget
                            fg="red"
                        )
                        mensaje3.place(x=260, y=95)  # Se posiciona el widget en la ventana en la coordenada (260, 95)

                        Label(
                            VentanaBebidas,
                            text="ID:",  # Texto que se mostrará en la etiqueta
                            font=5,  # Tamaño de fuente
                            pady=10,  # Espacio vertical interno en píxeles
                            background=pantllaColor,  # Color de fondo de la etiqueta
                            foreground="#00fcf1",  # Color del texto de la etiqueta
                        ).place(x=235, y=50)  # Posición (x, y) donde se colocará la etiqueta en la ventana

                        CajaID = Entry(
                            VentanaBebidas,
                            bg=pantllaColor,  # Color de fondo de la entrada
                            foreground="#00fcee",  # Color del texto de la entrada
                            font=("calibri", 10),  # Tamaño y fuente del texto de la entrada
                        )
                        CajaID.place(x=270, y=64)  # Posición (x, y) donde se colocará la entrada en la ventana
                        CajaID.configure(
                            highlightthickness=2, highlightbackground="#00fcee"
                        )  # Configuración adicional de la entrada

                        BotonHabilitar = Button(
                            VentanaBebidas,
                            text="Habilitar✅",  # Texto que se mostrará en el botón
                            width=13,  # Ancho del botón en caracteres
                            cursor="hand2",  # Cambia el cursor al pasar por encima del botón
                            command=capturadoIDHabiliar,  # Función que se ejecutará al hacer clic en el botón
                        )
                        BotonHabilitar.place(x=290, y=120)  # Posición (x, y) donde se colocará el botón en la ventana

                        BotonDesabilitar = Button(
                            VentanaBebidas,
                            text="Desabilitar❎",  # Texto que se mostrará en el botón
                            width=13,  # Ancho del botón en caracteres
                            cursor="hand2",  # Cambia el cursor al pasar por encima del botón
                            command=capturadoIDdesabilitar,  # Función que se ejecutará al hacer clic en el botón
                        )
                        BotonDesabilitar.place(x=180, y=120)  # Posición (x, y) donde se colocará el botón en la ventana

                        def salirChef():
                            VentanaBebidas.destroy()  # Cierra la ventana VentanaBebidas

                        BotonoCerrarPrograma = Button(
                            VentanaBebidas,
                            text="Cerrar programa",  # Texto que se mostrará en el botón
                            command=salirChef,  # Función que se ejecutará al hacer clic en el botón
                            cursor="hand2",  # Cambia el cursor al pasar por encima del botón
                            width=14,  # Ancho del botón en caracteres
                        )
                        BotonoCerrarPrograma.place(x=540, y=440)  # Posición (x, y) donde se colocará el botón en la ventana

                        BotonRetroceder = Button(
                            VentanaBebidas,
                            text="Retroceder",  # Texto que se mostrará en el botón
                            width=10,  # Ancho del botón en caracteres
                            cursor="hand2",  # Cambia el cursor al pasar por encima del botón
                            command=mostrar_ventana_Principal_Chef2,  # Función que se ejecutará al hacer clic en el botón
                        )
                        BotonRetroceder.place(x=400, y=120)  # Posición (x, y) donde se colocará el botón en la ventana

                        DatosBebidas = bebida.CargarBebidas()  # Carga los datos de las bebidas

                        encabezadosBebidas = (
                            "id",
                            "nombre",
                            "precio",
                            "tamaño",
                            "disponibilidad",
                        )  # Encabezados de las columnas de la tabla

                        anchos_Bebidas = [
                            100,
                            200,
                            200,
                            200,
                            100,
                        ]  # Anchura personalizada para cada columna en la tabla

                        marco2 = Frame(VentanaBebidas)  # Se crea un marco en la ventana VentanaBebidas
                        marco2.pack(side=BOTTOM, padx=0, pady=90)  # Se coloca el marco en la parte inferior de la ventana con relleno

                        scroll_horizontal = Scrollbar(marco2, orient=HORIZONTAL)  # Se crea una barra de desplazamiento horizontal
                        scroll_horizontal.pack(side=BOTTOM, fill=X)  # Se coloca la barra de desplazamiento en la parte inferior del marco, ocupando todo el ancho disponible


                        def crear_tabla(datos, encabezados, anchos_columnas):
                            tablita = Treeview(
                                marco2,  # Se crea un Treeview en el marco2
                                show="headings",  # Se muestran solo los encabezados
                                xscrollcommand=scroll_horizontal.set,  # Se asigna la barra de desplazamiento horizontal al Treeview
                            )
                            tablita["columns"] = encabezados  # Se establecen las columnas del Treeview
                            estilo = ThemedStyle(marco2)  # Se crea un estilo temático para el Treeview
                            estilo.set_theme("scidgrey")  # Se establece el tema "scidgrey" para el estilo
                            estilo.configure(
                                "Custom.Treeview",  # Estilo personalizado para el Treeview
                                background="#081118",  # Color de fondo de las celdas
                                foreground="#FFFFFF",  # Color del texto de las celdas
                                fieldbackground="#081118",  # Color de fondo de los campos
                                font=("Roboto", 10),  # Fuente del texto
                                bordercolor="#1E1E1E",  # Color del borde
                                selectbackground="#2979FF",  # Color de fondo de la selección
                                selectforeground="",  # Color del texto de la selección
                            )
                            estilo.configure(
                                "Custom.Treeview.Heading",  # Estilo personalizado para los encabezados
                                background="#1E1E1E",  # Color de fondo de los encabezados
                                foreground="#081118",  # Color del texto de los encabezados
                                font=("Roboto", 9, "bold"),  # Fuente del texto de los encabezados
                            )
                            tablita.configure(style="Custom.Treeview")  # Se aplica el estilo personalizado al Treeview
                            tablita.tag_configure(
                                "Custom.Treeview.Heading",  # Se configura el estilo para los encabezados
                                background="#212121",  # Color de fondo de los encabezados
                                foreground="#081118",  # Color del texto de los encabezados
                            )
                            # Configuración de las columnas y encabezados del Treeview
                            DatosTabla = zip(tablita["columns"], encabezados, anchos_columnas)
                            for columna, encabezado, ancho in DatosTabla:
                                tablita.column(columna, width=ancho, stretch=False)
                                tablita.heading(columna, text=encabezado, anchor=CENTER)
                            # Inserción de los datos en el Treeview
                            for dato in datos:
                                tablita.insert("", END, values=dato)
                            tablita.pack(side=LEFT, fill=Y)  # Se coloca el Treeview en el marco2, a la izquierda con relleno en el eje Y
                            scroll_horizontal.config(command=tablita.xview)  # Se configura la barra de desplazamiento horizontal para controlar el desplazamiento del Treeview
                            tablita.config(xscrollcommand=scroll_horizontal.set)  # Se establece la barra de desplazamiento horizontal para el Treeview

                        crear_tabla(DatosBebidas, encabezadosBebidas, anchos_Bebidas)  # Se llama a la función crear_tabla con los datos de las bebidas

                    bebida2()  #Se llama a la funcion que contiene la informacion comentada en el apartado en la interfaz del chef

                Button(
                    ventanaChef,
                    text="Bebidas",
                    width=10,
                    cursor="hand2",
                    command=Bebidas,
                ).place(x=500, y=120)  # Botón para acceder a la sección de bebidas

                def salirChef():
                    ventanaChef.destroy()  # Función para cerrar la ventana del chef

                BotonCerrarPrograma = Button(
                    ventanaChef,
                    text="Cerrar programa",
                    command=salirChef,
                    cursor="hand2",
                    width=14,
                )
                BotonCerrarPrograma.place(x=540, y=440)  # Botón para cerrar el programa del chef

                datos_originales = pedido.CargarPedido()  # Carga los datos originales de los pedidos

                encabezados_originales = (
                    "id",
                    "comidas",
                    "bebidas",
                    "Postres",
                    "cantidad de comida",
                    "cantidad de bebidas",
                    "cantidad de postres",
                    "total",
                    "fechas",
                    "Estado",
                )  # Encabezados de la tabla original

                anchos_columnas_originales = [
                    100,
                    300,
                    300,
                    300,
                    150,
                    150,
                    150,
                    200,
                    200,
                    100,
                ]  # Anchuras personalizadas para cada columna en la tabla original

                marco2 = Frame(ventanaChef)
                marco2.pack(side=BOTTOM, padx=0, pady=90)  # Marco para la tabla y la barra de desplazamiento

                scroll_horizontal = Scrollbar(marco2, orient=HORIZONTAL)
                scroll_horizontal.pack(side=BOTTOM, fill=X)  # Barra de desplazamiento horizontal

                def crear_tabla(datos, encabezados, anchos_columnas):
                    tablita = Treeview(
                        marco2,
                        show="headings",
                        xscrollcommand=scroll_horizontal.set,
                    )  # Se crea un Treeview en el marco2
                    tablita["columns"] = encabezados  # Se establecen las columnas del Treeview

                    # Estilos personalizados para el Treeview y los encabezados
                    estilo = ThemedStyle(marco2)
                    estilo.set_theme("scidgrey")
                    estilo.configure(
                        "Custom.Treeview",
                        background="#081118",
                        foreground="#FFFFFF",
                        fieldbackground="#081118",
                        font=("Roboto", 10),
                        bordercolor="#1E1E1E",
                        selectbackground="#2979FF",
                        selectforeground="",
                    )
                    estilo.configure(
                        "Custom.Treeview.Heading",
                        background="#1E1E1E",
                        foreground="#081118",
                        font=("Roboto", 9, "bold"),
                    )
                    tablita.configure(style="Custom.Treeview")  # Se aplica el estilo personalizado al Treeview
                    tablita.tag_configure(
                        "Custom.Treeview.Heading",
                        background="#212121",
                        foreground="#081118",
                    )  # Se configura el estilo para los encabezados

                    # Configuración de las columnas y encabezados del Treeview
                    DatosTabla = zip(tablita["columns"], encabezados, anchos_columnas)
                    for columna, encabezado, ancho in DatosTabla:
                        tablita.column(columna, width=ancho, stretch=False)
                        tablita.heading(columna, text=encabezado, anchor=CENTER)

                    # Inserción de los datos en el Treeview
                    for dato in datos:
                        tablita.insert("", END, values=dato)
                    tablita.pack(side=LEFT, fill=Y)  # Se coloca el Treeview en el marco2, a la izquierda con relleno en el eje Y
                    scroll_horizontal.config(command=tablita.xview)  # Se configura la barra de desplazamiento horizontal para controlar el desplazamiento del Treeview
                    tablita.config(xscrollcommand=scroll_horizontal.set)  # Se establece la barra de desplazamiento horizontal para el Treeview

                crear_tabla(
                    datos_originales, encabezados_originales, anchos_columnas_originales
                )  # Se llama a la función crear_tabla con  sus repectivos datos,anchos y encabezados

                ventanaChef.mainloop()  # se inicia  la ejecución del programa y mostrara la interfaz al usuario Chef.

            def mostrar_ventana_Principal_Chef():
                VentanaPostres.destroy()
                construir_ventana_principal()  # Función para mostrar la ventana principal del chef y destruir la ventana de postres

            def mostrar_ventana_Principal_Chef1():
                ventanaComida.destroy()
                construir_ventana_principal()  # Función para mostrar la ventana principal del chef y destruir la ventana de comidas

            def mostrar_ventana_Principal_Chef2():
                VentanaBebidas.destroy()
                construir_ventana_principal()  # Función para mostrar la ventana principal del chef y destruir la ventana de bebidas

            
            

            construir_ventana_principal()

        # -----------------------------------------------------------------------------------------------------------------------------------------

        inciarSeccion = Label(
            ventana, # Ventana en la que se va a colocar la etiqueta
            text="INICIAR SESSION", # Texto que se muestra en la etiqueta
            font=("Tahoma", 20, "bold"),# Fuente y tamaño del texto de la etiqueta
            bg=pantllaColor,# Color de fondo de la etiqueta
            foreground="#00fcee" # Color del texto de la etiqueta
        )
        inciarSeccion.place(x=125, y=40)         # Posición (coordenadas x, y) donde se coloca la etiqueta en la ventana

        usuariotext = Label(
            ventana, # Ventana en la que se va a colocar la etiqueta
            text="Usuario", # Texto que se muestra en la etiqueta
            font=16,# Tamaño de fuente de la etiqueta
            bg=pantllaColor,  # Color de fondo de la etiqueta
            foreground="#00fcee"  # Color del texto de la etiqueta
        )
        usuariotext.place(x=210, y=110) # Posición (coordenadas x, y) donde se coloca la etiqueta en la ventana


        entrada1 = Entry(
            ventana,      # Ventana en la que se va a colocar la entrada de texto
            width=22,     # Ancho de la entrada de texto
            relief="flat",# Estilo del borde de la entrada de texto
            bg=pantllaColor,# Color de fondo de la entrada de texto
            foreground="#00fcee", # Color del texto de la entrada de texto
            font=("calibri", 10) # Fuente del texto de la entrada de texto
        )
        entrada1.configure(highlightthickness=2, highlightbackground="#00fcee") # Configuración del grosor y color del resaltado de la entrada de texto
        entrada1.place(x=170, y=150)  # Posición (coordenadas x, y) donde se coloca la entrada de texto en la ventana

        paswordtxt = Label(
            ventana, # Ventana en la que se va a colocar la etiqueta
            text="Password", # Texto que se muestra en la etiqueta
            font=16,  # Tamaño de fuente de la etiqueta
            bg=pantllaColor,# Color de fondo de la etiqueta
            foreground="#00fcee" # Color del texto de la etiqueta
        )
        paswordtxt.place(x=200, y=190) # Posición (coordenadas x, y) donde se coloca la etiqueta en la ventana

        entrada2 = Entry(
            ventana, # Ventana en la que se va a colocar la entrada de texto
            show="•", # Carácter que se muestra en lugar del texto (en este caso, un punto para ocultar la contraseña)
            width=22, # Ancho de la entrada de texto
            relief="flat", # Estilo del borde de la entrada de texto
            bg=pantllaColor, # Color de fondo de la entrada de texto
            foreground="#00fcee", # Color del texto de la entrada de texto
            font=("calibri", 10) # Fuente del texto de la entrada de texto
        )
        entrada2.configure(highlightthickness=2, highlightbackground="#00fcee")  # Configuración del grosor y color del resaltado de la entrada de texto
        entrada2.place(x=170, y=230)        # Posición (coordenadas x, y) donde se coloca la entrada de texto en la ventana

        def salir():
            ventana.destroy()               # Función que se ejecuta cuando se hace clic en el botón "Salir". Destruye la ventana y finaliza el programa


        # Botones,el cursor va a cambiar a una mano
        boton1 = Button(
            ventana,        # Ventana en la que se va a colocar el botón
            text="Ingresar", # Texto que se muestra en el botón
            command=logiin,  # Función que se ejecuta cuando se hace clic en el botón
            cursor="hand2",   # Cursor que se muestra al pasar el ratón sobre el botón
            bg=fondo_entrar,     # Color de fondo del botón
            width=12,    # Ancho del botón
            font=("Calibre", 12, "bold") # Fuente del texto del botón
        )

        boton1.place(x=60, y=405) # Posición (coordenadas x, y) donde se coloca el botón en la ventana

        boton2 = Button(
            ventana, # Ventana en la que se va a colocar el botón
            text="Salir", # Texto que se muestra en el botón
            command=salir, # Función que se ejecuta cuando se hace clic en el botón
            cursor="hand2", # Cursor que se muestra al pasar el ratón sobre el botón
            bg=fondo_salir, # Color de fondo del botón
            width=12,  # Ancho del botón
            font=("Calibre", 12, "bold")#Fuente del texto del botón
        )
        boton2.place(x=310, y=405) # Posición (coordenadas x, y) donde se coloca el botón en la ventana
        ventana.mainloop()  # Inicia el bucle principal de la interfaz gráfica o 
                            # se inicia  la ejecución del programa y mostrara la interfaz al usuario.
