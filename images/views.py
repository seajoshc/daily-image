from django.shortcuts import render
from .models import Image

def index(request):
    # Get image that has is_current_image set to True
    image = Image.objects.filter(is_current_image=True).first()
    return render(request, 'index.html', {'image': image})

def detail(request, image_id):
    image = Image.objects.get(id=image_id)
    return render(request, 'detail.html', {'image': image})

def search(request):
    query = request.GET['query']
    images = Image.objects.filter(name__icontains=query) | Image.objects.filter(description__icontains=query) | Image.objects.filter(labels__icontains=query)
    return render(request, 'search.html', {'images': images})