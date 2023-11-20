from django.shortcuts import render

# Create your views here.
def forloop(request):
  d={'name':'sreenu'}
  return render(request,'forloop.html',d)