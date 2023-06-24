from django.shortcuts import render

# Create your views here.
def index(requets):
    return render(requets, 'index.html')

def galeria(requets):
    return render(requets, 'galeria.html')



def galeria1(requets):
    return render(requets, 'galeria-1.html')
    
    

def galeria2(requets):
    return render(requets, 'galeria-2.html')

def artistai(requets):
    return render(requets,'artista-i.html' )

def artistal(requets):
    return render(requets,'artista-l.html' )

def pinturaslocales(requets):
    return render(requets, 'pinturas-locales.html')


def pi(requets):
    return render(requets, 'p-i.html')
