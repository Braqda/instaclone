from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Post


@login_required
def feed(request):
    query = request.GET.get('search', '').strip()

    posts = Post.objects.all()
    if query:
        posts = posts.filter(author__username__icontains=query)

    return render(request, 'posts/feed.html', {
        'posts': posts,
        'search_query': query,
    })


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('feed')
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('feed')
    return redirect('feed')
