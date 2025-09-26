import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import matplotlib.ticker as ticker

# Datafil:
datapath = r"D:\Backup\Dokument\Utbildning\IT-Högskolan\Programmering Python\Panagiotis Github\Smorgasfantomen-python-programming-PANAGIOTIS-NIKOLIS\Labs\Lab_2\datapoints.txt"

# Funktion för att räkna ut avstånd mellan två punkter:
def eucdist(p0, p1):
    return np.sqrt((p0[0]-p1[0])**2 + (p0[1]-p1[1])**2)

# Skapa tomma Listor:
datapointslist = []
testpointslist = []
newpichulist = []
newpikachulist = []

# Läs in datapoints.txt till datapointslist
with open(datapath, 'r') as file:
    next(file) # Skippa första raden
    # Loopa varje rad
    for line in file:
        # Splitta raden i tre delar: bredd, höjd och species
        width, height, species = line.strip().split(",")
        # Konvertera mått till floats, art till int och spara som en tuple i datapointslist
        datapointslist.append((float(width), float(height), int(species)))

# Ta in testdata från användaren
inputmore = "y"
while inputmore == "y":
    # Main inmatningsloop
    while inputmore == "y":
        # Tjockleksinmatningsloop
        try:
            print("Skriv in hur bred din pokemon är:")
            inputwidth = float(input().replace(",", ".")) # Gör om komma till punkt pga EU-tangentbord
            if inputwidth < 0:
                raise ValueError("Användaren har inte matat in ett positivt tal.")
            break
        except ValueError:
            print("Du måste mata in ett positivt tal.")

    while inputmore == "y":
        # Längdinmatningsloop
        try:
            print("Skriv in hur lååång din pokemon är:")
            inputheight = float(input().replace(",", ".")) # Gör om komma till punkt pga EU-tangentbord
            if inputheight < 0:
                raise ValueError("Användaren har inte matat in ett positivt tal.")
            break
        except ValueError:
            print("Du måste mata in ett positivt tal.")
        
    testpointslist.append([float(inputwidth), float(inputheight)])
    
    print("Vill du mata in fler pokemons? y/n")
    inputmore = input()
    if inputmore == "y":
        continue
    elif inputmore == "n":
        break
    else:
        print("Var god upprepa dig: y/n")
        inputmore = input()

    

# Gör arrayer av listorna
datarr = np.array(datapointslist)
testarr = np.array(testpointslist)

# Splitta datarr i två arrays baserat på species
pichuarr = datarr[datarr[:, 2] == 0]
pikachuarr = datarr[datarr[:, 2] == 1]

# Loopa varje testpunkt och hitta "nearest neighbor" i träningsdata
for testpoint in testarr:
    min_dist = float("inf")
    # Minsta avstånd börjar på infinite
    nearneighbor = None
    # Tom variabel för närmaste granne
    for datapoint in datarr:   # Jämför med träningspunkterna
        # Räkna ut distansen mellan testpunkten och datapunkten (minus species-värdet)
        distance = eucdist(testpoint, datapoint[:2])
        if distance < min_dist:  # Uppdatera när ett mindre avstånd hittas
            min_dist = distance
            nearneighbor = datapoint
    # Lägg punkten i rätt lista efter species baserat på vilken som var närmast
    if nearneighbor[2] == 0:
        newpichulist.append((testpoint[0], testpoint[1], 0))
    elif nearneighbor[2] == 1:
        newpikachulist.append((testpoint[0], testpoint[1], 1))

# Gör arrays av listorna
newpichu = np.array(newpichulist)
newpikachu = np.array(newpikachulist)

# Skapar scatterplotsen
plt.scatter(pichuarr[:, 0], pichuarr[:, 1], color='yellow', label='Pichu', edgecolors='lightgrey')
plt.scatter(pikachuarr[:, 0], pikachuarr[:, 1], color='orange', label='Pikachu', edgecolors='lightgrey')
# Få skiten att inte krascha ifall arrayen är tom
if newpichu.size > 0:
    plt.scatter(newpichu[:, 0], newpichu[:, 1], color='yellow', label='Probably a Pichu', edgecolors='black')
if newpikachu.size > 0:
    plt.scatter(newpikachu[:, 0], newpikachu[:, 1], color='orange', label='Probably a Pikachu', edgecolors='black')

# Gör att varje axel får "cm"
plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{x:.0f} cm"))
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: f"{y:.0f} cm"))

plt.xlabel("Thiccness")
plt.ylabel("Height")
plt.title("Pokemice")
plt.legend()
plt.show()