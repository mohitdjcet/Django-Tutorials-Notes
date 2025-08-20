from django.shortcuts import render
from datetime import datetime

def blog_details(request):
    blogs =[
        {"title":"Dhango Basics","is_featured":True, "author":"Mohit Kumar"},
        {"title":"Django Advanced","is_featured":False, "author":""},
        {"title":"Django REST Framework","is_featured":False, "author":"Anu Choudhary"},
    ]
    context = {
        "blogs":blogs,
        "today": datetime.now(),
        "html_code":"<b>Welcome to My Blog</b>",
    }
    return render(request, 'blog/blog_list.html', context)
