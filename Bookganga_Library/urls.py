"""Bookganga_Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

from User import views as user_view

from BG_Library import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("welcome/", views.home, name = "home_page"),
    path("all-books/", views.show_all_books, name = "all_books"),
    path("update-book/<int:pk>/",views.update_book, name = "update_book"),
    path("delete-book/<int:pk>/", views.delete_book , name = 'delete_book'),
    
    #create csv url
    path('create-csv/', views.create_csv, name = "create_csv"),
    path("upload-csv/", views.upload_csv, name = "upload_csv"),


    #Class based views

    path("cbv/", views.NewView.as_view(), name = "cbv"),
    path('cbv-create-book/', views.BookCreate.as_view(), name = "BookCreate"),
    path('cbv-book-list/', views.BookRetrieve.as_view(), name = "BookRetrieve"),
    path('cbv-book-detail/<int:pk>/', views.BookDetail.as_view(), name = "BookDetail"),
    path("cbv-update_book/<int:pk>/", views.BookUpdate.as_view(), name = "BookUpdate"),
    path("cbv-delete-book/<int:pk>/", views.BookDelete.as_view(), name = "BookDelete"),


    #User URLs
    path("register/", user_view.register_request, name = "register"),
    path("login/", user_view.login_request, name = "login_user"),
    path('logout/', user_view.logout_request, name = "logout_user"),
]
