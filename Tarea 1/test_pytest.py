# Elaborado por: Francisco Aguilera y Jimena Murillo
# Fecha de Creación: 15/02/2022 10:00
# Fecha de última Modificación: 18/2/2022 1:00
# Versión: 3.10.2

# se importan las funciones string_work y num_to_str.
from Funciones import string_work
from Funciones import num_to_str

# función que verifica si string_work cambia todos los caracteres.


def test_string_work_input_abc():
    abc = "abcdefghijklmnopqrstuvwxyz"
    ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(26):
        assert string_work(abc[i]) == ABC[i]
        assert string_work(ABC[i]) == abc[i]

# función que verifica si string_work retorna el error correcto
# si se le pasa un número como entrada.


def test_string_work_input_int():
    assert string_work(630) == "Error: 0x4A"

# función que verifica si string_work retorna el error correcto
# si se le pasa un string con números y/o símbolos.


def test_string_work_input_str_int_sym():
    assert string_work("H01a") == "Error: 0xAF"
    assert string_work("Ho!a") == "Error: 0xAF"

# función que verifica si num_to_str traduce los números del 0 al 99.


def test_num_to_str_input_int():
    num_str = (
        'cero', 'uno',
        'dos', 'tres',
        'cuatro', 'cinco',
        'seis', 'siete',
        'ocho', 'nueve',
        'diez', 'once',
        'doce', 'trece',
        'catorce', 'quince',
        'dieciseis', 'diecisiete',
        'dieciocho', 'diecinueve',
        'veinte', 'veintiuno',
        'veintidos', 'veintitres',
        'veinticuatro', 'veinticinco',
        'veintiseis', 'veintisiete',
        'veintiocho', 'veintinueve',
        'treinta', 'treinta_y_uno',
        'treinta_y_dos', 'treinta_y_tres',
        'treinta_y_cuatro', 'treinta_y_cinco',
        'treinta_y_seis', 'treinta_y_siete',
        'treinta_y_ocho', 'treinta_y_nueve',
        'cuarenta', 'cuarenta_y_uno',
        'cuarenta_y_dos', 'cuarenta_y_tres',
        'cuarenta_y_cuatro', 'cuarenta_y_cinco',
        'cuarenta_y_seis', 'cuarenta_y_siete',
        'cuarenta_y_ocho', 'cuarenta_y_nueve',
        'cincuenta', 'cincuenta_y_uno',
        'cincuenta_y_dos', 'cincuenta_y_tres',
        'cincuenta_y_cuatro', 'cincuenta_y_cinco',
        'cincuenta_y_seis', 'cincuenta_y_siete',
        'cincuenta_y_ocho', 'cincuenta_y_nueve',
        'sesenta', 'sesenta_y_uno',
        'sesenta_y_dos', 'sesenta_y_tres',
        'sesenta_y_cuatro', 'sesenta_y_cinco',
        'sesenta_y_seis', 'sesenta_y_siete',
        'sesenta_y_ocho', 'sesenta_y_nueve',
        'setenta', 'setenta_y_uno',
        'setenta_y_dos', 'setenta_y_tres',
        'setenta_y_cuatro', 'setenta_y_cinco',
        'setenta_y_seis', 'setenta_y_siete',
        'setenta_y_ocho', 'setenta_y_nueve',
        'ochenta', 'ochenta_y_uno',
        'ochenta_y_dos', 'ochenta_y_tres',
        'ochenta_y_cuatro', 'ochenta_y_cinco',
        'ochenta_y_seis', 'ochenta_y_siete',
        'ochenta_y_ocho', 'ochenta_y_nueve',
        'noventa', 'noventa_y_uno',
        'noventa_y_dos', 'noventa_y_tres',
        'noventa_y_cuatro', 'noventa_y_cinco',
        'noventa_y_seis', 'noventa_y_siete',
        'noventa_y_ocho', 'noventa_y_nueve'
    )
    for i in range(100):
        assert num_to_str(i) == num_str[i]

# función que verifica si num_to_str retorna el error correcto
# si se le pasa un string.


def test_num_to_str_input_srt():
    assert num_to_str("101") == "Error: 0x57"

# función que verifica si num_to_str retorna el error correcto
# si se le pasa un número negativo, decimal o mayor a 99.


def test_num_to_str_input_intN_float():
    assert num_to_str(584) == "Error: 0x0B"
    assert num_to_str(-55) == "Error: 0x0B"
    assert num_to_str(9.81) == "Error: 0x0B"
