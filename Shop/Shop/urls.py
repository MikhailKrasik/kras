"""Shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from catalog.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/catalogs',Catalogs.as_view()),
    path('catalog/author/<int:pk>', AuthorDetail.as_view(), name='author-detail-view'),
    path('catalog/genre/<int:pk>', GenreDetail.as_view(), name='genre-detail-view'),
    path('catalog/seria/<int:pk>', SeriaDetail.as_view(), name='seria-detail-view'),
    path('catalog/publishinghouse/<int:pk>',  PublishingHouseDetail.as_view(), name='publishinghouse-detail-view'),
    path('catalog/author/', AuthorList.as_view(), name='author-list-view'),
    path('catalog/genre/', GenreList.as_view(), name='genre-list-view'),
    path('catalog/seria/', SeriaList.as_view(), name='seria-list-view'),
    path('catalog/genre-create/', GenreCreate.as_view()),
    path('catalog/publishinghouse/', PublishingHouseList.as_view(),name='publishinghouse-list-view')
]
