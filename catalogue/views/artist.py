from django.shortcuts import render

from catalogue.models import Artist

# Create your views here.
def index(request):
	artists = Artist.objects.all()
	title = 'Liste des artistes'
	
	return render(request, 'artist/index.html', {'artists':artists,'title':title})