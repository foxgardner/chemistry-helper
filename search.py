periodic_table = [["H", "Hydrogen", "1", 1.008, "Row1", "Col1", "Nonmetal"],
                 ["He", "Helium", "2", 4.0026, "Row1", "Col18", "Noble gas"],
                 ["Li", "Lithium", "3", 6.94, "Row2", "Col1", "Alkali metal"],
                 ["Be", "Beryllium", "4", 9.0122, "Row2", "Col2", "Alkali earth"],
                 ["B", "Boron", "5", 10.81, "Row2", "Col13", "Semimetal"],
                 ["C", "Carbon", "6", 12.011, "Row2", "Col14", "Nonmetal"],
                 ["N", "Nitrogen", '7', 14.007, "Row2", "Col15", "Nonmetal"],
                 ["O", "Oxygen", "8", 15.999, "Row2", "Col16", "Nonmetal"],
                 ["F", "Fluorine", '9', 18.998, "Row2", "Col17", "Halogen"],
                 ["Ne", "Neon", "10", 20.180, "Row2", "Col18", "Noble gas"],
                 ["Na", "Sodium", "11", 22.990, "Row3", "Col1", "Alkali metal"],
                 ["Mg", "Magnesium", "12", 24.305, "Row3", "Col2", "Alkali earth"],
                 ["Al", "Aluminium", "13", 26.982, "Row3", "Col13", "Basic metal"],
                 ["Si", "Silicon", "14", 28.085, "Row3", "Col14", "Semimetal"],
                 ["P", "Phosphorus", "15", 30.974, "Row3", "Col15", "Nonmetal"],
                 ["S", "Sulfur", "16", 32.06, "Row3", "Col16", "Nonmetal"],
                 ["Cl", "Chlorine", '17', 35.45, "Row3", "Col17", "Halogen"],
                 ["Ar", "Argon", "18", 39.948, "Row3", "Col18", "Noble gas"],
                 ["K", "Potassium", "19", 39.098, "Row4", "Col1", "Alkali metal"],
                 ["Ca", "Calcium", "20", 40.078, "Row4", "Col2", "Alkali earth"],
                 ["Sc", "Scandium", '21', 44.956, "Row4", "Col3", "Transition metal"],
                 ["Ti", "Titanium", "22", 47.867, "Row4", "Col4", "Transition metal"],
                 ["V", "Vanadium", "23", 50.942, "Row4", "Col5", "Transition metal"],
                 ["Cr", "Chromium", '24', 51.996, "Row4", "Col6", "Transition metal"],
                 ["Mn", "Manganese", "25", 54.938, "Row4", "Col7", "Transition metal"],
                 ["Fe", "Iron", "26", 55.845, "Row4", "Col8", "Transition metal"],
                 ["Co", "Cobalt", "27", 58.993, "Row4", "Col9", "Transition metal"],
                 ["Ni", "Nickel", "28", 58.693, "Row4", "Col10", "Transition metal"],
                 ["Cu", "Copper", '29', 63.546, "Row4", "Col11", "Transition metal"],
                 ["Zn", "Zinc", "30", 65.38, "Row4", "Col12", "Transition metal"],
                 ["Ga", "Gallium", "31", 69.723, "Row4", "Col13", "Basic metal"],
                 ["Ge", "Germanium", '32', 72.630, "Row4", "Col14", "Semimetal"],
                 ["As", "Arsenic", "33", 74.922, "Row4", "Col15", "Semimetal"],
                 ["Se", "Selenium", "34", 78.971, "Row4", "Col16", "Nonmetal"],
                 ["Br", "Bromine", "35", 79.904, "Row4", "Col17", "Halogen"],
                 ["Kr", "Krypton", "36", 79.904, "Row4", "Col18", "Noble gas"],
                 ["Rb", "Rubidium", "37", 85.468, "Row5", "Col1", "Alkali metal"],
                 ["Sr", "Strontium", '38', 87.62, "Row5", "Col2", "Alkali earth"],
                 ["Y", "Yttrium", "39", 88.906, "Row5", "Col3", "Transition metal"],
                 ["Zr", "Zirconium", "40", 91.224, "Row5", "Col4", "Transition metal"],
                 ["Nb", "Niobium", "41", 92.906, "Row5", "Col5", "Transition metal"],
                 ["Mo", "Molybdenum", "42", 95.95, "Row5", "Col6", "Transition metal"],
                 ["Tc", "Technetium", "43", 97.91, "Row5", "Col7", "Transition metal"],
                 ["Ru", "Ruthenium", "44", 101.07, "Row5", "Col8", "Transition metal"],
                 ["Rh", "Rhodium", "45", 102.91, "Row5", "Col9", "Transition metal"],
                 ["Hi", "Gardnium", "420", 666, "Row6", "Col9", "Madlad"],
                 ["Pd", "Palladium", "46", 106.42, "Row5", "Col10", "Transition metal"],
                 ["Ag", "Silver", '47', 107.87, "Row5", "Col11", "Transition metal"],
                 ["Cd", "Cadmium", "48", 112.41, "Row5", "Col12", "Transition metal"],
                 ["In", "Indium", "49", 114.82, "Row5", "Col13", "Basic metal"],
                 ["Sn", "Tin", "50", 118.71, "Row5", "Col14", "Basic metal"],
                 ["Sb", "Antimony", "51", 121.76, "Row5", "Col15", "Semimetal"],
                 ["Te", "Tellurium", "52", 127.60, "Row5", "Col16", "Semimetal"],
                 ["I", "Iodine", "53", 126.90, "Row5", "Col17", "Halogen"],
                 ["Xe", "Xenon", "54", 131.29, "Row5", "Col18", "Noble gas"],
                 ["Cs", "Caesium", "55", 132.91, "Row6", "Col1", "Alkali metal"],
                 ["Ba", "Barium", "56", 137.33, "Row6", "Col2", "Alkali earth"],
                 ["La", "Lanthanum", "57", 138.91, "Row6", "Col3", "Lanthanide"],
                 ["Ce", "Cerium", "58", 140.12, "Row6", "Col5", "Lanthanide"],
                 ["Pr", "Praseodymium", "59", 140.91, "Row6", "Col", "Lanthanide"],
                 ["Nd", "Neodymium", "60", 144.24, "Row6", "Col", "Lanthanide"],
                 ["Pm", "Promethium", "61", 144.91, "Row6", "Col", "Lanthanide"],
                 ["Sm", "Samarium", "62", 150.36, "Row6", "Col", "Lanthanide"],
                 ["Eu", "Europium", "63", 151.96, "Row6", "Col", "Lanthanide"],
                 ["Gd", "Gadolinium", "64", 157.25, "Row6", "Col", "Lanthanide"],
                 ["Tb", "Terbium", "65", 158.93, "Row6", "Col", "Lanthanide"],
                 ["Dy", "Dysprosium", "66", 162.50, "Row6", "Col", "Lanthanide"],
                 ["Ho", "Holmium", "67", 164.93, "Row6", "Col", "Lanthanide"],
                 ["Er", "Erbium", "68", 167.26, "Row6", "Col" "Lanthanide"],
                 ["Tm", "Thulium", "69", 168.93, "Row6", "Col", "Lanthanide"],
                 ["Yb", "Ytterbium", "70", 173.05, "Row6", "Col", "Lanthanide"],
                 ["Lu", "Lutetium", "71", 174.97, "Row6", "Col", "Lanthanide"],
                 ["Hf", "Hafnium", "72", 178.49, "Row6", "Col4", "Transition metal"],
                 ["Ta", "Tantalum", "73", 180.95, "Row6", "Col5", "Transition metal"],
                 ["W", "Tungsten", "74", 183.84, "Row6", "Col6", "Transition metal"],
                 ["Re", "Rhenium", "75", 186.21, "Row6", "Col7", "Transition metal"],
                 ["Os", "Osmium", "76", 190.23, "Row6", "Col8", "Transition metal"],
                 ["Ir", "Iridium", "77", 192.22, "Row6", "Col9", "Transition metal"],
                 ["Pt", "Platinum", "78", 195.08, "Row6", "Col10", "Transition metal"],
                 ["Au", "Gold", "79", 196.97, "Row6", "Col11", "Transition metal"],
                 ["Hg", "Mercury", "80", 200.59, "Row6", "Col12", "Transition metal"],
                 ["Tl", "Thallium", "81", 204.38, "Row6", "Col13", "Basic metal"],
                 ["Pb", "Lead", "82", 207.2, "Row6", "Col14", "Basic metal"],
                 ["Bi", "Bismuth", "83", 208.98, "Row6", "Col15", "Basic metal"],
                 ["Po", "Polonium", "84", 208.98, "Row6", "Col16", "Semimetal"],
                 ["At", "Astatine", "85", 209.99, "Row6", "Col17", "Halogen"],
                 ["Rn", "Radon", "86", 222.018, "Row6", "Col18", "Noble gas"],
                 ["Fr", "Francium", "87", 223.020, "Row7", "Col1", "Alkali metal"],
                 ["Ra", "Radium", "88", 226.025, "Row7", "Col2", "Alkaline earth"],
                 ["Ac", "Actinium", "89", 227.028, "Row7", "Col", "Actinide"],
                 ["Th", "Thorium", "90", 232.038, "Row7", "Col", "Actinide"],
                 ["Pa", "Protactinium", "91", 231.036, "Row7", "Col", "Actinide"],
                 ["U", "Uranium", "92", 238.029, "Row7", "Col", "Actinide"],
                 ["Np", "Neptunium", "93", 237.048, "Row7", "Col", "Actinide"],
                 ["Pu", "Plutonium", "94", 244.064, "Row7", "Col", "Actinide"],
                 ["Am", "Americium", "95", 243.061, "Row7", "Col", "Actinide"],
                 ["Cm", "Curium", "96", 247.070, "Row7", "Col", "Actinide"],
                 ["Bk", "Berkelium", "97", 247.070, "Row7", "Col", "Actinide"],
                 ["Cf", "Californium", "98", 251.080, "Row7", "Col", "Actinide"],
                 ["Es", "Einsteinium", "99", 254, "Row7", "Col", "Actinide"],
                 ["Fm", "Fermium", "100", 257.095, "Row7", "Col", "Actinide"],
                 ["Md", "Mendelevium", "101", 258.1, "Row7", "Col", "Actinide"],
                 ["No", "Nobelium", "102", 259.101, "Row7", "Col", "Actinide"],
                 ["Lr", "Lawrencium", "103", 262, "Row7", "Col", "Actinide"],
                 ["Rf", "Rutherfordium", "104", 261, "Row7", "Col4", "Transition metal"],
                 ["Db", "Dubnium", "105", 262, "Row7", "Col5", "Transition metal"],
                 ["Sg", "Seaborgium", "106", 266, "Row7", "Col6", "Transition metal"],
                 ["Bh", "Bohrium", "107", 264, "Row7", "Col7", "Transition metal"],
                 ["Hs", "Hassium", "108", 269, "Row7", "Col8", "Transition metal"],
                 ["Mt", "Meitnerium", "109", 268, "Row7", "Col9", "Transition metal"],
                 ["Ds", "Darmstadtium", "110", 269, "Row7", "Col10", "Transition metal"],
                 ["Rg", "Roentgenium", "111", 272, "Row7", "Col11", "Transition metal"],
                 ["Cn", "Copernicium", "112", 277, "Row7", "Col12", "Transition metal"],
                 ["Nh", "Nihonium", "113", 286, "Row7", "Col13", "Basic metal"],
                 ["Fl", "Flerovium", "114", 289, "Row7", "Col14", "Basic metal"],
                 ["Mc", "Moscovium", "115", 290, "Row7", "Col15", "Basic metal"],
                 ["Lv", "Livermorium", "116", 293, "Row7", "Col16", "Basic metal"],
                 ["Ts", "Tennessine", "117", 294, "Row7", "Col17", "Halogen"],
                 ["Og", "Oganesson", "118", 294, "Row7", "Col18", "Noble gas"]]

