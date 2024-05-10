from time import process_time

"""
1. Escriba una función redondear() que permita redondear un número
decimal de acuerdo al criterio: Si el número es mayor a 3.50, devolver el
entero siguiente (en este caso, 4), si no devolver el entero inmediatamente
anterior (3).
"""

"""

def redondear(numero): # Consigna

    if numero >= 3.50:
        return int(numero)+1
    
    return int(numero)

def redondearDeVerdad(numero): # Redondeo de verdad
    truncar=int(numero)

    if numero - truncar >= 0.5:
        return truncar+1
    
    return truncar

print(redondearDeVerdad(4.4))

# Tiempo de ejecución: 0.054516

"""

"""
2. Coloque el módulo del ejercicio anterior dentro de un paquete. En un
módulo que esté fuera de ese paquete, cree una función de suma de
decimales que redondee el resultado haciendo uso de la función
redondear() del paquete recién creado.
"""

"""

from Paquetes.Redondear import redondear

def sumarDecimales(numero1, numero2):
    sumar=numero1+numero2
    return redondear.redondearDeVerdad(sumar)

print(sumarDecimales(1.50, 2))

# Tiempo de ejecución: 0.05587

"""

"""
3. Usando el módulo datetime, escribe un programa que muestre la fecha
y hora actuales del sistema.
"""

"""

from datetime import datetime

print(f"Fecha y hora: {datetime.today()}")

# Tiempo de ejecución: 0.064384

"""

"""
4. Escriba un programa que devuelva un número par al azar entre 2 y 10
(pista: para comprobar si se pueden generar todos los números, pruebe
ejecutar el programa dentro de un ciclo infinito)
"""

"""

# Manera ciclica
#
#from random import randint
#from Paquetes.Par import par 
#
#while True:
#    numeroAzar=randint(1,10)
#
#    if par.esPar(numeroAzar):
#        break

# Manera super facil
from random import randrange
numeroAzar=randrange(2,10,2)

print(f"Numero Aleatorio entre 1 y 10 que es par: {numeroAzar}")

# Tiempo de ejecución: 0.067675

"""

"""
5. Bola mágica: La bola mágica (Magic 8 ball) es un popular juguete usado
para la adivinación o para buscar consejo. Su mecanismo es muy simple:
ante una pregunta del usuario, la bola responde con una de 8 posibles
respuestas:
- Es seguro que sí
- Las chances son buenas
- Puedes contar con ello
- Pregúntame de nuevo más tarde
- Concéntrate y pregunta de nuevo
- No veo con claridad, intenta de nuevo
- Mi respuesta es no
- Mis fuentes me dicen que no
Escriba una función en Python para simular la bola mágica.
"""

"""

from random import choice

Frases=(
    "Es seguro que sí",
    "Las chances son buenas",
    "Puedes contar con ello",
    "Pregúntame de nuevo más tarde",
    "Concéntrate y pregunta de nuevo",
    "No veo con claridad, intenta de nuevo",
    "Mi respuesta es no",
    "Mis fuentes me dicen que no",
)

input("Hazle una pregunta a la bola magica: ")
print(f"La bola 8 dice: {choice(Frases)}")

# Tiempo de ejecución: 0.064524

"""

"""
6. Encuentre el tiempo de ejecución de los programas de los ejercicios
anteriores (pista: use el módulo time)
"""

"""

print(process_time())

# Tiempo de todos los modulos hasta el punto 6: 0.076797
# Este valor es aproximado y cambiante, por supuesto.

"""

"""
7 .(Opcional) Sorteo: Escriba un programa que simule un sorteo donde
toman uno o más papeles al azar de un pozo para elegir los ganadores.
"""

"""

import names # pip install names
from time import sleep
from random import randrange
from random import shuffle
from Paquetes.Ganadores import eleccion

print("Bienvenido al simulador de sorteos!")

while True:
    try:
        Participantes=int(input("Ingrese la cantidad de participantes [int]: "))
        NumGanadores=int(input("Ingrese la cantidad de ganadores: "))
        break
    except ValueError:
        print("Numero invalido.")

papelitosConNombres=[]
for i in range(Participantes):
    papelitosConNombres.append(names.get_full_name())

def elegirGanador(elección, cantidadDeGanadores):
    if cantidadDeGanadores > 1:
        Ganadores=[]
        for c in range(cantidadDeGanadores):
            Elegir=elección.pop(randrange(0,len(elección)))
            Ganadores.append(Elegir)
        
        return Ganadores
    else:
        return elección.pop(randrange(0,len(elección)))

print("Participantes inscriptos:")
print(papelitosConNombres)

print("Revolviendo los papelitos...")

shuffle(papelitosConNombres)
sleep(3.5)

print("Recogiendo un papelito sin ver...")
sleep(2)

Ganador=elegirGanador(papelitosConNombres, NumGanadores)

eleccion.imprimirGanador(Ganador)

"""

"""

8. (Opcional) Escriba una función que pida al usuario ingresar su fecha de
nacimiento y sea capaz de devolver la cantidad de días desde su
nacimiento hasta hoy.

"""

from datetime import date
import time

print("Bienvenido al calculador de dias desde su nacimiento!")
print("- Ingrese su fecha de nacimiento -")
Opcion="Año"
while True:
    try:
        match Opcion:
            case "Año":
                Año=int(input("Año: "))
                Opcion="Mes"
            case "Mes": 
                Mes=int(input("Mes: "))
                Opcion="Dia"
            case "Dia":
                Dia=int(input("Dia: "))
                break
    except ValueError:
        print("Numero invalido.")


FechaDeNacimiento=date(Año, Mes, Dia)
Hoy=date.fromtimestamp(time.time())

DiasDesdeNac=Hoy-FechaDeNacimiento
DiasDesdeNac=str(DiasDesdeNac)

if len(DiasDesdeNac) == 7:
    DiasDesdeNac=0
else:
    try:
        DiasDesdeNac=int(DiasDesdeNac[:-14])
    except ValueError:
        DiasDesdeNac=int(DiasDesdeNac[:-13])

if DiasDesdeNac < 0:
    print("Introduciste una fecha en el futuro.")
elif DiasDesdeNac == 0:
    print("...Es hoy?")
else:
    if DiasDesdeNac == 1:
        Mensaje=f"pasó {DiasDesdeNac} dia."
    else:
        Mensaje=f"pasaron {DiasDesdeNac} días."
    print(f"Desde el {FechaDeNacimiento} hasta el dia de la fecha {Hoy}, {Mensaje}")
