from django.shortcuts import render

def home(request):
    return render(request, 'base.html')

def blog(request):
    students_list =[
        {"name":"Mohit", "class":"10th"},
        {"name":"Rohit", "class":"9th"},
        {"name":"Sohit", "class":"8th"},
    ]
    return render(request, 'blog.html', {'students': students_list})
