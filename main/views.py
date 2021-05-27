from django.shortcuts import render
import random
import string

# Create your views here.
def passgen(request):
    
    if request.method == 'POST':
        data = request.POST['digit']
        len = int(data)
        letter = string.ascii_letters + string.punctuation + string.digits
        passwrd = ''.join(random.sample(letter,len))
        return render(request, 'main.html', {'passwrd':passwrd})
    else:
        return render(request, 'main.html')

    