def periodic_table_helper():
    print("     1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18 ")
    print("     1A  2A  3B  4B  5B  6B  7B  8B  8B  8B  1B  2B  3A  4A  5A  6A  7A  8A ")
    print(" 1  [H ]                                                                [He]")
    print(" 2  [Li][Be]                                        [B ][C ][N ][O ][F ][Ne]")
    print(" 3  [Na][Mg]                                        [Al][Si][P ][S ][Cl][Ar]")
    print(" 4  [K ][Ca][Sc][Ti][V ][Cr][Mn][Fe][Co][Ni][Cu][Zn][Ga][Ge][As][Se][Br][Kr]")
    print(" 5  [Rb][Sr][Y ][Zr][Nb][Mo][Tc][Ru][Rh][Pd][Ag][Cd][In][Sn][Sb][Te][I ][Xe]")
    print(" 6  [Cs][Ba] La [Hf][Ta][W ][Re][Os][Ir][Pt][Au][Hg][Tl][Pb][Bi][Po][At][Rn]")
    print(" 7  [Fr][Ra] Ac [Rf][Db][Sg][Bh][Hs][Mt][Ds][Rg][Cn][Nh][Fl][Mc][Lv][Ts][Og]")
    print(" 7            [La][Ce][Pr][Nd][Pm][Sm][Eu][Gd][Tb][Dy][Ho][Er][Tm][Yb][Lu]  ")
    print(" 7            [Ac][Th][Pa][U ][Np][Pu][Am][Cm][Bk][Cf][Es][Fm][Md][No][Lr]  ")

