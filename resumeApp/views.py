from django.shortcuts import render
from .models import Resume 
from .forms import ResumeForm

# Create your views here.

def Home(request):
    if request.method == 'POST':
        fm = ResumeForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
    else:
        fm = ResumeForm()
    candidates = Resume.objects.all()
    return render(request, 'index.html',{'form':fm,'candidates':candidates})



def Data(request, id):
    data = Resume.objects.get(pk=id)
    return render(request, 'candidate.html',{'c':data})
