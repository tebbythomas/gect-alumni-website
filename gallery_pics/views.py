from django.shortcuts import render, redirect
from django.contrib import messages
from .models import GalleryPic


def gallery(request):
    images = GalleryPic.objects.all()
    context = {
        'pics' : images
    }
    return render(request,'gallery/gallery.html', context)
