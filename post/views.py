from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import PostForm, CommentForm 
from .models import Post
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

# Create your views here.
""" @login_required
def add_post(req):
  if req.method == 'POST':
    form = PostForm(req.POST)

    if form.is_valid():
      form.instance.author = req.user
      form.save()
      return redirect('home')
  else:
    form = PostForm()

  return render(req, 'posts/add_post.html', {'form': form}) """

@method_decorator(login_required, name = 'dispatch')
class AddPostView(CreateView):
  model = Post
  form_class = PostForm
  template_name = 'posts/add_post.html'
  success_url = reverse_lazy('home')

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

""" @login_required
def edit_post(req, id):
  post = Post.objects.get(pk=id)

  if req.method == 'POST':
    form = PostForm(req.POST, instance = post)
    if form.is_valid():
      form.instance.author = req.user
      form.save()
      return redirect('home')
  else:
    form = PostForm(instance = post)

  return render(req, 'posts/add_post.html', {'form': form}) """

@method_decorator(login_required, name = 'dispatch')
class EditPostView(UpdateView):
  model = Post
  form_class = PostForm
  template_name = 'posts/add_post.html'
  pk_url_kwarg = 'id'
  success_url = reverse_lazy('all-posts-by-user')

  def form_valid(self, form):
    messages.success(self.request, 'Post updated.')
    return super().form_valid(form)

""" @login_required
def delete_post(req, id):
  Post.objects.get(pk = id).delete()

  return redirect('home') """

@method_decorator(login_required, name = 'dispatch')
class DeletePostView(DeleteView):
  model = Post
  template_name = 'posts/delete.html'
  pk_url_kwarg = 'id'
  success_url = reverse_lazy('all-posts-by-user')

@method_decorator(login_required, name = "dispatch")
class DetailPostView(DetailView):
  template_name = 'posts/post_detail.html'
  model = Post
  pk_url_kwarg = 'id'

  def post(self, request, *args, **kwargs):
    post = self.get_object()

    if self.request.method == 'POST':
      comment_form = CommentForm(self.request.POST)

      if comment_form.is_valid():
        new_comment = comment_form.save(commit=False)
        new_comment.post = post
        new_comment.save()

    return self.get(request, *args, **kwargs)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    post = self.object
    comments = post.comments.all()
    comment_form = CommentForm()

    context['comments'] = comments
    context['comment_form'] = comment_form
    return context