import csv
def neuer_eintrag(start, ziel):
    with open("csv.csv", "a") as et:
        eintrag_target = csv.writer(et)
        eintrag_target.writerow([start, ziel])
        return

neuer_eintrag('3', '2')

def gesamtemission():
    with open("csv.csv", "r") as CO2F:
        CO2F = csv.reader(CO2F)
        summe = 0
        for line in CO2F:
            for i in range(len(line)):
                summe = summe + int(line[i])
        return (summe)

print(gesamtemission())

