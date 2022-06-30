from django.db import models

class Books(models.Model):
	name=models.CharField(max_length=100)
	author=models.CharField(max_length=100)
	publication=models.CharField(max_length=150)

	def __str__(self):
		return self.name



class Student(models.Model):
	firstname=models.CharField(max_length=50)
	lastname=models.CharField(max_length=50)
	email=models.EmailField()
	password=models.CharField(max_length=50)

	@staticmethod
	def get_object(email):
		return Student.objects.get(email=email)
	def __str__(self):
		return self.firstname
