from django.contrib import admin
from django.urls import path
from books import views
from django.contrib.auth import views as auth_views

urlpatterns = [
     path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('', views.book_list, name='book_list'),
    path('all/', views.all_books, name='all_books'),
]
