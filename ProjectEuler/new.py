def door_open(status):
    kontroll_liste = list(status)
    print(kontroll_liste)
    resultat_liste = []
    print(resultat_liste)

    if kontroll_liste[8] != 'P' or kontroll_liste[3]==0: # sjekker at gir er P eller sjekker om hovedbryter er på
        return resultat_liste  # hvis ikke P  eller hovedbryter av returnerer den tomme listen
    else:
        if kontroll_liste[2]== 0 : # hvis barnesikringen er av
            if kontroll_liste[0]==1 or kontroll_liste[4] == 1 or kontroll_liste[5] == 1 : # Hvis bryter eller at håndtakene for venstre dør er i bruk.
                resultat_liste.append("left")
                print(resultat_liste[:])
            elif kontroll_liste[1]==1 or kontroll_liste[6] == 1 or kontroll_liste[7] ==1 :  # Hvis bryter eller at håndtakene for høyre dør er i bruk.
                resultat_liste.append("rigth")
        elif kontroll_liste[0]==1 or kontroll_liste[5]==1: # barnesikring på, sjekker venstre håndtak ute og bryter
            resultat_liste.append("left")
            print(resultat_liste)
        elif kontroll_liste[1]==1 or kontroll_liste[7] ==1: # barnesikring på, sjekker høyre håndtak ute og bryter
            resultat_liste.append("rigth")
        elif kontroll_liste[0]==0 and kontroll_liste[1] == 0 and kontroll_liste[6]== 0 and kontroll_liste[7]==0 : # sjekker at ingen bryter og håndtak brukes
            resultat_liste = []

    return resultat_liste


print(door_open('00010100P'))
