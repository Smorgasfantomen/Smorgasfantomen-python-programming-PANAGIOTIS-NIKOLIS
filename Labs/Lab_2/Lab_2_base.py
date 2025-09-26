import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Datafiler:
datapath = r"D:\Backup\Dokument\Utbildning\IT-Högskolan\Programmering Python\Panagiotis Github\Smorgasfantomen-python-programming-PANAGIOTIS-NIKOLIS\Labs\Lab_2\datapoints.txt"
testpath = r"D:\Backup\Dokument\Utbildning\IT-Högskolan\Programmering Python\Panagiotis Github\Smorgasfantomen-python-programming-PANAGIOTIS-NIKOLIS\Labs\Lab_2\testpoints.txt"

# Räkna ut avstånd mellan två punkter:
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

# Läs in testpoints.txt till testpointslist
with open(testpath, 'r') as file:
    next(file) # Skippa första raden
    for line in file:
        # Plocka värdena inom parentesen
        paren = line.strip().split('(')[-1].split(')')[0]
        width, height = paren.split(',')
        testpointslist.append([float(width), float(height)])

# Gör arrayer av listorna
datarr = np.array(datapointslist)
testarr = np.array(testpointslist)

# Splitta datarr i två arrays baserat på species
pichuarr = datarr[datarr[:, 2] == 0]
pikachuarr = datarr[datarr[:, 2] == 1]

# Loopa varje testpunkt och hitta "nearest neighbor" i träningsdata
for testpoint in testarr:
    min_dist = float("inf")    # Minsta avstånd börjar på infinite
    nearneighbor = None        # Tom variabel för närmaste granne
    for datapoint in datarr:   # Jämför med träningspunkterna
        distance = eucdist(testpoint, datapoint[:2])
        if distance < min_dist:  # Uppdatera när ett mindre avstånd hittas
            min_dist = distance
            nearneighbor = datapoint
    # Lägg punkten i rätt lista efter species
    if nearneighbor[2] == 0:
        newpichulist.append((testpoint[0], testpoint[1], 0))
    elif nearneighbor[2] == 1:
        newpikachulist.append((testpoint[0], testpoint[1], 1))

# Gör arrays av listorna
newpichu = np.array(newpichulist)
newpikachu = np.array(newpikachulist)

# Skapa scatterplotsen
plt.scatter(pichuarr[:, 0], pichuarr[:, 1], color='yellow', label='Pichu', edgecolors='lightgrey')
plt.scatter(pikachuarr[:, 0], pikachuarr[:, 1], color='orange', label='Pikachu', edgecolors='lightgrey')
plt.scatter(newpichu[:, 0], newpichu[:, 1], color='yellow', label='Probably Pichu', edgecolors='black')
plt.scatter(newpikachu[:, 0], newpikachu[:, 1], color='orange', label='Probably Pikachu', edgecolors='black')

# Gör att varje axel får "cm"
plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{x:.0f} cm"))
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: f"{y:.0f} cm"))

plt.xlabel("Thiccness")
plt.ylabel("Height")
plt.title("Pokemice")
plt.legend()
plt.show()