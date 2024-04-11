from rest_framework import viewsets
from django.shortcuts import render, redirect

from .models import Book, Profile
from .serializers import BookSerializer, ProfileSerializer
from .forms import BookForm


def index(request):
    book_form = BookForm()
    if request.method == 'POST':
        if 'submit_book' in request.POST:
            book_form = BookForm(request.POST)
            if book_form.is_valid():
                book_form.save()
                return redirect('/')
        elif 'save_changes' in request.POST:
            for profile in Profile.objects.all():
                is_visible = request.POST.get(f'visibility_{profile.column_name}', 'off') == 'on'
                if profile.is_visible != is_visible:
                    profile.is_visible = is_visible
                    profile.save()

    books = Book.objects.all()
    profiles = Profile.objects.all()
    visibility = {profile.column_name: profile.is_visible for profile in profiles}
    return render(request,
                  'books_api/index.html',
                  {'books': books,
                   'profiles': profiles,
                   'book_form': book_form,
                   'visibility': visibility})


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    http_method_names = ['get', 'put', 'patch']
