from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Article

# Create your views here.

def home(request):
	artykuly = Article.objects.all().order_by('-date')[:10]
	return render(request, 'tablica/tablica.html', {'artykuly':artykuly})

# def wpis(request, wpis_id):
# 	wpis = get_object_or_404(Article, pk=wpis_id)
# 	return render(request, 'tablica/wpis.html', {'wpis':wpis})


def wpis(request, slug):
	wpis = get_object_or_404(Article, slug=slug)
	return render(request, 'tablica/wpis.html', {'wpis':wpis})

def redakcja(request):
	return render(request, 'tablica/redakcja.html')

def kontakt(request):
	return render(request, 'tablica/kontakt.html')

def archiwum(request):
	artykuly = Article.objects.all().order_by('-date')[10:]
	paginator = Paginator(artykuly, 2)
	page = request.GET.get('page')

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	return render(request, 'tablica/archiwum.html', {'page':page, 'posts':posts,
		'artykuly':artykuly})


def wyszukaj(request):
	if request.method == "GET":
		szukaj = request.GET.get('search')
		#wyniki = Article.objects.all().filter(title=szukaj)
		wyniki = []
		for post in Article.objects.all():
			if szukaj.lower() in post.title.lower() or szukaj.lower() in post.description.lower():
				wyniki.append(post)
		return render(request, 'tablica/wyszukaj.html', {'wyniki': wyniki})





