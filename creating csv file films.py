import csv

films = [["Top Gun", "Risky Business", "Minority Report"],["Titanic","The Revenant","Inception"],["Training Day", "Man on Fire", "Flight"]]
with open("films.csv", "w") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",")
    for film_list in films:
        spamwriter.writerow(film_list)
