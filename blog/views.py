from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Comments


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments1 = Comments.objects.filter(comments_post_id=pk)
    #comments = Comments.objects.all()
    print('test')
    print(comments1)
    print('test')
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments1})

