from django.shortcuts import get_object_or_404, redirect, render
from .forms import CommentForm
from Software.models import BlogPost, Category, Comment, Industry
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User

# Create your views here.

def index(request):   
    return render(request,'index.html')
            
def Blogs(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'Blogs.html', {'blog_posts': blog_posts})


def blog_detail_view(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    previous_post = BlogPost.objects.filter(id__lt=post_id).order_by('-id').first()
    next_post = BlogPost.objects.filter(id__gt=post_id).order_by('id').first()
    recent_posts = BlogPost.objects.order_by('-date_posted')[:3]
    categories = Category.objects.all()
    

    return render(request, 'blog_detail.html', {'post': post, 'previous_post': previous_post, 'next_post': next_post, 'recent_posts':recent_posts,'categories': categories})

def industries_list(request):
    industries = Industry.objects.all()
    return render(request, 'industries.html', {'industries': industries})

def industry_details(request, industry_id):
    industry = get_object_or_404(Industry, pk=industry_id)
    return render(request, 'industry_details.html', {'industry': industry})

@csrf_exempt
def ajax_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'failure', 'message': 'Invalid credentials'})
    return JsonResponse({'status': 'failure', 'message': 'Only POST method is allowed'})

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({'status': 'failed', 'message': 'Username already exists'})
        
        user = User.objects.create_user(username=username, password=password)
        
    
        user = authenticate(request, username=username, password=password)
        login(request, user)
        

        
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'failed', 'message': 'Invalid request method'})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed', 'message': 'Invalid request method'})
