from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Post
from django.contrib.auth import logout

def index(request):
    context = {
        'posts': Post.objects.order_by('-created_date')
        if request.user.is_authenticated else []
    }

    return render(request, 'blog/index.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:index'))