from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from books_api.views import BookViewSet, ProfileViewSet, index


router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'profile', ProfileViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
