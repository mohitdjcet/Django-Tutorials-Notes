from django.urls import path,re_path
from . import views

urlpatterns = [
    path('post/<int:post_id>/',views.post_details, name='post_details'),
    path('user/<str:username>/', views.user_profile, name='user_profile'),
    path('article/<int:year>/<int:month>/<int:days>', views.article_details, name='article_details'),

    re_path(r'^article/(?P<year>[0-9]{4})/$',views.article_by_year, name='article_by_year'),
]