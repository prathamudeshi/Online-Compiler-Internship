import sys
from django.shortcuts import render,redirect
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
    

def login_page(request):
    return render(request, 'login.html')

def registerstu(request):
    if request.method == "POST":
        first_name = request.POST.get('stu_first_name')
        last_name = request.POST.get('stu_last_name')
        username = request.POST.get('stu_username')
        rollno = request.POST.get('rollno')
        password = request.POST.get('password')

        user = User.objects.create(
            first_name=  first_name,
            last_name = last_name,
            username = username,
            is_staff = False
        )

        user.set_password(password)
        user.save()

        student = Student.objects.create(
            user = user,
            rollno = rollno
        )

        student.save()

        return redirect('/register-student/')



    return render(request, 'registerstu.html')

def registerfac(request):
    if request.method == "POST":
        first_name = request.POST.get('fac_first_name')
        last_name = request.POST.get('fac_last_name')
        username = request.POST.get('fac_username')
        # rollno = request.POST.get('rollno')
        password = request.POST.get('password')

        user = User.objects.create(
            first_name=  first_name,
            last_name = last_name,
            username = username,
            is_staff = True
        )

        user.set_password(password)
        user.save()

        faculty = Faculty.objects.create(
            user = user,
            # rollno = rollno
        )

        faculty.save()

        return redirect('/register-faculty/')



    return render(request, 'registerfac.html')