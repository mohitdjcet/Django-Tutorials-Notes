from django.shortcuts import render
from datetime import datetime

def blog_details(request):
    post ={
        "title": "My Second Templates Post",
        "descriptions": "Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.",
        "author": "yes",
        "created_at": datetime(2025,8,19,10,30),
        "comments_count": 5,
        "tags": ["Django", "Python", "Web Development"],
        "price":100,
        "number": 7,
    }
    return render(request,'blog/blog_details.html',{"post":post})
