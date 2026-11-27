atomic_masses = {
    'H': 1.008,
    'He': 4.003,
    'Li': 6.94,
    'Be': 9.012,
    'B': 10.81,
    'C': 12.011,
    'N': 14.007,
    'O': 15.999,
    'F': 18.998,
    'Ne': 20.180,
    'Na': 22.990,
    'Mg': 24.305,
    'Al': 26.982,
    'Si': 28.085,
    'P': 30.974,
    'S': 32.06,
    'Cl': 35.45,
    'Ar': 39.948,
    'K': 39.098,
    'Ca': 40.078,
    'Sc': 44.956,
    'Ti': 47.867,
    'V': 50.942,
    'Cr': 51.996,
    'Mn': 54.938,
    'Fe': 55.845,
    'Co': 58.933,
    'Ni': 58.693,
    'Cu': 63.546,
    'Zn': 65.38,
    'Ga': 69.723,
    'Ge': 72.630,
    'As': 74.922,
    'Se': 78.971,
    'Br': 79.904,
    'Kr': 83.798,
    'Rb': 85.468,
    'Sr': 87.62,
    'Y': 88.906,
    'Zr': 91.224,
    'Nb': 92.906,
    'Mo': 95.95,
    'Tc': 98.0,
    'Ru': 101.07,
    'Rh': 102.906,
    'Pd': 106.42,
    'Ag': 107.868,
    'Cd': 112.414,
    'In': 114.818,
    'Sn': 118.710,
    'Sb': 121.760,
    'Te': 127.60,
    'I': 126.904,
    'Xe': 131.293,
    'Cs': 132.905,
    'Ba': 137.327,
    'La': 138.905,
    'Ce': 140.116,
    'Pr': 140.908,
    'Nd': 144.242,
    'Pm': 145.0,
    'Sm': 150.36,
    'Eu': 151.964,
    'Gd': 157.25,
    'Tb': 158.925,
    'Dy': 162.500,
    'Ho': 164.930,
    'Er': 167.259,
    'Tm': 168.934,
    'Yb': 173.045,
    'Lu': 174.967,
    'Hf': 178.49,
    'Ta': 180.948,
    'W': 183.84,
    'Re': 186.207,
    'Os': 190.23,
    'Ir': 192.217,
    'Pt': 195.084,
    'Au': 196.967,
    'Hg': 200.592,
    'Tl': 204.38,
    'Pb': 207.2,
    'Bi': 208.980,
    'Po': 209.0,
    'At': 210.0,
    'Rn': 222.0,
    'Fr': 223.0,
    'Ra': 226.0,
    'Ac': 227.0,
    'Th': 232.038,
    'Pa': 231.036,
    'U': 238.029,
    'Np': 237.0,
    'Pu': 244.0,
    'Am': 243.0,
    'Cm': 247.0,
    'Bk': 247.0,
    'Cf': 251.0,
    'Es': 252.0,
    'Fm': 257.0,
    'Md': 258.0,
    'No': 259.0,
    'Lr': 266.0,
    'Rf': 267.0,
    'Db': 268.0,
    'Sg': 269.0,
    'Bh': 270.0,
    'Hs': 277.0,
    'Mt': 278.0,
    'Ds': 281.0,
    'Rg': 282.0,
    'Cn': 285.0,
    'Nh': 286.0,
    'Fl': 289.0,
    'Mc': 290.0,
    'Lv': 293.0,
    'Ts': 294.0,
    'Og': 294.0
}


def calculate_molar_mass(mass, moles):
    if moles > 0 and mass > 0:
        return mass / moles
    else:
        print('Mole i/lub masa muszą być większe od 0')
        return None


def calculate_moles(mass, molar_mass):
    if molar_mass > 0 and mass > 0:
        return mass / molar_mass
    else:
        print('Masa molowa i masa musi być większa od 0')
        return None


def calculate_mass(molar_mass, moles):
    if molar_mass > 0 and moles > 0:
        return molar_mass * moles
    else:
        print('Masa i mole muszą być większe od 0')
        return None

def calculate_formula_mass(formula):
    element1 = formula[0]

    if formula[1].isdigit():
        count1 = int(formula[1])
        element2 = formula[2]
        count2 = 1
    else:
        count1 = 1
        element2 = formula[1]
        count2 = 1

    molar_mass = (
        atomic_masses[element1] * count1
        + atomic_masses[element2] * count2
    )

    return molar_mass


def option_molar_mass():
    compound = input('Podaj nazwę związku: ').strip()

    try:
        mass = float(input('Podaj masę w gramach: '))
        moles = float(input('Podaj liczbę moli: '))
    except ValueError:
        print('Podaj poprawne liczby!')
        return

    molar_mass = calculate_molar_mass(mass, moles)

    if molar_mass is not None:
        print(f'Masa molowa {compound} wynosi {round(molar_mass, 2)} g/mol')
    else:
        print('Błąd')


def option_moles():
    compound = input('Podaj nazwę związku: ').strip()

    try:
        mass = float(input('Podaj masę w gramach: '))
        molar_mass = float(input('Podaj masę molową w g/mol: '))
    except ValueError:
        print('Podaj poprawne liczby!')
        return

    moles = calculate_moles(mass, molar_mass)

    if moles is not None:
        print(f'Liczba moli {compound} wynosi {round(moles, 2)} mol')
    else:
        print('Błąd')


def option_mass():
    compound = input('Podaj nazwę związku: ').strip()

    try:
        molar_mass = float(input('Podaj masę molową w g/mol: '))
        moles = float(input('Podaj liczbę moli: '))
    except ValueError:
        print('Podaj poprawne liczby!')
        return

    mass = calculate_mass(molar_mass, moles)

    if mass is not None:
        print(f'Masa {compound} wynosi {round(mass, 2)} g')
    else:
        print('Błąd')


def show_menu():
    print('CHEMICAL CALCULATOR')
    print('1 - Oblicz masę molową')
    print('2 - Oblicz liczbę moli')
    print('3 - Oblicz masę')
    print('4 - Zakończ program')


while True:
    show_menu()
    choice = input('Wybierz opcję: ').strip().lower()

    if choice == '1':
        option_molar_mass()

    elif choice == '2':
        option_moles()

    elif choice == '3':
        option_mass()

    elif choice == '4' or choice == 'q':
        break

    else:
        print('Nieprawidłowa opcja')
