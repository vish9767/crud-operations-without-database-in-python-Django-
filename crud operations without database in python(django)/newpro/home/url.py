from django.urls import *
from . import views
urlpatterns=[
    path('',views.home,name="home"),
    path('add',views.add,name="add"),
    path('delete',views.delete,name="delete"),
    path('edit',views.edit,name="edit"),
    path('save',views.save,name="save"),
]