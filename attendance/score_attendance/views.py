from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
# Create your views here.

def index(request):
    # Generate Number of students in the database
    # num_students=Student.objects.all().count()

    # return render(
    #     request,
    #     'index.html',
    #     context={'num_students':num_students}
    # )
    return HttpResponse('Attendance Record')