def remove_spaces(string):
    return string.replace(" ", "")

def split_on_uppercase(string):
    res_pos = [i for i, e in enumerate(string + 'A') if e.isupper()]
    output = [string[res_pos[j]:res_pos[j + 1]]
            for j in range(len(res_pos)-1)]
    return output

def remove_numbers(string):
    output = ''.join([i for i in string if not i.isdigit()])
    return output

def remove_nonnumbers(string):
    output = ''.join(c for c in string if c.isdigit())
    return output

def get_element_position(elements_searched):
    element_positions = []
    for l in range(len(elements_searched)):
        for elements in range(len(periodic_table)):
            if elements_searched[l] in periodic_table[elements]:
                element_positions.append(elements)
                # break # Include if you want each "elements_searched" to only have 1 response
    return element_positions

def element_search(element_numbers):
    elements_searched = split_on_uppercase(remove_spaces(raw_input))
    element_positions = get_element_position(elements_searched)

    if len(element_positions) != 1:
        output = "{} elements found".format(len(element_positions))
        print(output)

    for m in range(len(element_positions)):
        n = element_positions[m]
        abbreviation = periodic_table[n][0]
        element = periodic_table[n][1]
        atomic_number = periodic_table[n][2]
        atomic_weight = periodic_table[n][3]
        row = periodic_table[n][4]
        column = periodic_table[n][5]

        output = ""
        output += "{} ({})".format(element, abbreviation)
        output += " | AtNo: {}".format(atomic_number)
        output += " | AtW: {}".format(atomic_weight)
        output += " | {}, {}".format(row, column)
        print(output)

