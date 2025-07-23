from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import BlogPost
from .forms import BlogPostForm
from django.contrib import messages

# View to create a new blog post
@permission_required('blog.can_create', raise_exception=True)
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Blog post created successfully!")
            return redirect('blog:post_list')
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_post.html', {'form': form})

# View to edit an existing blog post
@permission_required('blog.can_edit', raise_exception=True)
def edit_blog_post(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=blog_post)
        if form.is_valid():
            form.save()
            return redirect('blog:post_detail', pk=blog_post.pk)
    else:
        form = BlogPostForm(instance=blog_post)
    return render(request, 'blog/edit_post.html', {'form': form, 'blog_post': blog_post})

# view to delete a blog post
@permission_required('blog.can_delete', raise_exception=True)
def delete_blog_post(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    blog_post.delete()
    return redirect('blog:post_list')     

# View to view a blog post (for viewers)
@permission_required('blog.can_view', raise_exception=True)
def view_blog_post(request, pk):
     blog_post = get_object_or_404(BlogPost, pk=pk)
     return render(request, 'blog/view_post.html', {'blog_post': blog_post})