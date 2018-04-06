from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
# Create your views here.

def index(request):
    # Generate Number of students in the database
    students=Student.objects.all()

    return render(
        request,
        'index.html',
        context={'students':students}
    )
    # return HttpResponse('Attendance Record ' + str(num_students))
