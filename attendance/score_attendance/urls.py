from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:student_id>/addscore', views.addscore, name='addscore'),
    path('<int:student_id>/subtractscore', views.subtractscore, name='subtractscore'),
]