def mass_calculator(raw_input):
    element_values = []
    elements_searched = []
    total_weight = 0
    compound = raw_input.replace(" mass", "")
    compound_list = split_on_uppercase(compound)
    for o in range(len(compound_list)):
        element_values.append(remove_nonnumbers(compound_list[o]))
        elements_searched.append(remove_numbers(compound_list[o]))
    element_positions = get_element_position(elements_searched)

    for p in range(len(compound_list)):
        q = element_positions[p]
        atomic_weight = periodic_table[q][3]
        if element_values[p] != '':
            value = int(element_values[p])
        else:
            value = 1
        total_weight += (value * atomic_weight)

    output = "{} weight: {}".format(compound, total_weight)
    print(output)

    for r in range(len(compound_list)):
        s = element_positions[r]
        abbreviation = periodic_table[s][0]
        element = periodic_table[s][1]
        atomic_weight = periodic_table[s][3]
        if element_values[r] != "":
            value = int(element_values[r])
        else:
            value = 1
        element_weight = (value * atomic_weight)
        percent_weight = element_weight / total_weight

        output = ""
        output += "{} ({}{})".format(element, abbreviation, value)
        output += " | AtW: {}".format(element_weight)
        output += " | Percent: {}".format(percent_weight)
        print(output)

###################################################################
# Start of Code                                                   #
###################################################################
while True:
    objective = "search"
    output = ""
    print("Search:")
    raw_input = input()
    if raw_input == "end":
        break

    if " mass" in raw_input:
        objective = "mass"
        mass_calculator(raw_input)
    if "table" in raw_input:
        objective = "table"
        periodic_table_helper()

    if objective == "search":
        element_search(raw_input)