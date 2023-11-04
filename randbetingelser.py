def bc(npunkt, punkt, K, R):
    for p in range(npunkt):
        if punkt[p][2] == 2:  # Fri
            pass
        elif punkt[p][2] == 0: # Fritt opplagt
            K[p * 3][p * 3] += 10 ** 6
            K[p * 3 + 1][p * 3 + 1] += 10 ** 6
            R[p * 3] = 0
            R[p * 3 + 1] = 0 
        elif punkt[p][2] == 1:  # Fast innspent
            K[p * 3][p * 3] += 10 ** 6
            K[p * 3 + 1][p * 3 + 1] += 10 ** 6
            K[p * 3 + 2][p * 3 + 2] += 10 ** 6
            R[p * 3] = 0
            R[p * 3 + 1] = 0
            R[p * 3 + 2] = 0
        else:
            print('Error: Fant ikke innspenning')

    return K, R