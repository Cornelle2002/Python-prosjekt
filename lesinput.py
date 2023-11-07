import numpy as np

#Funksjon for å lagre verdiene fra tekstfilen til lister
def input(file_path):

    # Listene for å lagre verdiene
    knutepunkt = []       # Lagrer knutepunkt-verdier
    fordelte_laster = []  # Lagrer fordelte laster
    punktlaster = []      # Lagrer punktlaster
    elementer = []        # Lagrer elementer
    geometri = []         # Lagrer geometri

    # Setter standardverdi til False for om funksjonen skal skrive ut
    print_knutepunkt = False
    print_elementer = False
    print_fordelte_laster = False
    print_punktlast = False
    print_geometri = False

    # Nøkkelord funksjonen skal lete etter i tekstfilen
    nokkelord = ['Knutepunkt', 'Elementer', 'Fordelte laster', 'Punktlaster', 'Geometri']

    # Åpner tekstfilen for lesing
    with open(file_path, 'r') as file:

        # Itererer gjennom hver linje i tekstfilen 
        for line in file:

            # Endrer verdiene til True hvis nøkkelord blir funnet
            if nokkelord[0] in line:
                print_knutepunkt = True 
                continue
            elif nokkelord[1] in line:
                print_elementer = True
                continue
            elif nokkelord[2] in line:
                print_fordelte_laster = True
                continue
            elif nokkelord[3] in line:
                print_punktlast = True
                continue   
            elif nokkelord[4] in line:
                print_geometri = True
                continue           

            # Hvis nøkkelord er funnet, legg til verdiene i respektive liste
            if print_knutepunkt:
                if not line.strip():                            # Stopper når en tom linje i tekstfilen blir nådd
                    print_knutepunkt = False
                else:
                    knutepunkt.append(line.strip().split(', ')) # Fjerner eventuelle ekstra mellomrom, linjeskift, og 
                                                                # legger til verdiene som egne elementer i respektiv liste
            if print_elementer:
                if not line.strip():
                    print_elementer = False
                else:
                    elementer.append(line.strip().split(', '))

            if print_fordelte_laster:
                if not line.strip():
                    print_fordelte_laster = False
                else:
                    fordelte_laster.append(line.strip().split(', '))

            if print_punktlast:
                if not line.strip():
                    print_punktlast = False
                else:
                    punktlaster.append(line.strip().split(', '))
            
            if print_geometri:
                if not line.strip():
                    print_geometri = False
                else:
                    geometri.append(line.strip().split(', '))
        
        #Finner lengden/antall av alle verdiene
        Nknutepunkt = len(knutepunkt)   
        Nelemeter = len(elementer)
        Nfordelt = len(fordelte_laster)
        Npunktlaster = len(punktlaster)

    # Returnerer listene med de ulike verdiene
    return knutepunkt, elementer, fordelte_laster, punktlaster, geometri, Nknutepunkt, Nelemeter, Nfordelt, Npunktlaster


#Funksjon for å verdier i lister til enten float eller char
def float_char(liste):
    # Definerer en liste med karakterer som representerer heltall
    int_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    # Går gjennom hver rad i listen
    for j, rows in enumerate(liste):
        for elem, i in enumerate(rows): # Går gjennom hver element i hver rad
            li = list(i)                # Konverterer elementet til en liste av tegn
            
            # Sjekker om det første tegnet i elementet er en representasjon av et heltall
            if li[0] in int_list:
                liste[j][elem] = float(i) # Konverterer elementet til flyttall og oppdaterer det i listen
    
    # Returnerer den oppdaterte listen med flyttall
    return liste
