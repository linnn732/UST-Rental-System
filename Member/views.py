from django.shortcuts import render, redirect
from .forms import MemberModelForm

# Create your views here.




def register(request):
    form = MemberModelForm()
    context = {}
    if request.method == "POST":
        form = MemberModelForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data['email']
            print(email)
            form.save()
            context['successful_submit']=True
            #return redirect('register')
    
    context['form']=form

    return render(request, 'register.html', context)
