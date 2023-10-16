
file_path = 'input.txt'  # Sti til filen

# Liste for å lagre verdier
knutepunkt = []

start_print = False

# Åpne filen for lesing
with open(file_path, 'r') as file:
    # Iterer gjennom hver linje i filen
    for line in file:
            #Sjekker
            if 'Knutepunkt:' in line:
                start_print = True
                continue

            if start_print:
                    
                if not line.strip():
                    break

                # Fjern eventuelle ekstra mellomrom og linjeskift
                value = line.strip().split(',')
                    
                #Konvertere verdier til desimaltall 
                float_values = [float(values) for values in value]

                # Legg verdien til i listen
                knutepunkt.append(float_values)

# Skriv ut resultatet
for row in knutepunkt: 
    print(row)


