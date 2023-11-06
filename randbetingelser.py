def randbetingelser(npunkt, punkt, K):
    for i in range(npunkt):
        if punkt[i][2] == 0: # Fri
            pass
        elif punkt[i][2] == 1: # Fast innspent
            for x in range(((i) * 3), ((i) * 3) + 3):
                K[x][x] = K[x][x]*10**6
        else:
            print('Error: Fant ikke innspenning')
    
    return K