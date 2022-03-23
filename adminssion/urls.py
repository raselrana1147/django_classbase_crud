from django.urls import path
from adminssion import views


app_name='crud'

urlpatterns = [
    path('',views.StudentCreateView.as_view(), name='home_page'),
    path('student_list/',views.StudentListView.as_view(), name='student_list'),
    path('edit_student/<int:pk>',views.StudentUpdateView.as_view(), name='edit_student'),
    path('delete_student/<int:pk>',views.StudentDeleteView.as_view(), name='delete_student'),
]

