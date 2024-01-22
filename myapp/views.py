from django.shortcuts import render, redirect
from pytube import *


def youtube(request):
    if request.method == 'POST':
        link = request.POST['link']

        video = YouTube(link)

        # Setting video resolution
        stream = video.streams.get_lowest_resolution()

        stream.download()

        return redirect('youtube')

    return render(request, 'form.html')


