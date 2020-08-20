from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post
from .forms import FilterForm


# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all
    }
    return render(request, 'myfarm/home.html', context)
    #Alternative: HttpResponse('<h1>Django Test Home<h1>')

def about(request):
    return render(request, 'myfarm/about.html', {'title': 'About'})

def categories(request):
    return render(request, 'myfarm/categories.html')

def fruits(request):
    return render(request, 'myfarm/category/fruits.html')

def vegetable(request):
    return render(request, 'myfarm/category/vegetable.html')


class PostListView(ListView):
    model = Post
    template_name = 'myfarm/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] #ordering posts from latest to oldest

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'city', 'category', 'product', 'product_type', 'amount_av_min', 'amount_av_max', 'price_min', 'price_max']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'city', 'category','product', 'product_type', 'amount_av_min', 'amount_av_max', 'price_min', 'price_max']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self): #prevent that a user can update other users posts
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self): #prevent that a user can update other users posts
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class FilterView(TemplateView):
    template_name = 'myfarm/filter.html'

    def filter(self, request): #get request
        form = FilterForm()
        posts = Post.objects.all()
        print(posts)
        print("inside def filter / Get request")
            #return render(request, 'myfarm/filter.html')
        return render(request, self.template_name, {'form': form})
            #return render(request, self.template_name, )

    def post(self, request):
        form = FilterForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']
            post = form.save()
            post.save()
            form = FilterForm()
            post = form.save()
            return redirect('filter:filter')

        args = {'form' : form}
        return render(request, self.template_name, args)