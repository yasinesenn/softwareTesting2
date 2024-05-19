from django.urls import include, path
#now import the views.py file into this code
from . import views

urlpatterns=[
path('', views.index,name="index"),
path('index/', views.index,name="index"),
path('blogs/', views.Blogs,name="Blogs"),
path('blog_details/<int:post_id>/', views.blog_detail_view, name="blog_detail"),
path('industries/', views.industries_list, name='industries'),
path('industry_details/<int:industry_id>/', views.industry_details, name='industry_details'),
path('ajax_login/', views.ajax_login, name='ajax_login'),
path('logout/', views.logout_view, name='logout'),
path('register/', views.register_view, name='register'),
]