
def input(file_path): 
    # Lists to store values
    knutepunkt = []
    fordelte_laster = []
    punktlaster = []

    # Default to False for whether to print
    print_knutepunkt = False
    print_fordelte_laster = False
    print_punktlast = False

    # Keywords to look for in the file
    info = ['Knutepunkt', 'Fordelte laster', 'Punktlaster']

    # Open the file for reading
    with open(file_path, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Change print flags based on keywords
            if info[0] in line:
                print_knutepunkt = True
                continue
            elif info[1] in line:
                print_fordelte_laster = True
                continue
            elif info[2] in line:
                print_punktlast = True
                continue

            # If inside a section, append the values to the respective list
            if print_knutepunkt:
                if not line.strip():
                    print_knutepunkt = False
                else:
                    knutepunkt.append(line.strip().split(', '))

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
            
    #Returnerer listene med de ulike verdiene
    return knutepunkt, fordelte_laster, punktlaster

knutepunkt, fordelte_laster, punktlaster = input('input.txt')



    