from django.shortcuts import render

def index(request):
        return render (request,"prima_app/index_root.html")