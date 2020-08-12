from django.shortcuts import render
from django.views.generic import ListView, TemplateView, View, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Post, Comment
from django.urls import reverse_lazy
from django.http import HttpResponse

from django.http import HttpResponse 
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from django.contrib.auth.models import User
from users.models import CustomUser

from .forms import CommentForm, PostCreateForm
from django.contrib.auth import get_user_model

from django.core.paginator import Paginator

from django.db.models.signals import post_save
from notifications.signals import notify
from story_blog.models import Comment

User = get_user_model()

# Create your views here.


class BlogListView(ListView):
    
    # model = Post
    # qset = Post.objects.order_by('-creation_time')
    # template_name = 'home.html'
    # login_url = 'login'

    def get(self, request, *args, **kwargs):
        featured = Post.objects.order_by('-timestamp')

        paginator = Paginator(featured, 4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        context = {
            'object_list': page_obj,
        }
        return render(request, 'home.html', context)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ('title', 'content', 'image')
    template_name = 'post_edit.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kawargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kawargs)

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    login_url = 'login'

    def dispatch(self, request, *args, **kawargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kawargs)

class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'comment_delete.html'
    success_url = "/{post_id}/detail/"
    login_url = 'login'

    def dispatch(self, request, *args, **kawargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kawargs)

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'
    login_url = 'login'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy('home')
    form_class = PostCreateForm
    template_name = 'post_create.html'
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    success_url = "/{post_id}/detail/"
    form_class = CommentForm
    template_name = 'comment.html'
    login_url = 'login'

    def form_valid(self,form,*args,**kwargs):
        self.object = form.save(commit = False)
        self.object.author = self.request.user
        self.object.post = Post.objects.get(pk=self.kwargs['pk'])
        self.object.save()
        return super().form_valid(form)



class ProfileView(ListView):
    model = Post
    template_name = ['profile_page.html', 'profile_edit.html']
    login_url = 'login'


    def get(self, request, *args, **kwargs):
        user_profile = CustomUser.objects.get(pk=self.kwargs['pk'])
        
        author = user_profile.username
        u = User.objects.get(username=author)
        featured = Post.objects.filter(author=u)
        featured = featured.order_by('-timestamp')
        
        template_file = 'profile_page.html'
        

        context = {
                'user_profile': user_profile,
                'object_list': featured,
                'author': author,
            }
        return render(request, template_file, context)



class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    success_url = reverse_lazy('home')
    fields = ('username','email', 'profile',)
    login_url = 'login'
    template_name = 'profile_edit.html'
    

    def dispatch(self, request, *args, **kawargs):
        obj = self.get_object()
        if obj.id != self.request.user.id:
            raise PermissionDenied
        return super().dispatch(request, *args, **kawargs)

    # def get(self, request, *args, **kwargs):
    #     user_profile = CustomUser.objects.get(pk=self.kwargs['pk'])
    #     template_name = 'profile_edit.html'
    #     context = {
    #             'user_profile': user_profile,     
    #     }
    #     return render(request, template_name, context)



# from django.dispatch import Signal, receiver

from .models import CommentNotification

from notifications.signals import notify

class NotificationView(LoginRequiredMixin, ListView):

    login_url = 'login'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=10)
        featured = user.notifications.unread()

        context = {
            'object_list': featured,
        }
        
        return render(request, 'notification.html', context)





def my_handler(sender, instance, created, **kwargs):
    notify.send(instance,  recipient=User.objects.get(pk=10), verb='was saved')



post_save.connect(my_handler, sender=Comment)

