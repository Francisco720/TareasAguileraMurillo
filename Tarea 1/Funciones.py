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


# Funcion: num_to_str
# Entradas: Un número
# Salidas: Una string con el número conventido a letras
# Restricciones: La entrada debe de ser un número >= 0 y <= 99
""" Descripción: Verifica que la entrada sea un número entre 0 y 99,
    y la salida es ese número convertido a letras, en caso de no
    cumplirse lo primero se retorna un código de error."""


def num_to_str(ifnum):
    # Tupla con los números del 0 al 9 convertidos a letras
    unidades_str = (
        'cero',
        'uno',
        'dos',
        'tres',
        'cuatro',
        'cinco',
        'seis',
        'siete',
        'ocho',
        'nueve'
    )

    # Tupla con los números del 10 al 19 convertidos a letras
    decenas_10_str = (
        'diez',
        'once',
        'doce',
        'trece',
        'catorce',
        'quince',
        'dieciseis',
        'diecisiete',
        'dieciocho',
        'diecinueve'
    )
    # Tupla con los números del 20 al 29 convertidos a letras
    decenas_20_str = (
        'veinte',
        'veintiuno',
        'veintidos',
        'veintitres',
        'veinticuatro',
        'veinticinco',
        'veintiseis',
        'veintisiete',
        'veintiocho',
        'veintinueve'
    )

    # Tupla con los números de 10 en 10 hasta 90 convertidos a letras
    decenas_str = (
        'treinta',
        'cuarenta',
        'cincuenta',
        'sesenta',
        'setenta',
        'ochenta',
        'noventa'
    )

    # Se verifica que la entrada sea un número
    if isinstance(ifnum, int) or isinstance(ifnum, float):
        # Se divide el número en unidades y decenas
        unidades = ifnum % 10
        # Se resta 3 porque la tupla de decenas empieza en 30
        decenas = (ifnum // 10) - 3

        # Si el número esta entre 0 y 9 se utiliza la tupla de unidades_str y
        # las unidades como índice
        if ifnum >= 0 and ifnum <= 9:
            return unidades_str[unidades]

        # Si el número esta entre 10 y 19 se utiliza la tupla de decenas_10_str
        # y las unidades como índice
        elif ifnum >= 10 and ifnum <= 19:
            return decenas_10_str[unidades]

        # Si el número esta entre 20 y 29 se utiliza la tupla de decenas_20_str
        # y las unidades como índice
        elif ifnum >= 20 and ifnum <= 29:
            return decenas_20_str[unidades]

        # Si el número esta entre 30 y 99 se utiliza la tupla de decenas_str
        # con decenas como índice y unidades_str con unidades como índice
        elif ifnum >= 30 and ifnum <= 99:
            # Excepción para múltiplos de 10
            if unidades == 0:
                return decenas_str[decenas]
            else:
                # Se concatenan las decenas y las unidades
                str_num = decenas_str[decenas] + "_y_" + unidades_str[unidades]
                return str_num

        else:
            # Código de error por si la entrada no esta entre 0 y 99
            return "Error: 0x0B"
    else:
        # Código de error por si la entrada no es un número
        return "Error: 0x57"
