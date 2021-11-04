class Personas:
    def __init__(self, nombre, apellidos, telefono, direccion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.direccion = direccion

    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos

    def getTelefono(self):
        return self.telefono

    def getDireccion(self):
        return self.direccion

    def pintar(self):
        return "{}/{}/{}/{}".format(self.nombre, self.apellidos, self.telefono, self.direccion)

    def __str__(self):
        return "{}/{}/{}/{}".format(self.nombre, self.apellidos, self.telefono, self.direccion)
