from django.shortcuts import render
import datetime
def home(request):
    student={"name":"Fahim","dec":"Fahim Al Imran is a Studen","age":16,"subject":["Bangla","English","Math","ICT"],"date":datetime.datetime.now()}
    return render(request,'home.html',student)