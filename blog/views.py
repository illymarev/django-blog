from django.views.generic import CreateView, ListView, DeleteView
from django.views.generic.edit import UpdateView
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import CreateUser, CreatePost, CreateComment


# Create your views here.
class UserRegistrationView(CreateView):
    form_class = CreateUser
    model = get_user_model()
    template_name = 'blog/registration.html'
    success_url = reverse_lazy('blog:login')

    def form_valid(self, form):
        form.save()

        return super().form_valid(form)


class MyLoginView(SuccessMessageMixin, LoginView):
    template_name = 'blog/login.html'
    success_message = 'Successful login'

class MyLogoutView(SuccessMessageMixin, LogoutView):
    success_message = 'Successful logout'


class PostFeedView(ListView):
    model = Post
    template_name = 'blog/feed.html'


class CreatePostView(CreateView):
    form_class = CreatePost
    model = Post
    success_url = reverse_lazy('blog:feed')
    template_name = 'blog/createpost.html'

    def form_valid(self, form, commit=True):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)


class UpdatePostView(UpdateView):
    model = Post
    fields = ['title', 'description', 'image']
    template_name = 'blog/updatepost.html'
    success_url = reverse_lazy('blog:feed')


class CreateCommentView(CreateView):
    model = Comment
    form_class = CreateComment
    template_name = 'blog/createcomment.html'
    success_url = reverse_lazy('blog:feed')

    def form_valid(self, form, commit=True):
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.post = self.get_object()
        comment.save()
        return super().form_valid(form)

