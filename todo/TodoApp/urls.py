# from TodoApp.views import Updatetodo
from django.urls import path
from TodoApp import views
urlpatterns = [
    path('', views.index, name='home'),
    path('task', views.taskss, name='task'),
    path('about', views.about, name='about'),
    path('addtodo', views.addtodo, name='addtodo'),
    path('deletetodo/<int:id>', views.deletetodo, name='deletetodo'),
    # path('updatetodo/<int:pk>', Updatetodo.as_view(), name='updatetodo'),
    path('updatetodo/<int:id>', views.updatetodo, name='updatetodo'),
    path('changestatus/<int:id>/<str:status>', views.changestatus, name='changestatus'),
    path('login', views.login, name='login'),
    path('signout', views.signout, name='signout'),
    path('signup', views.signup, name='signup'),
    path('searchtodo', views.searchtodo, name='searchtodo'),
]
