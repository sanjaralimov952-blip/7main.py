# 7main.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World")from django.http import HttpResponse
from django.views import View

class HomeView(View):
    def get(self, request):
        return HttpResponse("Hello World")
        path('', home),
        path('', HomeView.as_view()),
        def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})from django.views.generic import ListView

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    from django.views.generic import CreateView

class PostCreateView(CreateView):
    model = Post
    fields = '__all__'
    template_name = 'post_form.html'
    success_url = '/'
