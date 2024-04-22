from django.shortcuts import render
from .models import Image

def home(request):
    # Get most recent image and display it on the home page
    image = Image.objects.latest('date_taken')
    return render(request, 'home.html', {'image': image})

def image_detail(request, image_id):
    image = Image.objects.get(id=image_id)
    return render(request, 'image_detail.html', {'image': image})

def search(request):
    query = request.GET['query']
    images = Image.objects.filter(name__icontains=query) | Image.objects.filter(description__icontains=query) | Image.objects.filter(labels__icontains=query)
    return render(request, 'search.html', {'images': images})