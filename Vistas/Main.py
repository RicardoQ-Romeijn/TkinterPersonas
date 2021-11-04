from tkinter import *
from Modelos.ListaPersonas import ListaPersonas

def ventanaPrincipal():
    ventana = Tk()
    ventana.geometry("275x200")

    etiquetaAddClient = Label(ventana, text="Añadir Persona")
    etiquetaAddClient.configure(bg='grey')
    etiquetaAddClient.pack()

    botonAdd = Button(ventana, text="Anadir Persona", command=anadirPersonasVentana)
    botonAdd.pack()

    etiquetaDelPersona = Label(ventana, text="Borra Persona")
    etiquetaDelPersona.configure(bg='grey')
    etiquetaDelPersona.pack()

    boton = Button(ventana, text="Borra Persona", command=borrarPersonasVentana)
    boton.pack()

    etiquetaListPersona = Label(ventana, text="Listar Personas")
    etiquetaListPersona.configure(bg='grey')
    etiquetaListPersona.pack()

    boton = Button(ventana, text="Listar Personas", command=listarPersonasVentana)
    boton.pack()

    etiquetaModPersona = Label(ventana, text="Modificar Persona")
    etiquetaModPersona.configure(bg='grey')
    etiquetaModPersona.pack()

    boton = Button(ventana, text="Modificar Persona", command=modificarPersonaVentana)
    boton.pack()

    ventana.title("Interfaz Gráfica")
    ventana.configure(bg='grey')
    ventana.mainloop()


def anadirPersonasVentana():
    list = ListaPersonas()
    list.anadirPersonas()


def borrarPersonasVentana():
    list = ListaPersonas()
    list.borrarPersona()


def listarPersonasVentana():
    list = ListaPersonas()
    aux = list.leeFicheroPersonas()

    ventana = Tk()
    ventana.geometry("400x400")
    ventana.configure(bg='grey')

    etiquetaaddClient = Label(ventana, text="Personas")
    etiquetaaddClient.configure(bg='grey')
    etiquetaaddClient.pack()

    texto = Text(ventana, height=50, width=100)
    texto.insert(END, aux)
    texto.configure(state="disabled")
    texto.pack()

    ventana.title("Listado Personas")
    ventana.mainloop()


def modificarPersonaVentana():
    list = ListaPersonas()
    ventana = Tk()
    ventana.geometry("250x100")
    ventana.configure(bg='grey')

    etiquetaNombre = Label(ventana, text="ID de Persona a Modificar")
    etiquetaNombre.configure(bg='grey')
    etiquetaNombre.pack()

    posicion = Entry(ventana)
    posicion.pack()

    boton = Button(ventana, text="Ver Datos de Persona", command=lambda: list.modificarPersona(posicion.get(), ventana))
    boton.pack()

    ventana.title("Buscar")
    ventana.mainloop()

ventanaPrincipal()