from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from django.utils import timezone

from blog.models import Post
from .forms import PostForm

# Create your views here.
def post_list(request):
    qs = Post.objects.all()
    qs = qs.filter(published_date__lte=timezone.now())
    qs = qs.order_by('published_date')
    return render( request, 'blog/post_list.html', 
        {'post_list': qs,}
    )

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'blog/post_detail.html',
        {'post': post,}
    )

#@login_required
def post_new(request):
    # request.POST, request.FILES

    if request.method == 'POST':
        form = PostForm( request.POST, request.FILES )
        if form.is_valid():
            post = form.save( commit=False )
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect( 'post_detail', post.pk )
    else:
        form = PostForm()
   
    return render( request, 'blog/post_edit.html', 
        {'form': form }
    )
    #pass

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm( request.POST, request.FILES, instance=post )
        if form.is_valid():
            post = form.save( commit=False )
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect( 'post_detail', post.pk )
    else:
        form = PostForm(instance=post)    

    return render(request, 'blog/post_edit.html',
       {'form': form }
    )

