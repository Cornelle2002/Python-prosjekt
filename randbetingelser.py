def bc(npunkt, punkt, K, R):
    for p in range(npunkt):
        if punkt[p][2] == 1:  # Fritt opplagt
            for i in range(2):
                K[p * 3 + i][p * 3 + i] += 1e8
                R[p * 3 + i] = 0
        elif punkt[p][2] == 2:  # Fast innspent
            for i in range(3):
                K[p * 3 + i][p * 3 + i] += 1e8
                R[p * 3 + i] = 0

    return K, R