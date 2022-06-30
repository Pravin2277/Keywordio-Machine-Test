from django.shortcuts import render
from . import views
from django.urls import path

urlpatterns=[
	path('',views.login),
	path('signup/',views.signup),
	path('list/',views.ListBooksAPIView.as_view()),
	path('create/',views.CreateBooksAPIView.as_view()),
	path('update/<int:pk>',views.UpdateBooksAPIView.as_view()),
	path('delete/<int:pk>',views.DeleteBooksAPIView.as_view()),
]