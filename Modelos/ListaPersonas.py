from tkinter import *
import pickle
from Modelos.Personas import Personas


class ListaPersonas:
    personas = []

    def __init__(self):
        try:
            listaDePersonas = open("../Datos/personas", "ab+")
            listaDePersonas.seek(0)

            self.personas = pickle.load(listaDePersonas)
            print("He cargado {} personas".format(len(self.personas)))
        except:
            print("Fichero Vacío")
        finally:
            listaDePersonas.close()
            del listaDePersonas

    def guardarPersonasFichero(self):
        listaDePersonas = open("../Datos/personas", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del (listaDePersonas)

    def anadirPersonas(self):
        ventana = Tk()
        ventana.geometry("300x200")
        ventana.configure(bg='grey')

        etiquetaNombre = Label(ventana, text="Nombre")
        etiquetaNombre.configure(bg='grey')
        etiquetaNombre.pack()

        nombre = Entry(ventana)
        nombre.pack()

        etiquetaApe = Label(ventana, text="Apellidos")
        etiquetaApe.configure(bg='grey')
        etiquetaApe.pack()

        apellidos = Entry(ventana)
        apellidos.pack()

        etiquetaTelef = Label(ventana, text="Telefono")
        etiquetaTelef.configure(bg='grey')
        etiquetaTelef.pack()

        telefono = Entry(ventana)
        telefono.pack()

        etiquetaDir = Label(ventana, text="Dirección")
        etiquetaDir.configure(bg='grey')
        etiquetaDir.pack()

        direccion = Entry(ventana)
        direccion.pack()

        def anadirPersonasCl():
            auxNom = nombre.get()
            auxApe = apellidos.get()
            auxTelf = telefono.get()
            auxDir = direccion.get()

            c1 = Personas(auxNom, auxApe, auxTelf, auxDir)
            self.personas.append(c1)
            self.guardarPersonasFichero()
            ventana.destroy()

        boton = Button(ventana, text="Anadir Persona", command=anadirPersonasCl)
        boton.pack()

        ventana.title("Añadir Persona")
        ventana.mainloop()

    def mostrarPersonas(self):
        for item in self.personas:
            print(item)

    def leeFicheroPersonas(self):
        ficheroBinario = open("../Datos/personas", "rb")
        lista = pickle.load(ficheroBinario)
        ficheroBinario.close()
        aux = ""
        i = 1
        del (ficheroBinario)
        for itempersonas in lista:
            aux = aux + str(i) + " " + itempersonas.pintar() + "\n"
            i = i + 1
        return aux

    def borrarPersona(self):
        ventana = Tk()
        ventana.geometry("250x100")
        ventana.configure(bg='grey')

        etiquetaNombre = Label(ventana, text="ID De Persona")
        etiquetaNombre.configure(bg='grey')
        etiquetaNombre.pack()

        posicion = Entry(ventana)
        posicion.pack()

        def borraPersonaPosicion():
            if posicion.get() != "":
                tamanioArray = len(self.personas)
                poss = int(posicion.get())
                poss = poss - 1
                if poss <= tamanioArray:
                    self.personas.pop(poss)
                    self.guardarPersonasFichero()
                    ventana.destroy()

        boton = Button(ventana, text="Borrar", command=borraPersonaPosicion)
        boton.pack()

        ventana.title("Borrar Persona")
        ventana.mainloop()

    def modificarPersona(self, p, ventanaPrincipal):
        if p != "":
            tamanioArray = len(self.personas)
            poss = int(p)
            poss = poss - 1

            ventana = Tk()
            ventana.geometry("250x200")
            ventana.configure(bg='grey')

            if poss <= tamanioArray and poss >= 0:
                persona = self.personas[poss]
                ventanaPrincipal.destroy()
                cNombre = persona.getNombre()
                cApe = persona.getApellidos()
                cTelef = persona.getTelefono()
                cDir = persona.getDireccion()

                etiquetaNombre = Label(ventana, text="Nombre")
                etiquetaNombre.configure(bg='grey')
                etiquetaNombre.pack()

                nombre = Entry(ventana)
                nombre.insert(END, cNombre)
                nombre.pack()

                etiquetaApe = Label(ventana, text="Apellidos")
                etiquetaApe.configure(bg='grey')
                etiquetaApe.pack()

                apellidos = Entry(ventana)
                apellidos.insert(END, cApe)
                apellidos.pack()

                etiquetaTelef = Label(ventana, text="Telefono")
                etiquetaTelef.configure(bg='grey')
                etiquetaTelef.pack()

                telefono = Entry(ventana)
                telefono.insert(END, cTelef)
                telefono.pack()

                etiquetaDir = Label(ventana, text="Dirección")
                etiquetaDir.configure(bg='grey')
                etiquetaDir.pack()

                direccion = Entry(ventana)
                direccion.insert(END, cDir)
                direccion.pack()

                def modPersona():
                    self.personas.pop(poss)
                    c1 = Personas(nombre.get(), apellidos.get(), telefono.get(), direccion.get())
                    self.personas.insert(poss, c1)
                    self.guardarPersonasFichero()
                    ventana.destroy()
                    ventana2 = Tk();
                    ventana2.geometry("100x70")
                    ventana2.configure(bg='grey')
                    etiquetaNombre = Label(ventana2, text="Persona Modificado")
                    etiquetaNombre.pack()

                    def errMod():
                        ventana2.destroy()

                    boton = Button(ventana2, text="Aceptar", command=errMod)
                    boton.pack()

                    ventana2.title("Modificado")
                    ventana2.mainloop()

                boton = Button(ventana, text="Modificar Persona", command=modPersona)
                boton.pack()

                ventana.title("Modificar Persona")
                ventana.configure(bg='grey')
                ventana.mainloop()
            else:
                ventana.geometry("300x70")
                ventana.configure(bg='grey')
                etiquetaNombre = Label(ventana, text="Error al Cargar la Persona")
                etiquetaNombre.configure(bg='grey')
                etiquetaNombre.pack()

                def errMod():
                    ventana.destroy()

                boton = Button(ventana, text="Cerrar", command=errMod)
                boton.pack()
                ventana.title("Error al Cargar Persona")
                ventana.mainloop()
