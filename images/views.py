from django.shortcuts import render
from .models import Image

def index(request):
    # Get most recent image and display it on the home page
    image = Image.objects.latest('date_taken')
    return render(request, 'index.html', {'image': image})

def detail(request, image_id):
    image = Image.objects.get(id=image_id)
    return render(request, 'detail.html', {'image': image})

def search(request):
    query = request.GET['query']
    images = Image.objects.filter(name__icontains=query) | Image.objects.filter(description__icontains=query) | Image.objects.filter(labels__icontains=query)
    return render(request, 'search.html', {'images': images})