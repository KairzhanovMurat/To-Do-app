from . import views
from django.urls import path

app_name = 'Tasks'
urlpatterns = [
    path('',views.addTask,name=''),
    path('add/',views.addTask,name='add'),
    path('del/<int:id>',views.deleteTask,name='del')
]
