import sys

from django.shortcuts import render
from pycompiler.models import *

def index(request):
    return render(request, 'index.html')

def runcode(request):

    if request.method == "POST":
        codeareadata = request.POST['codearea']
        input_part = request.POST['inputarea']
        y = input_part
        input_part = input_part.replace("\n"," ").split(" ")
        def input():
            a = input_part[0]
            del input_part[0]
            return a

        try:
            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(codeareadata)  
            sys.stdout.close()
            sys.stdout = original_stdout  
            output = open('file.txt', 'r').read()

        except Exception as e:
            sys.stdout = original_stdout
            output = e

    return render(request , 'index.html', {"code":codeareadata, "input":y , "output":output})



def submitcode(request):
    return render(request, 'submit.html')


def submitgg(request):
    if request.method == "POST":
        codeareadata = request.POST['codearea']
        input_part = request.POST['inputarea']
        y = input_part
        input_part = input_part.replace("\n"," ").split(" ")
        def input():
            a = input_part[0]
            del input_part[0]
            return a

        try:
            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w') 
            exec(codeareadata) 
            sys.stdout.close()
            sys.stdout = original_stdout 
            output = open('file.txt', 'r').read()

        except Exception as e:
            sys.stdout = original_stdout
            output = e

        
        code  = Code.objects.create(
            code = codeareadata,
            output = output
        )
        code.save()

        return render(request , 'index.html', {"code":codeareadata ,"input":y, "output":output})
    

