from django.shortcuts import render

# Create your views here.

layout = '''<h1>Sitio web con Django | Cristian Guerra</h1>'''

def index(request):
    return render(request, 'mainapp/index.html')

def pagina2(request):
    return render(request, 'mainapp/pagina2.html')

def pagina3(request):
    return render(request, 'mainapp/pagina3.html')