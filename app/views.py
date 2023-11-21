from django.shortcuts import render

# Create your views here.
def fun(request):
  d={'name':'rayv'}
  return render(request,'rev.html',d)