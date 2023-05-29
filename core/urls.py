from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.get_main_page, name='main'),
    path('groups/', views.GroupList.as_view(), name='groups'),
    path('courses/', views.CourseList.as_view(), name='courses'),
    path('users/', views.UserList.as_view(), name='users'),
    path('user_detail/<int:pk>', views.UserDetail.as_view(), name='user_detail')
]
