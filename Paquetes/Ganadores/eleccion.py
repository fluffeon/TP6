def imprimirGanador(Ganador):
    if type(Ganador) == list:
        print("¡Los ganadores son ",end="")
        for d in range(len(Ganador)):
            print(Ganador[d],end="")
            if len(Ganador) - 2 == d:
                print(" y ",end="")
            elif len(Ganador) - 1 == d:
                print("!")
            else:
                print(", ",end="")
    else:
        print(f"¡Ganador es {Ganador}!")