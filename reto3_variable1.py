#NO ELIMINAR LA SIGUIENTE IMPORTACIÓN, sirve para probar tu código en consola
#from pruebas import pruebas_codigo_estudiante

#NOTA: PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
#LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO

#En este espacio podrás programar las funciones que deseas usar en la función solución (NO ES OBLIGATORIO CREAR OTRAS FUNCIONES)
"""Inicio espacio para programar funciones propias"""

equivalencias = {
"A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", "F":"..-.", "G":"--.", "H":"....", "I":"..", "J":".---", "K":"-.-", "L":".-..", "M":"--", "N":"-.", "O":"---", "P":".--.", "Q":"--.-",
"R":".-.", "S":"...", "T":"-", "U":"..-", "V":"...-", "W":".--", "X":"-..-", "Y":"-.--", "Z":"--..", " ":"/",
}

def caracter_plano(caracter):
    if caracter in equivalencias:
        return equivalencias[caracter]
    else:
        return caracter    


#PUEDES PROGRAMAR CUANTAS FUNCIONES DESEES 


"""Fin espacio para programar funciones propias"""

def traductor_a_morse(mensaje_a_traducir):
    #PROGRAMA ACÁ TU SOLUCIÓN
    texto = mensaje_a_traducir
    mensaje_a_traducir = mensaje_a_traducir.upper()
    mensaje_traducido = ""
    tamano = len(texto)
    for caracter in (mensaje_a_traducir):
        tamano = tamano - 1
        if caracter in equivalencias:
            if tamano != 1:
                caracter_codificado = caracter_plano(caracter)
                mensaje_traducido += caracter_codificado +" "
            else:
                caracter_codificado = caracter_plano(caracter)
                mensaje_traducido += caracter_codificado +""
        else:
            caracter_codificado = caracter_plano(caracter)
            mensaje_traducido += caracter_codificado +""
    return mensaje_traducido

palabra = "'HOLA MUNDO'"
convertido_morse = traductor_a_morse(palabra)
print("ENTRADA:", palabra)
print("MI SALIDA:", convertido_morse)

"""
Esta línea de código que sigue, permite probar si su ejercicio es correcto
"""
#NO ELIMINAR LA SIGUIENTE LÍNEA DE CÓDIGO
#pruebas_codigo_estudiante(traductor_a_morse)