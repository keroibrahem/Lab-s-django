from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from .models import Book

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def book_list(request):
    books = Book.objects.filter(user=request.user)
    return render(request, 'book_list.html', {'books': books})

@permission_required('books.view_book')
def all_books(request):
    return render(request, 'book_list.html', {'books': Book.objects.all()})
