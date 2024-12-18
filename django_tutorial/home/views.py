from django.shortcuts import render
from django.http import HttpResponse
from . forms import BookingForm
from . models import Departments, Doctors

# Create your views here.

# def about(request):
#     return HttpResponse('About page')
                                            #   to connect response given
# def booking(request):
#     return HttpResponse('Booking page')

# def doctors(request):
#     return HttpResponse('Doctors page')

# def contact(request):
#     return HttpResponse('Contact page')
# def department(request):
#     return HttpResponse('department page')


# def index(request):
#     return render (request, 'index.html')       to connect html page we created in templates



# def index(request):
#     numbers = {'num1': 10}
#     return render(request, 'index.html', {'numbers': numbers})      positive negative no function




# def index(request):
#     person = {
#         'name': 'Vishnu',                        to connect dictionary variable
#         'age': 24,
#         'place': 'Malappuram'
#     }
#     return render(request, 'index.html', {'person': person})



# def index(request):
#     numbers = {'num1':[1,2,3,4,5,6,7,8,9,10]}                   print list of numbers
#     return render(request, 'index.html', {'numbers': numbers})

def index(request):
     numbers = {'fruits':['mango','banana','apple','grapes']}                   
     return render(request, 'index.html', {'numbers': numbers})

def about(request):
    return render (request, 'about.html')

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    form = BookingForm()
    dict_form={
        'form':form
    }
    return render (request, 'booking.html', dict_form)

def doctors(request):
    dict_docs ={
        'doctors': Doctors.objects.all()
    }
    return render (request, 'doctors.html', dict_docs)

def contact(request):
    return render (request, 'contact.html')

def department(request):
    dict_dept ={
        'dept' : Departments.objects.all()
    }
    return render (request, 'department.html',dict_dept)


