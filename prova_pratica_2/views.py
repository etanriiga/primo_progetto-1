from django.shortcuts import render
import random

def index(request):
    return render(request, "prova_pratica_2/index.html")
def media(request):
    centrale=0
    massimo=0
    minimo=0

    lista=[3]
    for _ in range(1,3):
        lista.append(random.randint(1,50))
    

    somma= sum(lista)
    media=somma/3
    massimo= max(lista)
    minimo=min(lista)
    lista.remove(massimo)
    lista.remove(minimo)
    centrale=lista[0]
    lista.append(massimo)
    lista.append(minimo)
    
    
    
    context={
            'lista' : [lista],
            'media' : media,
            'massimo' : massimo,
            'minimo' : minimo,
            'centrale' : centrale
            }

    return render(request, "prova_pratica_2/media.html", context)


def stringhe(request):
    lista2=[]
    lista2=['cane','gatto','cinghiale','tardigrado','axolotol','salmone','bufalo','bue','cervo','lupo', 'canocchia','medusa','umano','orangotango','babbuino',
            'squalo','cetriolo di mare','struzzo', 'camaleonte','nutria']
    lista10=[]


    
    for k in range (0,10):
        numero=random.randint(0,19)
        
        aggiungi= lista2[numero]
        lista10.append(aggiungi)
          
        
    listaMagg=[]
    listaMin=[]
    for i in range (0,10):
        if len(lista10[i])>= 5 :
            listaMagg.append(lista10[i])
        else:
            listaMin.append(lista10[i])
    maggiore=len(listaMagg)
    minore= len(listaMin)
            
    context={
        'lista' : lista2,
        'altraLista' : lista10,
        'listaMagg' : listaMagg,
        'listaMin' : listaMin,
        'maggiore' : maggiore,
        'minore' : minore
    }
    
    return render(request, "prova_pratica_2/stringhe.html",context)