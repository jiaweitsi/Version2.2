import matplotlib.pyplot as plot

class Airport:
    def __init__(self, code, lat, lon):
        self.code = code
        self.lat = lat
        self.lon = lon
        self.schengen = False


def IsSchengenAirport(code):
    if code == "":
        return False

    schengen_codes = ['LO', 'EB', 'LK', 'LC', 'EK', 'EE', 'EF', 'LF', 'ED', 'LG', 'EH', 'LH',
                'BI', 'LI', 'EV', 'EY', 'EL', 'LM', 'EN', 'EP', 'LP', 'LZ', 'LJ', 'LE', 'ES', 'LS']

    inicio = code[0:2]
    i=0
    found=False
    while i < len(schengen_codes) and not found:
        if schengen_codes[i] == inicio:
            found=True
        else:
            i=i+1
    if found:
        return True
    else:
        return False


def SetSchengen(airport):
    if IsSchengenAirport(airport.code):
        airport.schengen = True
    else:
        airport.schengen = False

def PrintAirport(airport):
    print('ICAO:', airport.code)
    print('Latitude:', airport.lat)
    print('Longitude:', airport.lon)
    print('Schengen:', airport.schengen)

def LoadAirports(filename):
    lista_airports = []
    try:
        f = open(filename, "r")
        lineas = f.readlines()
        f.close()

        for l in lineas[1:]:
            partes = l.split()
            if len(partes) >= 3:
                codigo = partes[0]
                lat_decimal = ConvertirCordinadas(partes[1])
                lon_decimal = ConvertirCordinadas(partes[2])

                nuevo_ap = Airport(codigo, lat_decimal, lon_decimal)
                lista_airports.append(nuevo_ap)

    except FileNotFoundError:
        return []

    return lista_airports

def ConvertirCordinadas(cord_str):
    sentido = cord_str[0]

    grados = float(cord_str[1:3])
    minutos = float(cord_str[3:5])
    segundos = float(cord_str[5:7])

    decimal = grados + (minutos / 60.0) + (segundos / 3600.0)

    if sentido == 'S' or sentido == 'W':
        decimal = decimal * -1

    return decimal

def SaveSchengenAirports(airports, filename):
    if len(airports) == 0:
        return "Error:Lista vacia"

    f = open(filename, "w")
    f.write("CODE LAT LON\n")

    i = 0
    n = len(airports)
    while i < n:
        a = airports[i]
        SetSchengen(a)
        if a.schengen == True:
            f.write(a.code)
            f.write(" ")
            f.write(str(a.lat))
            f.write(" ")
            f.write(str(a.lon))
            f.write("\n")
        i = i + 1
    f.close()

def AddAirport(airports, airport):
    i = 0
    encontrado = False
    n = len(airports)

    while i < n and encontrado == False:
        if airports[i].code == airport.code:
            encontrado = True
        else:
            i = i + 1
    if encontrado == False:
        airports.append(airport)
    else:
        print("El aeropuerto ya existe en la lista")


def RemoveAirport(airports, code):
    encontrado = False
    i = 0
    n = len(airports)
    pos = -1
    while i < n and encontrado == False:
        if airports[i].code == code:
            encontrado = True
            pos = i
        else:
            i = i + 1
    if encontrado:
        while pos < n - 1:
            airports[pos] = airports[pos + 1]
            pos = pos + 1
        del airports[n - 1]


def PlotAirports(airports):
    si = 0
    no = 0
    for a in airports:
        SetSchengen(a)
        if a.schengen:
            si = si+1
        else:
            no = no + 1

    plot.bar(['Airports'], [si], label='Schengen', color='blue')
    plot.bar(['Airports'], [no], bottom=[si], label='No Schengen', color='red')
    plot.title("Schengen vs No Schengen")
    plot.legend()
    plot.show()



