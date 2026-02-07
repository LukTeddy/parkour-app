from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .models import Post, Spot, Comment, CommentMedia
from .forms import SpotForm, CommentForm, CommentMediaForm

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'home/main_menu.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'adelaide/map.html' # <app>/<model>_<view_type>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

def adelaide(request):
    return render(request, 'adelaide/map.html')

def spot_list(request):
    spots = Spot.objects.all()
    return render(request, 'adelaide/spot_list.html', {'spots' : spots})

def spot_detail(request, spot_id):
    spot = get_object_or_404(Spot, id=spot_id)
    comments = spot.comments.all()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        media_form = CommentMediaForm(request.POST, request.FILES)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.spot = spot
            comment.save()

            if media_form.is_valid():
                for media in request.FILES.getlist('media_file'):
                    media_type = media_form.cleaned_data['media_type']
                    media_instance = CommentMedia(comment=comment, media_file=media, media_type=media_type)
                    media_instance.save()

            return redirect('spot-detail', spot_id=spot.id)
    else:
        comment_form = CommentForm()
        media_form = CommentMediaForm()
    return render(request, 'adelaide/spot_detail.html', {
        'spot': spot,
        'comments': comments,
        'comment_form': comment_form,
        'media_form': media_form
    })

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.user == request.user:
        comment.delete()
        return redirect('spot-detail', spot_id=comment.spot.id)
    else:
        return redirect('spot_detail', spot_id=comment.spot.id)

@login_required
def add_spot(request):
    if request.method == "POST":
        form = SpotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('spot-list')
    else:
        form = SpotForm()
    return render(request, 'adelaide/add_spot.html', {'form': form})