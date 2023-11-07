def randbetingelser(npunkt, punkt, K):

    for i in range(npunkt):                             # Itererer gjennom knutepunktene
        if punkt[i][2] == 0:                            # Finner punktene som er er fritt opplagt
            pass
        elif punkt[i][2] == 1:                          # Finner punktene som er er fast innspent
            for x in range(((i) * 3), ((i) * 3) + 3):
                K[x][x] = K[x][x]*10**6                 # Putter på fjær stivhet på 10^6
        else:
            print('Error: Fant ikke innspenning')       # Printer ut Error hvis om det er feil frihetsgrad
    
    return K # Returnerer modifisert global stivhetsvektor