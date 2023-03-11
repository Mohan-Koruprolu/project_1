from django.shortcuts import render

posts=[
    {
    'author': 'Mohan',
    'title':'Blog post 1',
    'content':'First post content',
    'date_posted':'August 27,2018'
    },
    {
        'author': 'user',
        'title': 'Blog post 2',
        'content': 'second post content',
        'date_posted': 'August 28,2018'
    }
]
def home(request):
    context={
        'posts': posts
    }
    return render(request, 'blog/home.html',context)


def about(request):
    return render(request, 'blog/about.html')
# Create your views here.
