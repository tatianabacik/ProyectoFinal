from django.http import response
from django.shortcuts import render, HttpResponse, redirect
from mainapp.models import Article

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html')

def pagina2(request):
    return render(request, 'mainapp/pagina2.html')

def pagina3(request):
    return render(request, 'mainapp/pagina3.html')

def crear_articulo(request):
    articulo = Article(
        title = 'Segundo articulo',
        content = 'Contenido del segundo articulo',
        public = True
    )
    articulo.save()
    return HttpResponse(f'Articulo Creado: {articulo.title}')

def articulo(request):
    try:
        articulo = Article.objects.get(title = 'Primer articulo')
        response = f'Mostrando Articulo: {articulo.title}'
    except:
        response = 'Articulo no encontrado'

    return HttpResponse(response)

def editar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.title = 'Primer Articulo Modificado'
    articulo.content = 'Contenido modificado del primer articulo'
    articulo.public = True

    articulo.save()
    return HttpResponse(f'Articulo Editado: {articulo.title} <br>{articulo.content}')

def articulos(request):
    articulos = Article.objects.all() #order_by('id')[0:1] muestra solo un elemento, funciona igual que una lista
    articulos = Article.objects.filter(title__contains = 'articulo').exclude( public = False )
    return render(request, 'mainapp/articulos.html',{
        'articulos' : articulos
    })

def borrar_articulo(request, id):
    articulo = Article.objects.get(pk = id)
    articulo.delete()

    return redirect('articulos')

def save_article(request):
    articulo = Article(
        title = title,
        content = content, 
        public = public
    )
    articulo.save()
    return HttpResponse(f'Articulo Creado: {articulo.title}')

def create_article(request):
    return render(request, 'mainapp/create_article.html')