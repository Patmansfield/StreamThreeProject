from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.contrib.auth.decorators import login_required


@login_required
def post_list(request):
    top = request.GET.get('top', False)
    if top:
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-views')[:3]
    else:
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "blog/blogtests.html", {'posts': posts})


@login_required
def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    post.views += 1
    post.save()
    return render(request, "blog/postdetail.html", {'post': post})
