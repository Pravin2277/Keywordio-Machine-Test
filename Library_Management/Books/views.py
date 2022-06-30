from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import RetrieveAPIView
from .serializers import BooksSerializer
from rest_framework import serializers
from .models import Books,Student

def login(request):
	if request.method=='POST':
		email=request.POST.get('email')
		password=request.POST.get('password')
		users=Student.objects.all()
		print(users)
		for user in users:
			if email==user.email:
				return redirect('/list/')
	return render(request,'login.html')

def signup(request):
	if request.POST=='POST':
		firstname=request.POST.get('firstname')
		lastname=request.POST.get('lastname')
		email=request.POST.get('email')
		password=request.POST.get('password')
		student=Student(firstname=firstname,lastname=lastname,email=email,password=password)
		student.save()
		return redirect('/')
	return render(request,'signup.html')

class AuthenticationView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        content = {
            'user': str(request.user),
            'auth': str(request.auth),
        }
        return Response(content)


class ListBooksAPIView(ListAPIView):
	queryset = Books.objects.all()
	serializer_class = BooksSerializer

class CreateBooksAPIView(CreateAPIView):
	queryset = Books.objects.all()
	serializer_class = BooksSerializer

class UpdateBooksAPIView(UpdateAPIView):
	queryset = Books.objects.all()
	serializer_class = BooksSerializer


class DeleteBooksAPIView(DestroyAPIView):
	queryset = Books.objects.all()
	serializer_class = BooksSerializer

