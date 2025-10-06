from django.shortcuts import render, redirect, get_object_or_404
from .models import Video
from .forms import VideoForm

# Create
def add_video(request):
    if request.method == "POST":
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_videos')
    else:
        form = VideoForm()
    return render(request, 'inventory/add_video.html', {'form': form})

# Read
def list_videos(request):
    videos = Video.objects.all()
    return render(request, 'inventory/list_videos.html', {'videos': videos})

# Update
def edit_video(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == "POST":
        form = VideoForm(request.POST, instance=video)
        if form.is_valid():
            form.save()
            return redirect('list_videos')
    else:
        form = VideoForm(instance=video)
    return render(request, 'inventory/edit_video.html', {'form': form})

# Delete
def delete_video(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == "POST":
        video.delete()
        return redirect('list_videos')
    return render(request, 'inventory/delete_video.html', {'video': video})
