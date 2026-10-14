from django.shortcuts import render, redirect
from .models import SharedFile

def index(request):
    if request.method == 'POST' and request.FILES.getlist('files'):
        for uploaded_file in request.FILES.getlist('files'):
            SharedFile.objects.create(file=uploaded_file)
        return redirect('index')

    files = SharedFile.objects.all().order_by('-uploaded_at')
    return render(request, 'core/index.html', {'files': files})