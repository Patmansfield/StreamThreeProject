from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def get_index(request):
   return render(request, 'index.html')


@login_required
def articleone(request):
   return render(request, 'article/articleone.html')


@login_required
def articletwo(request):
   return render(request, 'article/articletwo.html')


@login_required
def articlethree(request):
   return render(request, 'article/articlethree.html')

