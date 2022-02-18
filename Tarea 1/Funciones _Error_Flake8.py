# Elaborado por: Francisco Aguilera y Jimena Murillo
# Fecha de Creación: 14/02/2022 11:00
# Fecha de última Modificación: 18/2/2022 1:00
# Versión: 3.10.2

# Funcion: string_work
# Entradas: Una string
# Salidas: Una string con cada carácter invertido de mayúscula
#          a minúscula y viceversa
# Restricciones: La entrada  de ser una string sin ningún número
""" Descripción: Verifica que la entrada sea una string sin números
    y luego se invierte cada carácter de mayúscula a minúscula y
    viceversa, en caso de no cumplirse lo primero se retorna un
    código de error."""


def string_work(ifstr):
    # Se verifica que la entrada sea una string
    if isinstance(ifstr, str):
        # Se verifica que la entrada sean solo letras
        if ifstr.isalpha():
            # Se retorna la entrada con los caracteres invertidos
            return ifstr.swapcase()
        else:
            # Código de error por si la entrada contiene algún número
            return "Error: 0xAF"
    else:
        # Código de error por si la entrada no es una string
        return "Error: 0x4A"
