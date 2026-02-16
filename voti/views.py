from django.shortcuts import render

# --- DATI CONDIVISI ---
materie = ["Matematica", "Italiano", "Inglese", "Storia", "Geografia"]

voti = {
    'Giuseppe Gullo': [("Matematica", 9, 0), ("Italiano", 7, 3), ("Inglese", 7, 4), ("Storia", 7, 4), ("Geografia", 5, 7)],
    'Antonio Barbera': [("Matematica", 8, 1), ("Italiano", 6, 1), ("Inglese", 9, 0), ("Storia", 8, 2), ("Geografia", 8, 1)],
    'Nicola Spina': [("Matematica", 7, 2), ("Italiano", 6, 2), ("Inglese", 4, 3), ("Storia", 8, 2), ("Geografia", 8, 2)]
}

def index(request):
    return render(request, "voti/index.html")

def view_a(request):
    context = {
        'elenco_materie': materie
    }
    return render(request, "voti/materie.html", context)

def view_b(request):
    context = {
        # Chiave rinominata in 'registro' per corrispondere al template HTML
        'registro': voti 
    }
    return render(request, "voti/materieVoti.html", context)

def view_c(request):
    medie_studenti = {}
    
    for studente, lista_voti in voti.items():
        somma_voti = sum([item[1] for item in lista_voti])
        numero_materie = len(lista_voti)
        media = round(somma_voti / numero_materie, 2)
        medie_studenti[studente] = media

    context = {
        'medie': medie_studenti
    }
    return render(request, "voti/Mediavoti.html", context)

def view_d(request):
    # 1. Troviamo i valori numerici min e max assoluti
    tutti_i_voti = []
    for lista in voti.values():
        for item in lista:
            tutti_i_voti.append(item[1]) # item[1] è il voto
            
    val_max = max(tutti_i_voti)
    val_min = min(tutti_i_voti)

    # 2. Troviamo CHI ha preso quei voti e in QUALI materie
    # Usiamo set() per evitare duplicati, poi convertiamo in list()
    studenti_max = set()
    materie_max = set()
    studenti_min = set()
    materie_min = set()

    for studente, lista_voti in voti.items():
        for materia, voto, assenze in lista_voti:
            if voto == val_max:
                studenti_max.add(studente)
                materie_max.add(materia)
            if voto == val_min:
                studenti_min.add(studente)
                materie_min.add(materia)

    context = {
        'v_max': val_max,
        'stud_max': list(studenti_max),
        'mat_max': list(materie_max),
        'v_min': val_min,
        'stud_min': list(studenti_min),
        'mat_min': list(materie_min),
    }
    return render(request, "voti/MaxMin.html", context)