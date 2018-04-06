from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Student
# Create your views here.

def index(request):
    # Generate Number of students in the database
    students=Student.objects.all()
    context= {'students':students}

    return render(
        request,
        'score_attendance/index.html',
        context
    )
    # return HttpResponse('Attendance Record ' + str(num_students))

def addscore(request, student_id):
    student = Student.objects.get(pk=student_id)
    student.score+=1
    student.save()
    return HttpResponseRedirect(reverse('index'))

def subtractscore(request, student_id):
    student = Student.objects.get(pk=student_id)
    student.score-=1
    student.save()
    return HttpResponseRedirect(reverse('index'))
