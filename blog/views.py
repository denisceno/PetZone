from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import StoryForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/blog_list.html', {'posts': posts})


def blog_detail(request, id):
    template_name = "blog/blog_details.html"
    post = get_object_or_404(BlogPost, id=id)
    is_author = post.author == request.user
    is_superuser = request.user.is_superuser
    context = {
        'post': post,
        'is_author': is_author,
        'is_superuser': is_superuser
    }
    return render(request, template_name, context)


@login_required
def blog_create(request):
    if request.method == 'POST':
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Your post has been created!")
            return redirect('blog_list')
    else:
        form = StoryForm()
    return render(request, 'blog/blog_create.html', {'form': form})


@login_required
def blog_edit(request, id):
    post = get_object_or_404(BlogPost, id=id)
    if request.user != post.author :
        messages.error(request, "You are not authorized to edit this post.")
        return redirect('blog_detail', id=id)

    if request.method == 'POST':
        form = StoryForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Your post has been updated!")
            return redirect('blog_detail', id=id)
    else:
        form = StoryForm(instance=post)

    return render(request, 'blog/blog_update.html', {'form': form})


@login_required
def blog_delete(request, id):
    post = get_object_or_404(BlogPost, id=id)

    if request.user != post.author and not request.user.is_superuser:
        messages.error(request, "You are not authorized to delete this post.")
        return redirect('blog_detail', id=id)

    if request.method == "POST":
        post.delete()
        messages.success(request, "Your post has been deleted!")
        return redirect('blog_list')

    return render(request, 'blog/blog_delete.html', {'post': post})
