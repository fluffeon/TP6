def redondearDeVerdad(numero): # Redondeo de verdad
    truncar=int(numero)

    if numero - truncar >= 0.5:
        return truncar+1
    
    return truncar