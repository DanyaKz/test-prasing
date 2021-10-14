from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from . import prs

# Create your views here.
def main(request):
    if request.method == 'POST':
        link = request.POST.get('get-information-name')
        parse = prs.Parser(link).main()

        res = {'kk':parse}
        print(parse)
        return render(request,'result.html',res)
    else:
        return render(request,'main.html')
    # return HttpResponse('ok')

# def result(request):
    
#     else:
#         return redirect('/')