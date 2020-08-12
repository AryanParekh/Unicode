from django.shortcuts import render
from task1 import Binary
from .forms import NumberInputForm
# Create your views here.
def get_numbers(request):
    if request.method=='POST':
        form=NumberInputForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            result=str(Binary.con_checker(cd['a'],cd['b']))
            return render(request,'index2.html',{'result':result})
    else:
        form=NumberInputForm()
    return render(request,'index1.html',{"form":form})
