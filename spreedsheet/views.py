from django.shortcuts import render, HttpResponse

def spreedsheet(request):
	return render(request, 'spreedsheet/spreedsheet.html')
# Create your views here.
